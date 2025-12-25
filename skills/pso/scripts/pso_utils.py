"""
Utility functions for the Project Support Officer skill.
"""

import os
import re
import csv
import random
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional, List, Dict, Any


# Configuration
ORG_DIR = "org"
PROJECTS_DIR = os.path.join(ORG_DIR, "projects")
PROJECT_LIST_CSV = os.path.join(PROJECTS_DIR, "project-list.csv")
ACTIVITY_LOGS_CSV = os.path.join(PROJECTS_DIR, "project-activity-logs.csv")


def generate_short_id(length: int = 6) -> str:
    """Generate a short ID using alphanumeric characters."""
    characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    return ''.join(random.choices(characters, k=length))


def sanitize_name(name: str) -> str:
    """Sanitize a project name for use in folder names."""
    # Convert to lowercase
    name = name.lower()
    # Replace spaces and special chars with hyphens
    name = re.sub(r'[^\w\s-]', '', name)
    name = re.sub(r'[\s_]+', '-', name)
    # Remove leading/trailing hyphens
    name = name.strip('-')
    # Limit length
    return name[:50]


def ensure_directories() -> None:
    """Ensure required directories and files exist."""
    os.makedirs(PROJECTS_DIR, exist_ok=True)

    # Create project-list.csv if it doesn't exist
    if not os.path.exists(PROJECT_LIST_CSV):
        with open(PROJECT_LIST_CSV, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['projectId', 'projectName', 'description', 'startDate', 'endDate'])

    # Create project-activity-logs.csv if it doesn't exist
    if not os.path.exists(ACTIVITY_LOGS_CSV):
        with open(ACTIVITY_LOGS_CSV, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['projectId', 'datetime', 'agentName', 'note'])


def read_projects() -> List[Dict[str, str]]:
    """Read all projects from project-list.csv."""
    ensure_directories()
    projects = []

    if not os.path.exists(PROJECT_LIST_CSV):
        return projects

    with open(PROJECT_LIST_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            projects.append(row)

    return projects


def write_projects(projects: List[Dict[str, str]]) -> None:
    """Write all projects to project-list.csv."""
    ensure_directories()

    with open(PROJECT_LIST_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['projectId', 'projectName', 'description', 'startDate', 'endDate'])
        writer.writeheader()
        writer.writerows(projects)


def read_activity_logs() -> List[Dict[str, str]]:
    """Read all activity logs."""
    ensure_directories()
    logs = []

    if not os.path.exists(ACTIVITY_LOGS_CSV):
        return logs

    with open(ACTIVITY_LOGS_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            logs.append(row)

    return logs


def write_activity_logs(logs: List[Dict[str, str]]) -> None:
    """Write all activity logs."""
    ensure_directories()

    with open(ACTIVITY_LOGS_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['projectId', 'datetime', 'agentName', 'note'])
        writer.writeheader()
        writer.writerows(logs)


def get_project_folder(project_id: str, project_name: str) -> str:
    """Get the folder path for a project's artifacts."""
    sanitized = sanitize_name(project_name)
    return os.path.join(PROJECTS_DIR, f"{project_id}-{sanitized}")


def is_project_manager(agent_name: str) -> bool:
    """Check if an agent is a project manager."""
    # Check for exact match or role indicator
    name_lower = agent_name.lower().strip()
    return (
        name_lower == "project manager" or
        name_lower.startswith("project manager:") or
        name_lower.endswith("(project manager)") or
        name_lower.endswith("[pm]") or
        "project manager" in name_lower
    )


def format_datetime(dt: Optional[datetime] = None) -> str:
    """Format a datetime as ISO string."""
    if dt is None:
        dt = datetime.now()
    return dt.isoformat()


def parse_datetime(dt_str: str) -> datetime:
    """Parse an ISO datetime string."""
    # Handle various ISO formats
    dt_str = dt_str.replace('Z', '+00:00')
    try:
        return datetime.fromisoformat(dt_str)
    except ValueError:
        # Try parsing without timezone
        return datetime.fromisoformat(dt_str.split('+')[0].split('.')[0])
