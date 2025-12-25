"""
Close a project (only available to project managers).

Usage:
    python close_project.py <project_id> <agent_name>
"""

import sys
import os
import argparse
import json

# Add the scripts directory to the path
sys.path.insert(0, os.path.dirname(__file__))
from pso_utils import (
    ensure_directories, read_projects, write_projects,
    is_project_manager, format_datetime
)


def close_project(project_id: str, agent_name: str) -> dict:
    """
    Close a project by setting its endDate.
    Only project managers can close projects.

    Args:
        project_id: The project ID to close
        agent_name: Name/role of the agent requesting the closure

    Returns:
        Updated project dictionary

    Raises:
        PermissionError: If the agent is not a project manager
        ValueError: If the project doesn't exist or is already closed
    """
    # Verify the agent is a project manager
    if not is_project_manager(agent_name):
        raise PermissionError(
            f"Only project managers can close projects. "
            f"Agent '{agent_name}' is not authorized."
        )

    ensure_directories()
    projects = read_projects()

    project = None
    for i, p in enumerate(projects):
        if p['projectId'] == project_id:
            project = p
            break

    if not project:
        raise ValueError(f"Project '{project_id}' not found")

    # Check if already closed
    if project.get('endDate') and project['endDate'] != '':
        raise ValueError(f"Project '{project_id}' is already closed")

    # Close the project
    project['endDate'] = format_datetime()
    write_projects(projects)

    # Record the activity
    from pso_utils import read_activity_logs, write_activity_logs
    logs = read_activity_logs()
    logs.append({
        'projectId': project_id,
        'datetime': format_datetime(),
        'agentName': agent_name,
        'note': f"Project closed by {agent_name}"
    })
    write_activity_logs(logs)

    return project


def main():
    parser = argparse.ArgumentParser(description='Close a project')
    parser.add_argument('project_id', help='Project ID to close')
    parser.add_argument('agent_name', help='Name/role of the agent (must be project manager)')
    args = parser.parse_args()

    try:
        result = close_project(args.project_id, args.agent_name)
        print(json.dumps(result, indent=2))
    except PermissionError as e:
        print(f"Permission denied: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
