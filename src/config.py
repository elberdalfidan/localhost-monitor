"""Configuration settings for Localhost Monitor."""

from . import __version__

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
# Place your custom icon in: assets/icons/
# - icon.png (22x22) or icon@2x.png (44x44)
# If None, will use emoji (🚀)
import os
from pathlib import Path

# Try to find custom icon
_icon_dir = Path(__file__).parent.parent / "assets" / "icons"
_icon_paths = [
    _icon_dir / "icon@2x.png",  # Retina (preferred)
    _icon_dir / "icon.png",      # Standard
]

APP_ICON = None
for _icon_path in _icon_paths:
    if _icon_path.exists():
        APP_ICON = str(_icon_path)
        break

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
