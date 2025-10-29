# Changelog

## [0.3.0] - 2025-10-29

### ✨ Added
- **Auto-Update System**: Automatic update checking on startup
  - Check for new versions via GitHub Releases API
  - Silent background check 5 seconds after launch
  - Notification when new version is available
  - Manual "Check for Updates" option in ABOUT section
  - Direct link to download latest release
- **Icon-Free Design**: Removed all emoji/icons for minimal, professional appearance
  - Process status: `[ACTIVE]` instead of 🟢
  - Favorites: `[FAVORITE]` instead of ⭐
  - All menu items now text-only
  - Terminal/IDE aesthetic

### 🔧 Changed
- **UI Redesign**: Complete transition to text-based interface
  - Menu items: "Refresh", "Kill All Ports", "Quit" (no emojis)
  - Process info: "Uptime:" label instead of ⏱ icon
  - Cleaner, more professional look
- **Version System**: Bumped to 0.3.0 for update tracking

### 📝 Technical Details

**Update Checker:**
```python
# New module: src/updater.py
- GitHub API integration (no external dependencies)
- Version comparison (semantic versioning)
- Silent and manual check modes
- Opens releases page in browser

# Configuration in config.py:
ENABLE_AUTO_UPDATE_CHECK = True
AUTO_UPDATE_CHECK_INTERVAL = 86400  # 24 hours
UPDATE_CHECK_ON_STARTUP_DELAY = 5  # seconds
```

**Icon Removal:**
- All emojis removed from UI
- Text-based status indicators
- Professional terminal aesthetic
- Better for accessibility

### 🎯 User Experience
- Users are notified of updates automatically
- One-click access to latest release
- No manual GitHub checking required
- Seamless update workflow

## [0.2.0] - 2025-10-26

### ✨ Added
- **Section-Based UI**: Organized menu with ACTIVE PROCESSES, QUICK ACTIONS, and ABOUT sections
- **Kill All Ports**: Kill all active development processes with one click
- **About Dialog**: Professional dialog showing version, author, license, and description
- **Website Integration**: Direct link to open website from menubar
- **App Metadata**: Version, author, license, and description in config
- **Phase 2 Placeholders**: Favorites (v0.2.1) and Settings GUI (v0.2.2) coming soon
- **New Modules**:
  - `ui_helpers.py` - Section headers, dialogs, formatting utilities
  - `quick_actions.py` - Batch operations (kill all, restart, favorites)

### 🔧 Changed
- **Menu Building**: Complete refactor to section-based architecture
- **Config Organization**: Grouped settings into logical sections with headers
- **Process Display**: Using helper functions for consistent formatting
- **UI Structure**: Three-section layout (Processes, Actions, About)

### 🎨 Improved
- **Visual Hierarchy**: Clear section separators (═══) for better organization
- **User Experience**: More professional and polished interface
- **Code Structure**: Modular, extensible, maintainable architecture
- **Configuration**: More options for customization

### 📝 Configuration Changes
```python
# New in v0.2.0
APP_VERSION = "0.2.0"
APP_AUTHOR = "Elber Dalfidan"
WEBSITE_URL = "https://dalfidan.dev"  # Customize!
ENABLE_KILL_ALL = True
ENABLE_FAVORITES = False  # v0.2.1
ENABLE_SETTINGS_GUI = False  # v0.2.2
SECTION_STYLE = "equals"  # "equals", "dashes", or "none"
SHOW_SECTIONS = True
```

## [0.1.1] - 2025-10-26

### Added
- **Smart Process Filtering**: Filter out system apps (Spotify, Control Center, etc.)
  - 3 modes: whitelist (default), blacklist, off
  - 30+ development tools in whitelist
  - Configurable in `src/config.py`

### Fixed
- **CPU Measurement**: CPU now shows real values instead of always 0.0%
  - Implemented process caching for accurate measurements
  - Configurable measurement interval (default: 0.5s)
  - Multiple samples show varying CPU usage

### Changed
- Port scanner now filters by process name
- Process monitor uses cached objects for better CPU tracking

### Technical Details

**Filtering System:**
```python
# In config.py
FILTER_MODE = "whitelist"  # or "blacklist" or "off"

# Development tools (shown)
DEV_PROCESS_WHITELIST = ["node", "python", "ruby", ...]

# System apps (hidden)
SYSTEM_PROCESS_BLACKLIST = ["spotify", "controlcenter", ...]
```

**CPU Measurement:**
```python
# Old (always 0.0%)
cpu_percent = process.cpu_percent(interval=0.1)

# New (real values)
_process_cache[pid] = process  # Cache for continuity
cpu_percent = process.cpu_percent(interval=0.5)
```

## [0.1.0] - Initial Release

### Features
- Port scanning (3000-9000)
- Process monitoring (RAM, CPU, uptime)
- Kill process functionality
- Auto-refresh every 3 seconds
- macOS menubar integration
- Homebrew formula
- DMG packaging support
