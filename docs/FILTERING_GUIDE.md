# 🔍 Process Filtering Guide

## Quick Start

By default, the app **only shows development tools** like:
- ✅ node, npm, yarn, python, ruby, java, go
- ✅ webpack, vite, django, rails, nginx
- ❌ Spotify, Control Center, Safari, Chrome

## Change Filter Mode

Edit `src/config.py`:

```python
# Option 1: Show only development tools (DEFAULT)
FILTER_MODE = "whitelist"

# Option 2: Hide system apps, show everything else
FILTER_MODE = "blacklist"

# Option 3: Show everything (no filtering)
FILTER_MODE = "off"
```

## Add Custom Tools

### Add to Whitelist (show these)

```python
DEV_PROCESS_WHITELIST = [
    # ... existing tools ...
    "mycustomtool",
    "rust-analyzer",
    "docker",
]
```

### Add to Blacklist (hide these)

```python
SYSTEM_PROCESS_BLACKLIST = [
    # ... existing apps ...
    "steam",
    "telegram",
]
```

## Examples

### Before Filtering (FILTER_MODE = "off")
```
🚀 4 processes
├─ :3000 → node          ✅ Development
├─ :5000 → ControlCenter ❌ System
├─ :7000 → ControlCenter ❌ System
└─ :7768 → Spotify       ❌ System
```

### After Filtering (FILTER_MODE = "whitelist")
```
🚀 1 process
└─ :3000 → node          ✅ Development only!
```

## How It Works

**Whitelist Mode:**
- Process name must contain ANY word from whitelist
- Case-insensitive matching
- Example: "node" matches "node", "Node", "node.exe"

**Blacklist Mode:**
- Process name must NOT contain ANY word from blacklist
- Shows everything except blacklisted apps

**Off Mode:**
- No filtering, shows all processes on localhost ports

## Tips

1. **Can't find your process?**
   - Check if it's in the blacklist
   - Try `FILTER_MODE = "off"` temporarily
   - Add your tool to whitelist

2. **Too many system apps?**
   - Use whitelist mode (default)
   - Add unwanted apps to blacklist

3. **Custom dev server?**
   - Add process name to `DEV_PROCESS_WHITELIST`
   - Restart the app

## Configuration File Location

```
localhost-monitor/
└── src/
    └── config.py  ← Edit this file
```

After editing, restart the app to see changes!
