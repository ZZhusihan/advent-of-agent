#!/usr/bin/env python3
"""
Script to create a new day's notes file for Advent of Agents
Usage: python make-day.py <day_number>
Example: python make-day.py 3
"""

import sys
import os
import re
from pathlib import Path


def create_day_notes(day_num):
    """Create a new day's notes file and update README."""

    # Validate day number
    if not (1 <= day_num <= 25):
        print(f"Error: Day number must be between 1 and 25")
        sys.exit(1)

    # Format day number with zero padding
    day_padded = f"{day_num:02d}"
    notes_file = Path(f"notes/day-{day_padded}.md")

    # Check if file already exists
    if notes_file.exists():
        response = input(f"Warning: {notes_file} already exists! Overwrite? (y/N): ")
        if response.lower() != 'y':
            print("Aborted.")
            sys.exit(1)

    # Read template
    template_file = Path("notes/template.md")
    if not template_file.exists():
        print(f"Error: Template file {template_file} not found!")
        sys.exit(1)

    template_content = template_file.read_text()

    # Replace placeholders
    content = template_content.replace("XX", day_padded)
    content = content.replace(f"Day {day_padded}", f"Day {day_padded}")

    # Write the notes file
    notes_file.write_text(content)
    print(f"Created {notes_file}")

    # Update README
    readme_file = Path("README.md")
    if not readme_file.exists():
        print(f"Warning: {readme_file} not found, skipping README update")
        return

    readme_content = readme_file.read_text()

    # Check if day is already in README
    if f"[Day {day_padded}]" in readme_content:
        print(f"Day {day_padded} is already in the README index.")
    else:
        # Find the Daily Notes section and add the new day
        pattern = r'(## Daily Notes\n\n)((?:- \[Day \d+\]\(notes/day-\d+\.md\)\n?)+)'

        def add_day_to_list(match):
            header = match.group(1)
            existing_days = match.group(2)

            # Extract all existing days
            day_pattern = r'- \[Day (\d+)\]\(notes/day-(\d+)\.md\)'
            days = []
            for m in re.finditer(day_pattern, existing_days):
                days.append((int(m.group(1)), m.group(2)))

            # Add new day
            days.append((day_num, day_padded))

            # Sort by day number
            days.sort(key=lambda x: x[0])

            # Rebuild the list
            day_list = ""
            for d_num, d_padded in days:
                day_list += f"- [Day {d_padded}](notes/day-{d_padded}.md)\n"

            return header + day_list

        updated_content = re.sub(pattern, add_day_to_list, readme_content)

        if updated_content != readme_content:
            readme_file.write_text(updated_content)
            print(f"Updated README.md to include Day {day_padded} in the index.")
        else:
            print("Warning: Could not find 'Daily Notes' section in README.md")

    print(f"Done! You can now edit {notes_file}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python make-day.py <day_number>")
        print("Example: python make-day.py 3")
        sys.exit(1)

    try:
        day_num = int(sys.argv[1])
    except ValueError:
        print(f"Error: '{sys.argv[1]}' is not a valid number")
        sys.exit(1)

    create_day_notes(day_num)


if __name__ == "__main__":
    main()
