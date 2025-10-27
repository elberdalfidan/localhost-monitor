"""Port scanning functionality using lsof."""

import subprocess
import re
from typing import List, Dict, Optional

from . import config


def scan_ports(start_port: int, end_port: int) -> List[Dict[str, any]]:
    """
    Scan for processes listening on localhost ports in the given range.

    Args:
        start_port: Starting port number
        end_port: Ending port number

    Returns:
        List of dictionaries with port, pid, and process name
        Example: [{'port': 3000, 'pid': 12345, 'name': 'node'}]
    """
    processes = []

    try:
        # Run lsof to find listening TCP connections
        # -i TCP - only TCP connections
        # -sTCP:LISTEN - only listening sockets
        # -n - no hostname resolution (faster)
        # -P - no port name resolution (show numbers)
        cmd = ["lsof", "-i", "TCP", "-sTCP:LISTEN", "-n", "-P"]

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=5
        )

        if result.returncode != 0:
            # lsof returns 1 if no files found, which is ok
            if result.returncode == 1:
                return processes
            return processes

        # Parse lsof output
        lines = result.stdout.strip().split('\n')

        # Skip header line
        for line in lines[1:]:
            parts = line.split()
            if len(parts) < 9:
                continue

            process_name = parts[0]
            pid = int(parts[1])

            # The network info is usually in format like: *:3000 or localhost:3000 or 127.0.0.1:3000
            network_info = parts[8]

            # Extract port number
            port_match = re.search(r':(\d+)', network_info)
            if not port_match:
                continue

            port = int(port_match.group(1))

            # Filter by port range
            if start_port <= port <= end_port:
                # Check if already in list (sometimes lsof shows same process multiple times)
                if not any(p['port'] == port and p['pid'] == pid for p in processes):
                    processes.append({
                        'port': port,
                        'pid': pid,
                        'name': process_name
                    })

    except subprocess.TimeoutExpired:
        print("lsof command timed out")
    except FileNotFoundError:
        print("lsof command not found")
    except Exception as e:
        print(f"Error scanning ports: {e}")

    # Apply filtering
    if config.FILTER_MODE != "off":
        processes = filter_processes(processes)

    # Sort by port number
    processes.sort(key=lambda x: x['port'])

    return processes


def filter_processes(processes: List[Dict[str, any]]) -> List[Dict[str, any]]:
    """
    Filter processes based on configuration settings.

    Args:
        processes: List of process dictionaries

    Returns:
        Filtered list of processes
    """
    if config.FILTER_MODE == "off":
        return processes

    filtered = []

    for proc in processes:
        process_name_lower = proc['name'].lower()

        if config.FILTER_MODE == "whitelist":
            # Only include if in whitelist
            if any(dev_tool.lower() in process_name_lower
                   for dev_tool in config.DEV_PROCESS_WHITELIST):
                filtered.append(proc)

        elif config.FILTER_MODE == "blacklist":
            # Include unless in blacklist
            if not any(sys_app.lower() in process_name_lower
                      for sys_app in config.SYSTEM_PROCESS_BLACKLIST):
                filtered.append(proc)

    return filtered


def get_process_by_port(port: int) -> Optional[Dict[str, any]]:
    """
    Get process information for a specific port.

    Args:
        port: Port number to check

    Returns:
        Dictionary with process info or None if not found
    """
    try:
        cmd = ["lsof", "-i", f"TCP:{port}", "-sTCP:LISTEN", "-n", "-P"]

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=5
        )

        if result.returncode != 0:
            return None

        lines = result.stdout.strip().split('\n')
        if len(lines) < 2:
            return None

        # Parse first matching line
        parts = lines[1].split()
        if len(parts) < 9:
            return None

        return {
            'port': port,
            'pid': int(parts[1]),
            'name': parts[0]
        }

    except Exception as e:
        print(f"Error getting process for port {port}: {e}")
        return None
