# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Localhost Monitor is a macOS menubar application that monitors and manages localhost development servers. Built with Python using `rumps` (Ridiculously Uncomplicated macOS Python Statusbar apps) and `psutil` for process monitoring.

**Current Version:** 0.3.0

## Development Commands

### Running the App

```bash
# Development mode (from terminal)
python -m src.main

# Or use the run script
./scripts/run.sh
```

### Testing

```bash
# Run unit tests
python tests/test_scanner.py
python tests/test_monitor.py
python tests/test_cpu.py
```

### Building

```bash
# Build everything (.app bundle + DMG installer)
./scripts/build_all.sh

# Build .app bundle only
./scripts/build_app.sh

# Build DMG installer only (requires .app to exist)
./scripts/build_dmg.sh
```

**Build Requirements:**
- py2app: `pip install py2app`
- macOS with Xcode Command Line Tools

**Build Artifacts:**
- `dist/Localhost Monitor.app` - macOS app bundle
- `LocalhostMonitor-{version}.dmg` - DMG installer

### Dependencies

```bash
# Install runtime dependencies
pip install -r requirements.txt

# Core dependencies:
# - rumps>=0.4.0 (menubar app framework)
# - psutil>=5.9.0 (process monitoring)
```

## Architecture

### Core Module Structure

The application follows a modular architecture with clear separation of concerns:

**`src/main.py`** - Main application entry point
- `LocalhostMonitorApp` class extends `rumps.App`
- Manages menubar UI with section-based layout (ACTIVE PROCESSES, QUICK ACTIONS, ABOUT)
- Auto-refresh timer (configurable interval)
- Process state management with in-memory cache

**`src/port_scanner.py`** - Port scanning via lsof
- Scans TCP ports in range (default: 3000-9000) for LISTEN state
- Process filtering (whitelist/blacklist modes)
- Returns: `[{'port': int, 'pid': int, 'name': str}]`

**`src/process_monitor.py`** - Process monitoring via psutil
- Retrieves detailed process info (RAM, CPU, uptime)
- Process cache for accurate CPU measurement (psutil requires interval)
- Graceful termination with SIGTERM → SIGKILL fallback
- Returns: `{'pid', 'name', 'memory_mb', 'cpu_percent', 'uptime_seconds', 'uptime_formatted'}`

**`src/ui_helpers.py`** - UI utilities
- Section headers (═══ style)
- Dialog helpers (about, confirmation, info)
- Process title formatting with favorite support
- Website launcher

**`src/quick_actions.py`** - Batch operations
- Kill All Ports: terminate all monitored processes with confirmation
- Favorites (placeholder for v0.2.1)
- Restart process (placeholder for v0.2.2)

**`src/updater.py`** - Update checking
- Queries GitHub API for latest release
- Compares semantic versions
- Notifications for new versions
- DMG download URL extraction

**`src/config.py`** - Centralized configuration
- Port range, refresh interval, display settings
- Process filtering: whitelist (dev tools), blacklist (system apps)
- Feature flags for upcoming features
- Icon path resolution (dev vs bundled app)

### Key Design Patterns

**Process Cache Strategy:**
- `process_monitor.py` maintains `_process_cache: Dict[int, psutil.Process]`
- psutil.Process.cpu_percent() requires interval or cached object for accuracy
- First call returns 0.0, subsequent calls return actual usage since last measurement
- Cache invalidation on process termination

**Icon Resolution:**
- Development: `assets/icons/icon@2x.png` (relative to repo root)
- Bundled app: `Resources/assets/icons/icon@2x.png` (py2app Resources dir)
- `_get_icon_path()` tries multiple paths for portability

**Section-Based Menu:**
1. ACTIVE PROCESSES: Expandable items per port (PID, RAM, CPU, uptime, kill button)
2. QUICK ACTIONS: Refresh, Kill All Ports, Favorites (coming), Settings (coming)
3. ABOUT: About dialog, Website, Check for Updates

**Process Filtering:**
- Whitelist mode (default): Only show dev tools (node, python, etc.)
- Blacklist mode: Hide system apps (Spotify, ControlCenter, etc.)
- Configurable in `src/config.py` via `DEV_PROCESS_WHITELIST` and `SYSTEM_PROCESS_BLACKLIST`

### Distribution

**Development vs Production:**
- Development: Run via `python -m src.main`, console output visible
- Production: DMG installer with .app bundle, no console, menubar-only (LSUIElement=True)

**py2app Configuration:**
- `setup.py` defines bundle structure
- `LSUIElement=True`: No dock icon (menubar-only app)
- `semi_standalone=False, site_packages=True`: Proper dependency packaging
- Includes jaraco modules for setuptools compatibility

## Important Configuration

**Port Range:** `PORT_RANGE_START = 3000`, `PORT_RANGE_END = 9000`
- Common development ports

**Refresh Interval:** `REFRESH_INTERVAL = 3` seconds

**CPU Measurement:** `CPU_MEASUREMENT_INTERVAL = 0.5` seconds
- Balance between accuracy and performance

**Process Filtering:** `FILTER_MODE = "whitelist"`
- Options: "whitelist", "blacklist", "off"

**Feature Flags:**
- `ENABLE_KILL_ALL = True` (v0.2.0 - implemented)
- `ENABLE_FAVORITES = False` (v0.2.1 - planned)
- `ENABLE_SETTINGS_GUI = False` (v0.2.2 - planned)
- `ENABLE_AUTO_UPDATE_CHECK = True` (v0.3.0 - implemented)

## Version Management

Version is stored in `src/__init__.py`:
```python
__version__ = "0.3.0"
```

This version is imported by:
- `src/config.py` → `APP_VERSION`
- `setup.py` → `CFBundleVersion`
- `src/updater.py` → version comparison

When releasing, update `__version__` and the version will propagate throughout the app.

## Roadmap Context

- **v0.2.0** (released): Section-based UI, Kill All Ports, About dialog
- **v0.2.1** (planned): Favorites/pinning feature
- **v0.2.2** (planned): Settings GUI, Quick Restart
- **v0.3.0** (released): Auto-update system
- **v1.0.0** (planned): Code signing & notarization

## Testing Notes

Tests are minimal unit tests for core functionality:
- `test_scanner.py`: Port scanning logic
- `test_monitor.py`: Process monitoring
- `test_cpu.py`: CPU measurement accuracy

Manual testing is primary method - run `./scripts/run.sh` and verify menubar behavior.

## Security Considerations

- Uses `lsof` and `psutil` which require appropriate permissions on macOS
- Process termination uses graceful SIGTERM with SIGKILL fallback
- No elevated privileges required (monitors only user's processes)
- Update checker uses HTTPS GitHub API
