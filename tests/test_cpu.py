"""Test CPU measurement with multiple samples."""

import sys
import time
sys.path.insert(0, '/Users/elberdalfidan/Desktop/personal/localhost-monitor')

from src import process_monitor, port_scanner


def test_cpu_measurement():
    """Test CPU measurement over multiple samples."""
    print("Testing CPU measurement over time...\n")

    # Get processes
    processes = port_scanner.scan_ports(3000, 9000)

    if not processes:
        print("No processes found to test")
        return

    print(f"Found {len(processes)} development processes\n")

    for proc in processes:
        pid = proc['pid']
        port = proc['port']
        name = proc['name']

        print(f"📊 Port {port} - {name} (PID {pid})")
        print("=" * 50)

        # Take 5 samples over 15 seconds
        for i in range(5):
            info = process_monitor.get_process_info(pid)

            if info:
                print(f"Sample {i+1}:")
                print(f"  RAM: {info['memory_mb']} MB")
                print(f"  CPU: {info['cpu_percent']}%")
                print(f"  Uptime: {info['uptime_formatted']}")
            else:
                print(f"Sample {i+1}: Process no longer exists")
                break

            if i < 4:  # Don't sleep after last sample
                time.sleep(3)

        print()


if __name__ == "__main__":
    test_cpu_measurement()
