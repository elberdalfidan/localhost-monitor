"""Configuration settings for Localhost Monitor."""

from src import __version__

# ═══════════════════════════════════════════════════════════
# App Metadata
# ═══════════════════════════════════════════════════════════

APP_VERSION = __version__
APP_NAME = "Localhost Monitor"  # Clean name (icon will show in menubar)
APP_AUTHOR = "Elber Dalfidan"
APP_LICENSE = "MIT"
APP_DESCRIPTION = "Monitor and manage localhost development servers from your macOS menubar"

# Website URL
WEBSITE_URL = "https://dalfidan.dev"

# App icon (menubar)
# For bundled app, icon is in Resources/assets/icons/
import os
import sys
from pathlib import Path

def _get_icon_path():
    """Get menubar icon path (works in both dev and bundled app)."""
    # Try multiple possible locations
    possible_paths = []

    # 1. Bundled app (py2app) - icon in Resources/assets/icons/
    try:
        import __main__
        if hasattr(__main__, '__file__'):
            main_file = Path(__main__.__file__)
            # In py2app, main is in Resources/ and assets is in Resources/assets
            resources_dir = main_file.parent
            possible_paths.append(resources_dir / "assets" / "icons" / "icon@2x.png")
            possible_paths.append(resources_dir / "assets" / "icons" / "icon.png")
    except:
        pass

    # 2. Development mode - relative to this file
    try:
        config_file = Path(__file__)
        dev_icon_dir = config_file.parent.parent / "assets" / "icons"
        possible_paths.append(dev_icon_dir / "icon@2x.png")
        possible_paths.append(dev_icon_dir / "icon.png")
    except:
        pass

    # Try all paths
    for icon_path in possible_paths:
        try:
            if icon_path.exists():
                return str(icon_path)
        except:
            continue

    return None

APP_ICON = _get_icon_path()

# ═══════════════════════════════════════════════════════════
# Core Settings
# ═══════════════════════════════════════════════════════════

# Port range for scanning (development servers)
PORT_RANGE_START = 3000
PORT_RANGE_END = 9000

# Refresh interval in seconds
REFRESH_INTERVAL = 3

# Display settings
SHOW_PID = True
SHOW_RAM = True
SHOW_CPU = True
SHOW_UPTIME = True

# Kill signal settings
KILL_TIMEOUT = 5  # seconds to wait before force kill

# Process filtering settings
FILTER_MODE = "whitelist"  # "whitelist", "blacklist", or "off"

# Development process whitelist (case-insensitive)
# Only show processes that match these names
DEV_PROCESS_WHITELIST = [
    "node",
    "npm",
    "yarn",
    "pnpm",
    "deno",
    "bun",
    "python",
    "python3",
    "flask",
    "django",
    "uvicorn",
    "gunicorn",
    "ruby",
    "rails",
    "puma",
    "java",
    "gradle",
    "maven",
    "go",
    "php",
    "php-fpm",
    "nginx",
    "httpd",
    "apache",
    "webpack",
    "vite",
    "next",
    "nuxt",
    "react-scripts",
    "vue-cli-service",
    "ng",  # Angular CLI
    "expo",
    "metro",  # React Native
]

# System process blacklist (case-insensitive)
# Never show these processes
SYSTEM_PROCESS_BLACKLIST = [
    "spotify",
    "controlcenter",
    "controlce",  # Truncated name
    "systemuiserver",
    "finder",
    "dock",
    "safari",
    "chrome",
    "firefox",
    "slack",
    "discord",
    "zoom",
    "teams",
]

# CPU measurement settings
CPU_MEASUREMENT_INTERVAL = 0.5  # seconds to measure CPU usage

# ═══════════════════════════════════════════════════════════
# Quick Actions (Phase 2 Features)
# ═══════════════════════════════════════════════════════════

# Enable/disable Quick Actions features
ENABLE_KILL_ALL = True  # v0.2.0 - Kill all active processes at once
ENABLE_FAVORITES = False  # v0.2.1 - Pin favorite ports to top (coming soon)
ENABLE_QUICK_RESTART = False  # v0.2.2 - Restart processes quickly (coming soon)
ENABLE_SETTINGS_GUI = False  # v0.2.2 - GUI preferences window (coming soon)

# ═══════════════════════════════════════════════════════════
# UI Customization
# ═══════════════════════════════════════════════════════════

# Section header style
SECTION_STYLE = "equals"  # "equals" (═══) or "dashes" (─────) or "none"

# Show section headers in menu
SHOW_SECTIONS = True

# ═══════════════════════════════════════════════════════════
# Auto-Update Settings (v0.3.0)
# ═══════════════════════════════════════════════════════════

# Enable automatic update check on startup
ENABLE_AUTO_UPDATE_CHECK = True

# Auto-update check interval (in seconds)
# Default: 86400 seconds = 24 hours
AUTO_UPDATE_CHECK_INTERVAL = 86400

# Delay before checking for updates on startup (in seconds)
# This allows the app to fully initialize before checking
UPDATE_CHECK_ON_STARTUP_DELAY = 5
