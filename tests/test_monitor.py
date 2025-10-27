"""Tests for process monitor module."""

import sys
sys.path.insert(0, '/Users/elberdalfidan/Desktop/personal/localhost-monitor')

from src import process_monitor, port_scanner


def test_process_info():
    """Test process info retrieval."""
    print("Testing process monitor...")

    # First get some processes
    processes = port_scanner.scan_ports(3000, 9000)

    if not processes:
        print("No processes found to test")
        return

    print(f"\nTesting {len(processes)} processes:\n")

    for proc in processes:
        pid = proc['pid']
        port = proc['port']

        info = process_monitor.get_process_info(pid)

        if info:
            print(f"Port {port} (PID {pid}):")
            print(f"  Name: {info['name']}")
            print(f"  Memory: {info['memory_mb']} MB")
            print(f"  CPU: {info['cpu_percent']}%")
            print(f"  Uptime: {info['uptime_formatted']}")
            print()
        else:
            print(f"Port {port} (PID {pid}): Could not get info")


if __name__ == "__main__":
    test_process_info()
