#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ArXiv Scraper Script

This script performs the following actions:
1. Reads keywords and settings from `config.ini` in the root directory.
2. Loads the existing paper archive from `data/archive.json` to avoid duplicates.
3. Queries the arXiv API for recent papers matching the keywords.
4. Filters results to find new papers published/updated in the last 48 hours.
5. Overwrites `data/papers_today.md` with a human-readable list of new papers.
6. Appends new paper data to `data/archive.json` for a persistent log.

This script is intended to be run by a GitHub Action from the `scripts/` directory.
"""

import configparser
import arxiv
import json
import logging
import sys
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path

# --- Setup Logging ---
# Set up basic logging to print info and error messages to standard output
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)

# --- Setup Paths ---
# This script is in /scripts, so we go up one level (parent) to get the project root.
try:
    ROOT_DIR = Path(__file__).parent.parent.resolve()
except NameError:
    # Fallback for interactive environments (like notebooks)
    ROOT_DIR = Path('.').resolve().parent

CONFIG_FILE = ROOT_DIR / 'config.ini'
DATA_DIR = ROOT_DIR / 'data'
TODAY_MD_FILE = DATA_DIR / 'papers_today.md'
ARCHIVE_JSON_FILE = DATA_DIR / 'archive.json'
README_FILE = ROOT_DIR / 'README.md'

# Ensure the data directory exists
DATA_DIR.mkdir(exist_ok=True)


def load_config():
    """
    Loads configuration from config.ini.
    
    Returns:
        tuple: (list_of_keywords, max_results)
    """
    if not CONFIG_FILE.exists():
        logging.error(f"Config file not found at: {CONFIG_FILE}")
        raise FileNotFoundError(f"Config file not found: {CONFIG_FILE}")

    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)

    try:
        keywords_str = config.get('arXiv', 'keywords', fallback='')
        # Split keywords by comma, strip whitespace, and filter out empty strings
        keywords = [k.strip() for k in keywords_str.split(',') if k.strip()]
        max_results = config.getint('arXiv', 'max_results', fallback=100)
        
        if not keywords:
            logging.warning("No keywords found in config.ini. The scraper will fetch all recent papers.")
            
        logging.info(f"Loaded {len(keywords)} keywords and max_results={max_results}")
        return keywords, max_results
    except (configparser.NoSectionError, configparser.NoOptionError) as e:
        logging.error(f"Error reading config file: {e}")
        raise

def load_archive():
    """
    Loads the set of seen paper IDs (entry_id) from archive.json.
    
    Returns:
        set: A set of all paper entry_ids found in the archive.
    """
    if not ARCHIVE_JSON_FILE.exists():
        logging.warning(f"Archive file not found at {ARCHIVE_JSON_FILE}. Starting a new one.")
        return set()
    
    try:
        with open(ARCHIVE_JSON_FILE, 'r', encoding='utf-8') as f:
            archive = json.load(f)
            # Use entry_id (the URL) as the unique key
            return {paper['id'] for paper in archive if 'id' in paper}
    except json.JSONDecodeError:
        logging.warning(f"Archive file {ARCHIVE_JSON_FILE} is corrupted. Starting fresh.")
        return set()
    except IOError as e:
        logging.error(f"Could not read archive file: {e}")
        return set()

def build_query(keywords):
    """
    Builds an arXiv API query string from a list of keywords.
    
    Args:
        keywords (list): A list of keyword strings.
        
    Returns:
        str: A formatted query string for the arXiv API.
    """
    if not keywords:
        return "" # Empty query will fetch all recent papers
    
    # Format: (ti:"keyword 1" OR abs:"keyword 1") AND (ti:"keyword 2" OR abs:"keyword 2")
    query_parts = []
    for keyword in keywords:
        # Escape quotes in keyword if any (e.g., "AI 'Safety'")
        safe_keyword = keyword.replace('"', '\\"')
        # Search in title (ti) or abstract (abs)
        query_parts.append(f'(ti:"{safe_keyword}" OR abs:"{safe_keyword}")')
    
    return " AND ".join(query_parts)

def fetch_papers(query, max_results):
    """
    Fetches papers from the arXiv API based on the query.
    
    Args:
        query (str): The formatted query string.
        max_results (int): The maximum number of results to fetch.
        
    Returns:
        list: A list of arxiv.Result objects.
    """
    logging.info(f"Executing query: {query if query else 'ALL_PAPERS'}")
    
    # Search for the most recent submissions that match our query
    try:
        search = arxiv.Search(
            query=query,
            max_results=max_results,
            sort_by=arxiv.SortCriterion.SubmittedDate
        )
        
        results = list(search.results())
        logging.info(f"Fetched {len(results)} raw results from API.")
        return results
    except Exception as e:
        logging.error(f"Error fetching from arXiv API: {e}")
        return []

def filter_new_papers(results, seen_ids):
    """
    Filters for new papers that were published recently and are not in our archive.
    
    Args:
        results (list): List of arxiv.Result objects from the API.
        seen_ids (set): Set of paper entry_ids from our archive.
        
    Returns:
        list: A filtered list of new arxiv.Result objects.
    """
    new_papers = []
    # Define "recent" as the last 2 days (48 hours)
    # This accounts for timezone differences and GitHub Action scheduling delays.
    recent_threshold = datetime.now(timezone.utc) - timedelta(days=2)
    
    for paper in results:
        # Use 'updated' date as it reflects the most recent version.
        # arXiv 'published' date is the date of v1.
        paper_date = paper.updated.astimezone(timezone.utc)
        
        # Check if recent AND not seen before
        if paper_date > recent_threshold and paper.entry_id not in seen_ids:
            new_papers.append(paper)
    
    logging.info(f"Found {len(new_papers)} new paper(s) after filtering.")
    return new_papers

def write_daily_markdown(new_papers):
    """Overwrites the data/papers_today.md file with the day's findings."""
    today_str = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    md_content = [f"# Papers Found on: {today_str}\n"]
    
    if not new_papers:
        logging.info("No new papers to report today.")
        md_content.append("No new papers matching your keywords were found in the last 48 hours.")
    else:
        logging.info(f"Writing {len(new_papers)} new paper(s) to markdown file.")
        
        # Sort papers by published date, newest first
        new_papers.sort(key=lambda p: p.updated, reverse=True)
        
        for paper in new_papers:
            title = paper.title.replace('\n', ' ').strip()
            first_author = paper.authors[0].name if paper.authors else "N/A"
            
            md_content.append(f"### {title}")
            md_content.append(f"* **Authors:** {first_author} et al.")
            md_content.append(f"* **Published (v1):** {paper.published.strftime('%Y-%m-%d')}")
            md_content.append(f"* **Updated:** {paper.updated.strftime('%Y-%m-%d')}")
            md_content.append(f"* **Link:** {paper.entry_id}")
            md_content.append(f"* **Abstract:** {paper.summary.replace(chr(10), ' ').strip()}\n")
    
    try:
        with open(TODAY_MD_FILE, 'w', encoding='utf-8') as f:
            f.write("\n".join(md_content))
        logging.info(f"Successfully wrote to {TODAY_MD_FILE}")
    except IOError as e:
        logging.error(f"Failed to write to {TODAY_MD_FILE}: {e}")

def update_readme():
    """
    Updates the README.md with the content from papers_today.md.
    """
    logging.info("Attempting to update README.md...")
    
    # 1. Read the new content from the daily markdown file
    try:
        with open(TODAY_MD_FILE, 'r', encoding='utf-8') as f:
            papers_content = f.read()
    except IOError as e:
        logging.error(f"Could not read {TODAY_MD_FILE} to update README: {e}")
        return

    # 2. Read the current README content
    try:
        with open(README_FILE, 'r', encoding='utf-8') as f:
            readme_content = f.read()
    except IOError as e:
        logging.error(f"Could not read {README_FILE} to update it: {e}")
        return

    # 3. Define the placeholder tags
    start_tag = "<!-- LATEST_PAPERS_START -->"
    end_tag = "<!-- LATEST_PAPERS_END -->"
    
    # 4. Use regex to find and replace content
    # re.DOTALL makes '.' match newline characters, which is crucial
    pattern = re.compile(f"{re.escape(start_tag)}.*{re.escape(end_tag)}", re.DOTALL)
    
    # 5. *** THE FIX ***
    # We must escape all backslashes in the paper content.
    # Otherwise, re.subn will try to parse them as back-references (e.g., \g, \1)
    # and fail if the abstract contains scientific notation.
    safe_papers_content = papers_content.replace('\\', '\\\\')
    
    # We add newlines for nice formatting in the markdown
    replacement_text = f"{start_tag}\n\n{safe_papers_content}\n{end_tag}"
    
    # 6. Substitute the content
    new_readme_content, sub_count = re.subn(pattern, replacement_text, readme_content)
    
    if sub_count == 0:
        logging.warning(f"Could not find placeholder tags in {README_FILE}. Skipping README update.")
        return

    # 7. Write the updated content back to the README
    try:
        with open(README_FILE, 'w', encoding='utf-8') as f:
            f.write(new_readme_content)
        logging.info("Successfully updated README.md.")
    except IOError as e:
        logging.error(f"Could not write updated content to {README_FILE}: {e}")

def update_archive(new_papers):
    """Appends new papers to the data/archive.json file."""
    if not new_papers:
        logging.info("No new papers to add to archive.")
        return

    # Load the old archive first
    archive_list = []
    if ARCHIVE_JSON_FILE.exists():
        try:
            with open(ARCHIVE_JSON_FILE, 'r', encoding='utf-8') as f:
                archive_list = json.load(f)
        except json.JSONDecodeError:
            logging.warning(f"Could not read {ARCHIVE_JSON_FILE}. Will create a new one.")
            archive_list = []

    # Add new papers
    for paper in new_papers:
        archive_list.append({
            "id": paper.entry_id,
            "title": paper.title,
            "authors": [str(a) for a in paper.authors],
            "summary": paper.summary,
            "published": paper.published.isoformat(), # v1 date
            "updated": paper.updated.isoformat(), # Last revision date
            "link": paper.entry_id,
            "pdf_link": paper.pdf_url,
            "categories": paper.categories
        })
    
    # Write the entire updated list back to the file
    try:
        with open(ARCHIVE_JSON_FILE, 'w', encoding='utf-8') as f:
            json.dump(archive_list, f, indent=2, ensure_ascii=False)
        logging.info(f"Successfully updated {ARCHIVE_JSON_FILE} with {len(new_papers)} new entries.")
    except IOError as e:
        logging.error(f"Failed to write to {ARCHIVE_JSON_FILE}: {e}")

def main():
    """Main execution function for the scraper."""
    logging.info("--- Starting arXiv Scraper Script ---")
    try:
        # 1. Load Config
        keywords, max_results = load_config()
        
        # 2. Load Archive to get seen paper IDs
        seen_ids = load_archive()
        logging.info(f"Loaded {len(seen_ids)} seen paper IDs from archive.")
        
        # 3. Build Query
        query = build_query(keywords)
        
        # 4. Fetch Papers
        all_results = fetch_papers(query, max_results)
        
        # 5. Filter for new papers
        new_papers = filter_new_papers(all_results, seen_ids)
        
        # 6. Write new papers to daily markdown
        write_daily_markdown(new_papers)
        
        # 7. Update the JSON archive
        update_archive(new_papers)

        # 8. Update the README.md
        update_readme()
        
        logging.info("--- Scraper script finished successfully ---")

    except FileNotFoundError as e:
        logging.error(f"CRITICAL ERROR: Config file not found. {e}")
        sys.exit(1) # Exit with an error code for GitHub Actions
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}", exc_info=True)
        sys.exit(1) # Exit with an error code

if __name__ == "__main__":
    main()