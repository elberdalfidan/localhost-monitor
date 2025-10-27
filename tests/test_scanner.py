"""Tests for port scanner module."""

import sys
sys.path.insert(0, '/Users/elberdalfidan/Desktop/personal/localhost-monitor')

from src import port_scanner


def test_scan_ports():
    """Test port scanning."""
    print("Testing port scanner...")

    # Scan development port range
    processes = port_scanner.scan_ports(3000, 9000)

    print(f"\nFound {len(processes)} processes:")
    for proc in processes:
        print(f"  Port {proc['port']}: {proc['name']} (PID: {proc['pid']})")

    return processes


if __name__ == "__main__":
    test_scan_ports()
