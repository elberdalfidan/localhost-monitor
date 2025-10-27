"""Process monitoring functionality using psutil."""

import psutil
import time
import signal
import os
from typing import Dict, Optional

from . import config

# Cache for process objects to maintain CPU measurement state
_process_cache: Dict[int, psutil.Process] = {}


def get_process_info(pid: int) -> Optional[Dict[str, any]]:
    """
    Get detailed information about a process.

    Args:
        pid: Process ID

    Returns:
        Dictionary with process information or None if process not found
        Example: {
            'pid': 12345,
            'name': 'node',
            'memory_mb': 245.6,
            'cpu_percent': 12.5,
            'uptime_seconds': 8456,
            'uptime_formatted': '2h 20m'
        }
    """
    try:
        # Use cached process object if available for accurate CPU measurement
        if pid in _process_cache:
            process = _process_cache[pid]
            # Verify process is still the same (not reused PID)
            if not process.is_running():
                del _process_cache[pid]
                process = psutil.Process(pid)
                _process_cache[pid] = process
        else:
            process = psutil.Process(pid)
            _process_cache[pid] = process

        # Get memory info (in bytes, convert to MB)
        memory_info = process.memory_info()
        memory_mb = memory_info.rss / (1024 * 1024)

        # Get CPU percent with longer interval for more accurate measurement
        # Using cached process object, subsequent calls return actual usage
        # First call initializes the measurement, returns 0.0
        # Subsequent calls return actual CPU usage since last call
        cpu_percent = process.cpu_percent(interval=config.CPU_MEASUREMENT_INTERVAL)

        # Get uptime
        create_time = process.create_time()
        uptime_seconds = int(time.time() - create_time)
        uptime_formatted = format_uptime(uptime_seconds)

        # Get process name
        name = process.name()

        return {
            'pid': pid,
            'name': name,
            'memory_mb': round(memory_mb, 1),
            'cpu_percent': round(cpu_percent, 1),
            'uptime_seconds': uptime_seconds,
            'uptime_formatted': uptime_formatted
        }

    except psutil.NoSuchProcess:
        # Clean up cache if process no longer exists
        if pid in _process_cache:
            del _process_cache[pid]
        return None
    except psutil.AccessDenied:
        # Sometimes we can't access process info
        return None
    except Exception as e:
        print(f"Error getting process info for PID {pid}: {e}")
        return None


def clear_process_cache():
    """Clear the process cache. Useful for testing or cleanup."""
    global _process_cache
    _process_cache.clear()


def format_uptime(seconds: int) -> str:
    """
    Format uptime in human-readable format.

    Args:
        seconds: Uptime in seconds

    Returns:
        Formatted string like '2h 20m' or '45m' or '30s'
    """
    if seconds < 60:
        return f"{seconds}s"

    minutes = seconds // 60
    if minutes < 60:
        return f"{minutes}m"

    hours = minutes // 60
    remaining_minutes = minutes % 60

    if hours < 24:
        if remaining_minutes > 0:
            return f"{hours}h {remaining_minutes}m"
        return f"{hours}h"

    days = hours // 24
    remaining_hours = hours % 24

    if remaining_hours > 0:
        return f"{days}d {remaining_hours}h"
    return f"{days}d"


def kill_process(pid: int, force: bool = False) -> bool:
    """
    Kill a process by PID.

    Args:
        pid: Process ID to kill
        force: If True, use SIGKILL instead of SIGTERM

    Returns:
        True if successful, False otherwise
    """
    try:
        process = psutil.Process(pid)

        if force:
            # Force kill
            process.kill()  # SIGKILL
        else:
            # Graceful termination
            process.terminate()  # SIGTERM

        # Wait for process to terminate
        try:
            process.wait(timeout=3)
        except psutil.TimeoutExpired:
            # If still running after timeout, force kill
            if not force:
                return kill_process(pid, force=True)

        return True

    except psutil.NoSuchProcess:
        # Process already dead
        return True
    except psutil.AccessDenied:
        print(f"Access denied when trying to kill PID {pid}")
        return False
    except Exception as e:
        print(f"Error killing process {pid}: {e}")
        return False


def is_process_running(pid: int) -> bool:
    """
    Check if a process is still running.

    Args:
        pid: Process ID

    Returns:
        True if running, False otherwise
    """
    try:
        process = psutil.Process(pid)
        return process.is_running()
    except psutil.NoSuchProcess:
        return False
    except Exception:
        return False
