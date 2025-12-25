"""
List artifacts in a project folder.

Usage:
    python get_artifacts.py <project_id> [--agent-name <agent>]
"""

import sys
import os
import argparse
import json

# Add the scripts directory to the path
sys.path.insert(0, os.path.dirname(__file__))
from pso_utils import (
    ensure_directories, read_projects, get_project_folder
)


def get_artifacts(project_id: str) -> list:
    """
    List all artifacts in a project folder.

    Args:
        project_id: The project ID

    Returns:
        List of artifact metadata (name, path, size, type)
    """
    ensure_directories()

    # Verify project exists and get its name
    projects = read_projects()
    project = None
    for p in projects:
        if p['projectId'] == project_id:
            project = p
            break

    if not project:
        raise ValueError(f"Project '{project_id}' not found")

    project_folder = get_project_folder(project_id, project['projectName'])

    if not os.path.exists(project_folder):
        return []

    artifacts = []
    for item in os.listdir(project_folder):
        item_path = os.path.join(project_folder, item)
        if os.path.isfile(item_path):
            stat = os.stat(item_path)
            artifacts.append({
                'name': item,
                'path': item_path,
                'sizeBytes': stat.st_size,
                'type': item.rsplit('.', 1)[-1].lower() if '.' in item else 'unknown'
            })

    return artifacts


def main():
    parser = argparse.ArgumentParser(description='List project artifacts')
    parser.add_argument('project_id', help='Project ID')
    parser.add_argument('--agent-name', default='unknown',
                       help='Name/role of the agent making the request')
    args = parser.parse_args()

    try:
        result = get_artifacts(args.project_id)
        print(json.dumps(result, indent=2))
    except ValueError as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
