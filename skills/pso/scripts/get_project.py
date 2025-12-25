"""
Get a specific project by ID.

Usage:
    python get_project.py <project_id> [--agent-name <agent>]
"""

import sys
import os
import argparse
import json

# Add the scripts directory to the path
sys.path.insert(0, os.path.dirname(__file__))
from pso_utils import ensure_directories, read_projects


def get_project(project_id: str) -> dict:
    """
    Get a specific project by ID.

    Args:
        project_id: The project ID to look up

    Returns:
        Project dictionary or None if not found
    """
    ensure_directories()
    projects = read_projects()

    for project in projects:
        if project['projectId'] == project_id:
            return project

    return None


def main():
    parser = argparse.ArgumentParser(description='Get a specific project')
    parser.add_argument('project_id', help='Project ID to look up')
    parser.add_argument('--agent-name', default='unknown',
                       help='Name/role of the agent making the request')
    args = parser.parse_args()

    result = get_project(args.project_id)

    if result:
        print(json.dumps(result, indent=2))
    else:
        print(f"Project '{args.project_id}' not found", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
