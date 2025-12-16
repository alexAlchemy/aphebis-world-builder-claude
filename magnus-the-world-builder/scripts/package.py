#!/usr/bin/env python3
"""
Simple packaging script for the magnus-the-world-builder skill
Creates a .skill file (zip archive) with proper directory structure
"""

import zipfile
import os
import sys
from pathlib import Path

def create_skill_package(skill_dir, output_dir=None):
    """Package the skill into a .skill file"""
    skill_path = Path(skill_dir)
    skill_name = skill_path.name

    if output_dir is None:
        output_path = skill_path.parent / f"{skill_name}.skill"
    else:
        output_path = Path(output_dir) / f"{skill_name}.skill"

    # Validate required files
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        print(f"Error: SKILL.md not found in {skill_path}")
        return False

    # Validate YAML frontmatter
    with open(skill_md, 'r', encoding='utf-8') as f:
        content = f.read()
        if not content.startswith('---'):
            print("Error: SKILL.md must start with YAML frontmatter")
            return False

    # Create zip archive
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file_path in skill_path.rglob('*'):
            if file_path.is_file() and file_path.name != 'package.py':
                # Calculate relative path for archive
                arcname = file_path.relative_to(skill_path.parent)
                zipf.write(file_path, arcname)

    print(f"Skill packaged successfully: {output_path}")
    return True

if __name__ == "__main__":
    skill_dir = "."
    if len(sys.argv) > 1:
        skill_dir = sys.argv[1]

    output_dir = None
    if len(sys.argv) > 2:
        output_dir = sys.argv[2]

    create_skill_package(skill_dir, output_dir)