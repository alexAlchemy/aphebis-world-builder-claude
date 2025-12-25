"""
Get activity logs with optional filtering.

Usage:
    python get_activity_logs.py [--project-id <id>] [--days <n>] [--hours <n>] [--agent-name <agent>]
"""

import sys
import os
import argparse
import json
from datetime import datetime, timedelta

# Add the scripts directory to the path
sys.path.insert(0, os.path.dirname(__file__))
from pso_utils import (
    ensure_directories, read_activity_logs, parse_datetime
)


def get_activity_logs(project_id: str = None, days_ago: int = None,
                     hours_ago: int = None) -> list:
    """
    Get activity logs with optional filtering.

    Args:
        project_id: Filter by project ID (optional)
        days_ago: Only include logs from N days ago (default: 7)
        hours_ago: Only include logs from N hours ago (overrides days_ago)

    Returns:
        List of activity log entries
    """
    ensure_directories()
    logs = read_activity_logs()

    # Default to 7 days if no time filter specified
    if days_ago is None and hours_ago is None:
        days_ago = 7

    # Calculate cutoff time
    if hours_ago is not None:
        cutoff = datetime.now() - timedelta(hours=hours_ago)
    elif days_ago is not None:
        cutoff = datetime.now() - timedelta(days=days_ago)
    else:
        cutoff = None

    # Filter logs
    filtered = []
    for log in logs:
        # Filter by project ID
        if project_id and log['projectId'] != project_id:
            continue

        # Filter by time
        if cutoff:
            try:
                log_time = parse_datetime(log['datetime'])
                if log_time < cutoff:
                    continue
            except:
                pass

        filtered.append(log)

    # Sort by datetime descending (newest first)
    filtered.sort(key=lambda x: x['datetime'], reverse=True)

    return filtered


def main():
    parser = argparse.ArgumentParser(description='Get activity logs')
    parser.add_argument('--project-id', help='Filter by project ID')
    parser.add_argument('--days', type=int, default=None,
                       help='Only include logs from N days ago (default: 7)')
    parser.add_argument('--hours', type=int, default=None,
                       help='Only include logs from N hours ago (overrides days)')
    parser.add_argument('--agent-name', default='unknown',
                       help='Name/role of the agent making the request')
    args = parser.parse_args()

    result = get_activity_logs(
        project_id=args.project_id,
        days_ago=args.days,
        hours_ago=args.hours
    )

    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
