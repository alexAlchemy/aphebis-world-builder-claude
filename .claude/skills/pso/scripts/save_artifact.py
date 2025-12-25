"""
Save an artifact to a project folder.

Usage:
    python save_artifact.py <project_id> <source_path> <artifact_name> [--agent-name <agent>]
"""

import sys
import os
import argparse
import json
import shutil

# Add the scripts directory to the path
sys.path.insert(0, os.path.dirname(__file__))
from pso_utils import (
    ensure_directories, read_projects, get_project_folder,
    sanitize_name, format_datetime
)


def save_artifact(project_id: str, source_path: str,
                 artifact_name: str, agent_name: str) -> dict:
    """
    Save an artifact to a project folder.

    Args:
        project_id: The project ID
        source_path: Path to the source file
        artifact_name: Name for the artifact (will be sanitized)
        agent_name: Name/role of the agent saving the artifact

    Returns:
        dict with artifact path and metadata
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

    # Get project folder
    project_folder = get_project_folder(project_id, project['projectName'])

    # Sanitize artifact name
    safe_name = sanitize_name(artifact_name)
    # Preserve extension
    if '.' in artifact_name:
        ext = artifact_name.rsplit('.', 1)[-1]
        safe_name = f"{safe_name.rsplit('.', 1)[0] if '.' in safe_name else safe_name}.{ext}"

    dest_path = os.path.join(project_folder, safe_name)

    # Copy the file
    shutil.copy2(source_path, dest_path)

    # Record the activity
    from pso_utils import read_activity_logs, write_activity_logs
    logs = read_activity_logs()
    logs.append({
        'projectId': project_id,
        'datetime': format_datetime(),
        'agentName': agent_name,
        'note': f"Saved artifact: {safe_name}"
    })
    write_activity_logs(logs)

    return {
        'projectId': project_id,
        'artifactName': safe_name,
        'path': dest_path,
        'savedBy': agent_name,
        'savedAt': format_datetime()
    }


def main():
    parser = argparse.ArgumentParser(description='Save an artifact to a project')
    parser.add_argument('project_id', help='Project ID')
    parser.add_argument('source_path', help='Path to the source file')
    parser.add_argument('artifact_name', help='Name for the artifact')
    parser.add_argument('--agent-name', default='unknown',
                       help='Name/role of the agent saving the artifact')
    args = parser.parse_args()

    try:
        result = save_artifact(args.project_id, args.source_path,
                             args.artifact_name, args.agent_name)
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
