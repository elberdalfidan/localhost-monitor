# 🎉 Release Notes - v0.2.0

## Professional UI Upgrade

### ✨ New Features

#### 🎨 Section-Based Menu Layout
The menubar UI has been completely redesigned with a clean, organized structure:

```
🚀 [N] Processes
═══════════════════════════
═══ ACTIVE PROCESSES ═══
🟢 :3000 → node
   ├─ PID: 12345
   ├─ RAM: 245 MB
   ├─ CPU: 8%
   ├─ ⏱  2h 15m
   └─ ❌ Kill Process
───────────────────────────
═══ QUICK ACTIONS ═══
🔄 Refresh
⚡ Kill All Ports (NEW!)
📌 Favorites (v0.2.1)
───────────────────────────
═══ ABOUT ═══
ℹ️  About Localhost Monitor
🌐 Website
⚙️  Settings (v0.2.2)
───────────────────────────
🚪 Quit
```

#### ⚡ Kill All Ports
- Kill all active development processes with one click
- Confirmation dialog for safety
- Shows success/failure notification
- Auto-refreshes menu after execution

#### ℹ️ About Dialog
Professional about dialog with:
- Version information (v0.2.0)
- Author and license details
- App description
- "Visit Website" button

#### 🌐 Website Integration
- Direct link to your personal website or GitHub
- Configurable in `config.py`
- Opens in default browser

#### 📌 Phase 2 Foundation
- Placeholders for upcoming features
- Favorites (v0.2.1) - coming soon
- Settings GUI (v0.2.2) - coming soon
- Quick Restart (v0.2.2) - coming soon

### 🔧 Technical Improvements

#### New Modules
- **`ui_helpers.py`**: Section headers, dialogs, formatting
- **`quick_actions.py`**: Batch operations and utilities

#### Enhanced Configuration
```python
# App Metadata
APP_VERSION = "0.2.0"
APP_AUTHOR = "Elber Dalfidan"
WEBSITE_URL = "https://dalfidan.dev"  # Customize this!

# Quick Actions Toggles
ENABLE_KILL_ALL = True
ENABLE_FAVORITES = False  # Coming in v0.2.1
ENABLE_SETTINGS_GUI = False  # Coming in v0.2.2

# UI Customization
SECTION_STYLE = "equals"  # or "dashes" or "none"
SHOW_SECTIONS = True
```

#### Refactored Menu Building
- Clean section-based architecture
- Modular menu construction
- Easy to extend with new features
- Better separation of concerns

### 📊 Before & After

**v0.1.1 (Old)**
```
🚀 4
───────────────
🟢 :3000 → node
   └─ [stats...]
───────────────
Refresh
Quit
```

**v0.2.0 (New)**
```
🚀 4
═══════════════════════════
═══ ACTIVE PROCESSES ═══
🟢 :3000 → node
   └─ [stats...]
───────────────────────────
═══ QUICK ACTIONS ═══
🔄 Refresh
⚡ Kill All Ports
📌 Favorites (v0.2.1)
───────────────────────────
═══ ABOUT ═══
ℹ️  About
🌐 Website
⚙️  Settings (v0.2.2)
───────────────────────────
🚪 Quit
```

### 🚀 Quick Start

1. **Update to v0.2.0**
   ```bash
   git pull
   # or download latest release
   ```

2. **Customize Website URL**
   Edit `src/config.py`:
   ```python
   WEBSITE_URL = "https://dalfidan.dev"  # Your URL here!
   ```

3. **Run the App**
   ```bash
   ./scripts/run.sh
   ```

4. **Try New Features**
   - Click 🚀 icon → See new sections
   - Click "⚡ Kill All Ports" → Kill all at once
   - Click "ℹ️ About" → See app info
   - Click "🌐 Website" → Visit your site

### 🎯 What's Next?

#### v0.2.1 - Favorites (Coming Soon)
- Star/pin favorite ports
- Keep favorites at top
- Persist across sessions

#### v0.2.2 - GUI Settings (Coming Soon)
- Preferences window
- Change settings without editing code
- Port range configuration
- Filter mode selection

### 🐛 Bug Fixes
- Improved menu refresh logic
- Better error handling
- More robust process tracking

### 💡 Tips

1. **Customize Section Style**
   ```python
   SECTION_STYLE = "dashes"  # Use ─── instead of ═══
   ```

2. **Hide Sections**
   ```python
   SHOW_SECTIONS = False  # Cleaner, minimal look
   ```

3. **Disable Kill All**
   ```python
   ENABLE_KILL_ALL = False  # If you prefer manual killing
   ```

### 📝 Upgrade Notes

**Breaking Changes:** None! Fully backward compatible.

**New Dependencies:** None! Uses same dependencies.

**Configuration:** Optional. Old config.py still works.

### 🙏 Feedback

We'd love to hear your thoughts!
- GitHub Issues: Report bugs
- Feature Requests: Suggest improvements
- Pull Requests: Contribute code

---

**Enjoy the new professional UI!** 🎉

*Release Date: October 26, 2025*
