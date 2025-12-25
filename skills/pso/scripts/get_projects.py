"""
Get projects from the project list.

Usage:
    python get_projects.py [--active-only] [--agent-name <agent>]
"""

import sys
import os
import argparse
import json

# Add the scripts directory to the path
sys.path.insert(0, os.path.dirname(__file__))
from pso_utils import ensure_directories, read_projects


def get_projects(active_only: bool = False) -> list:
    """
    Get all projects or only active projects.

    Args:
        active_only: If True, only return projects without an endDate

    Returns:
        List of project dictionaries
    """
    ensure_directories()
    projects = read_projects()

    if active_only:
        projects = [p for p in projects if not p.get('endDate') or p['endDate'] == '']

    return projects


def main():
    parser = argparse.ArgumentParser(description='Get projects')
    parser.add_argument('--active-only', action='store_true',
                       help='Only return active projects (no endDate)')
    parser.add_argument('--agent-name', default='unknown',
                       help='Name/role of the agent making the request')
    args = parser.parse_args()

    result = get_projects(active_only=args.active_only)

    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
