"""
Update project information (name, description).

Usage:
    python update_project.py <project_id> [--name <new_name>] [--description <new_desc>] [--agent-name <agent>]
"""

import sys
import os
import argparse
import json

# Add the scripts directory to the path
sys.path.insert(0, os.path.dirname(__file__))
from pso_utils import (
    ensure_directories, read_projects, write_projects,
    format_datetime
)


def update_project(project_id: str, agent_name: str,
                  name: str = None, description: str = None) -> dict:
    """
    Update project name or description.

    Args:
        project_id: The project ID
        agent_name: Name/role of the agent making the update
        name: New project name (optional)
        description: New description (optional)

    Returns:
        Updated project dictionary
    """
    ensure_directories()
    projects = read_projects()

    project = None
    for i, p in enumerate(projects):
        if p['projectId'] == project_id:
            project = p
            break

    if not project:
        raise ValueError(f"Project '{project_id}' not found")

    # Track changes
    changes = []

    if name:
        old_name = project['projectName']
        project['projectName'] = name
        changes.append(f"name: '{old_name}' -> '{name}'")

    if description:
        old_desc = project['description']
        project['description'] = description
        changes.append(f"description updated")

    if not changes:
        return project

    # Save changes
    write_projects(projects)

    # Record activity
    from pso_utils import read_activity_logs, write_activity_logs
    logs = read_activity_logs()
    logs.append({
        'projectId': project_id,
        'datetime': format_datetime(),
        'agentName': agent_name,
        'note': f"Updated project: {', '.join(changes)}"
    })
    write_activity_logs(logs)

    return project


def main():
    parser = argparse.ArgumentParser(description='Update project information')
    parser.add_argument('project_id', help='Project ID')
    parser.add_argument('--name', help='New project name')
    parser.add_argument('--description', help='New description')
    parser.add_argument('--agent-name', default='unknown',
                       help='Name/role of the agent making the update')
    args = parser.parse_args()

    if not args.name and not args.description:
        print("Error: Must provide at least --name or --description", file=sys.stderr)
        sys.exit(1)

    try:
        result = update_project(args.project_id, args.agent_name,
                               name=args.name, description=args.description)
        print(json.dumps(result, indent=2))
    except ValueError as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
