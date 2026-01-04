#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Archive Management Script

This script allows you to clear old papers from the archive.json file.
Useful if you want to start fresh or remove papers older than a certain date.
"""

import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

# Setup paths
ROOT_DIR = Path(__file__).parent.parent.resolve()
ARCHIVE_JSON_FILE = ROOT_DIR / 'data' / 'archive.json'

def clear_archive():
    """Clears all papers from the archive."""
    if not ARCHIVE_JSON_FILE.exists():
        print(f"Archive file not found at {ARCHIVE_JSON_FILE}")
        return
    
    # Backup first
    backup_file = ARCHIVE_JSON_FILE.with_suffix('.json.backup')
    with open(ARCHIVE_JSON_FILE, 'r') as f:
        archive = json.load(f)
    
    with open(backup_file, 'w') as f:
        json.dump(archive, f, indent=2)
    print(f"Backup created at {backup_file}")
    
    # Clear archive
    with open(ARCHIVE_JSON_FILE, 'w') as f:
        json.dump([], f, indent=2)
    
    print(f"Cleared {len(archive)} papers from archive.")
    print(f"Archive is now empty. Backup saved to {backup_file}")

def clear_old_papers(days=30):
    """Removes papers older than specified number of days."""
    if not ARCHIVE_JSON_FILE.exists():
        print(f"Archive file not found at {ARCHIVE_JSON_FILE}")
        return
    
    threshold = datetime.now(timezone.utc) - timedelta(days=days)
    
    with open(ARCHIVE_JSON_FILE, 'r') as f:
        archive = json.load(f)
    
    original_count = len(archive)
    
    # Filter out old papers
    filtered_archive = []
    removed_count = 0
    for paper in archive:
        try:
            updated_date = datetime.fromisoformat(paper['updated'].replace('Z', '+00:00'))
            if updated_date > threshold:
                filtered_archive.append(paper)
            else:
                removed_count += 1
        except (KeyError, ValueError) as e:
            print(f"Warning: Could not parse date for paper {paper.get('id', 'unknown')}: {e}")
            # Keep papers with unparseable dates
            filtered_archive.append(paper)
    
    # Backup first
    backup_file = ARCHIVE_JSON_FILE.with_suffix('.json.backup')
    with open(backup_file, 'w') as f:
        json.dump(archive, f, indent=2)
    print(f"Backup created at {backup_file}")
    
    # Write filtered archive
    with open(ARCHIVE_JSON_FILE, 'w') as f:
        json.dump(filtered_archive, f, indent=2, ensure_ascii=False)
    
    print(f"Removed {removed_count} papers older than {days} days.")
    print(f"Archive now contains {len(filtered_archive)} papers (was {original_count}).")
    print(f"Backup saved to {backup_file}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "clear":
            clear_archive()
        elif sys.argv[1] == "clean" and len(sys.argv) > 2:
            try:
                days = int(sys.argv[2])
                clear_old_papers(days)
            except ValueError:
                print("Error: Days must be a number")
                print("Usage: python scripts/clear_archive.py clean <days>")
        else:
            print("Usage:")
            print("  python scripts/clear_archive.py clear          # Clear all papers")
            print("  python scripts/clear_archive.py clean <days>  # Remove papers older than <days> days")
    else:
        print("Archive Management Script")
        print("Usage:")
        print("  python scripts/clear_archive.py clear          # Clear all papers")
        print("  python scripts/clear_archive.py clean <days>  # Remove papers older than <days> days")
        print("\nExample: python scripts/clear_archive.py clean 60  # Remove papers older than 60 days")

