"""Quick action functions for batch operations."""

import rumps
from typing import Dict, List

import src.process_monitor as process_monitor
import src.ui_helpers as ui_helpers


def kill_all_processes(processes: Dict[int, Dict]) -> tuple[int, int]:
    """
    Kill all active processes.

    Args:
        processes: Dictionary of port -> process info

    Returns:
        Tuple of (successful_kills, total_processes)
    """
    if not processes:
        return 0, 0

    total = len(processes)
    successful = 0

    for port, proc_info in processes.items():
        pid = proc_info.get('pid')
        if pid:
            try:
                if process_monitor.kill_process(pid):
                    successful += 1
            except Exception as e:
                print(f"Error killing process {pid}: {e}")

    return successful, total


def confirm_kill_all(process_count: int) -> bool:
    """
    Show confirmation dialog for killing all processes.

    Args:
        process_count: Number of processes to kill

    Returns:
        True if user confirmed, False otherwise
    """
    if process_count == 0:
        ui_helpers.show_info_dialog(
            title="No Processes",
            message="No active processes to kill."
        )
        return False

    message = (
        f"Are you sure you want to kill all {process_count} "
        f"active development {'process' if process_count == 1 else 'processes'}?\n\n"
        "This action cannot be undone."
    )

    return ui_helpers.show_confirmation_dialog(
        title="Kill All Processes",
        message=message,
        ok_text="Kill All",
        cancel_text="Cancel"
    )


def execute_kill_all(processes: Dict[int, Dict]) -> None:
    """
    Execute kill all action with confirmation and notification.

    Args:
        processes: Dictionary of port -> process info
    """
    process_count = len(processes)

    # Show confirmation dialog
    if not confirm_kill_all(process_count):
        return

    # Execute kills
    successful, total = kill_all_processes(processes)

    # Show result notification
    if successful == total:
        rumps.notification(
            title="Kill All Complete",
            subtitle=f"Successfully killed {successful} processes",
            message="All development servers have been stopped"
        )
    else:
        failed = total - successful
        rumps.notification(
            title="Kill All Partial Success",
            subtitle=f"Killed {successful}/{total} processes",
            message=f"{failed} processes could not be stopped"
        )


def restart_process(pid: int, command: str = None) -> bool:
    """
    Restart a process (kill and start again).

    NOTE: This is a placeholder for v0.2.2.
    Requires command detection or user input.

    Args:
        pid: Process ID to restart
        command: Command to run (optional)

    Returns:
        True if successful, False otherwise
    """
    # Phase 2.2 feature - coming soon
    ui_helpers.show_info_dialog(
        title="Feature Coming Soon",
        message="Quick Restart will be available in v0.2.2"
    )
    return False


def toggle_favorite(port: int, favorites: set) -> set:
    """
    Toggle favorite status for a port.

    NOTE: This is a placeholder for v0.2.1.

    Args:
        port: Port number
        favorites: Set of favorite ports

    Returns:
        Updated favorites set
    """
    if port in favorites:
        favorites.remove(port)
    else:
        favorites.add(port)

    return favorites


def get_process_summary(processes: Dict[int, Dict]) -> str:
    """
    Get a summary of all processes for display or export.

    Args:
        processes: Dictionary of port -> process info

    Returns:
        Formatted summary string
    """
    if not processes:
        return "No active processes"

    lines = ["Active Development Processes:", "=" * 40]

    for port, proc_info in sorted(processes.items()):
        lines.append(f"\nPort {port}:")
        lines.append(f"  Name: {proc_info.get('name', 'Unknown')}")
        lines.append(f"  PID: {proc_info.get('pid', 'N/A')}")
        lines.append(f"  RAM: {proc_info.get('memory_mb', 'N/A')} MB")
        lines.append(f"  CPU: {proc_info.get('cpu_percent', 'N/A')}%")
        lines.append(f"  Uptime: {proc_info.get('uptime_formatted', 'N/A')}")

    lines.append("\n" + "=" * 40)
    lines.append(f"Total: {len(processes)} processes")

    return "\n".join(lines)
