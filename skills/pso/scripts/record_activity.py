"""
Record an activity for a project.

Usage:
    python record_activity.py <project_id> <agent_name> <note>
"""

import sys
import os
import argparse
import json

# Add the scripts directory to the path
sys.path.insert(0, os.path.dirname(__file__))
from pso_utils import (
    ensure_directories, read_projects, read_activity_logs,
    write_activity_logs, format_datetime
)


def record_activity(project_id: str, agent_name: str, note: str) -> dict:
    """
    Record an activity for a project.

    Args:
        project_id: The project ID
        agent_name: Name/role of the agent recording the activity
        note: Activity note/description

    Returns:
        The recorded activity entry
    """
    ensure_directories()

    # Verify project exists
    projects = read_projects()
    project = None
    for p in projects:
        if p['projectId'] == project_id:
            project = p
            break

    if not project:
        raise ValueError(f"Project '{project_id}' not found")

    # Create activity log entry
    activity = {
        'projectId': project_id,
        'datetime': format_datetime(),
        'agentName': agent_name,
        'note': note
    }

    logs = read_activity_logs()
    logs.append(activity)
    write_activity_logs(logs)

    return activity


def main():
    parser = argparse.ArgumentParser(description='Record project activity')
    parser.add_argument('project_id', help='Project ID')
    parser.add_argument('agent_name', help='Name/role of the agent')
    parser.add_argument('note', help='Activity note')
    args = parser.parse_args()

    try:
        result = record_activity(args.project_id, args.agent_name, args.note)
        print(json.dumps(result, indent=2))
    except ValueError as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
