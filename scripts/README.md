# Build Scripts

Scripts for development and distribution.

## For Developers

### Development Mode (Terminal)
```bash
./run.sh
```
Runs the app in development mode with console output. **Not for end users.**

### Build Distribution
```bash
./build_all.sh      # Recommended: Build both .app and DMG
./build_app.sh      # Build only .app bundle
./build_dmg.sh      # Build only DMG (requires .app first)
```

## Output

```
dist/
├── Localhost Monitor.app        # macOS app bundle
└── LocalhostMonitor-0.2.0.dmg   # DMG installer for distribution
```

## Distribution Strategy

- ✅ **DMG installer** → End users
- ❌ **Terminal/Homebrew** → Not supported (development only)

## Requirements

- macOS with Xcode Command Line Tools
- Python 3.9+
- py2app: `pip install py2app`

## Notes

- `_archive_homebrew_tap.sh` → Archived (not used)
- Terminal execution is for development only
- End users should install via DMG

See [CONTRIBUTING.md](../CONTRIBUTING.md) for detailed instructions.
