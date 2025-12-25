"""
Create a new project.

Usage:
    python create_project.py <project_name> <description> [--agent-name <agent>]

Returns the new project ID.
"""

import sys
import os
import argparse

# Add the scripts directory to the path to import pso_utils
sys.path.insert(0, os.path.dirname(__file__))
from pso_utils import (
    ensure_directories, read_projects, write_projects,
    generate_short_id, get_project_folder, format_datetime
)


def create_project(name: str, description: str, agent_name: str) -> dict:
    """
    Create a new project.

    Args:
        name: The project name
        description: Project description
        agent_name: Name/role of the agent creating the project

    Returns:
        dict with projectId, projectName, description, startDate, endDate (null)
    """
    ensure_directories()
    projects = read_projects()

    # Generate a unique project ID
    while True:
        project_id = generate_short_id(6)
        existing = [p for p in projects if p['projectId'] == project_id]
        if not existing:
            break

    # Create project record
    start_date = format_datetime()
    new_project = {
        'projectId': project_id,
        'projectName': name,
        'description': description,
        'startDate': start_date,
        'endDate': ''  # Empty means active
    }

    projects.append(new_project)
    write_projects(projects)

    # Create project folder for artifacts
    project_folder = get_project_folder(project_id, name)
    os.makedirs(project_folder, exist_ok=True)

    # Record the activity
    record_project_activity(project_id, agent_name,
                           f"Created project: {name} - {description}")

    return new_project


def record_project_activity(project_id: str, agent_name: str, note: str) -> None:
    """Record an activity for a project."""
    from pso_utils import read_activity_logs, write_activity_logs, format_datetime

    logs = read_activity_logs()
    logs.append({
        'projectId': project_id,
        'datetime': format_datetime(),
        'agentName': agent_name,
        'note': note
    })
    write_activity_logs(logs)


def main():
    parser = argparse.ArgumentParser(description='Create a new project')
    parser.add_argument('name', help='Project name')
    parser.add_argument('description', help='Project description')
    parser.add_argument('--agent-name', default='unknown',
                       help='Name/role of the agent creating the project')
    args = parser.parse_args()

    result = create_project(args.name, args.description, args.agent_name)

    # Output as JSON for easy parsing
    import json
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
