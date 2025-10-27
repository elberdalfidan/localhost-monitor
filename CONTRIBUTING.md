# Contributing to Localhost Monitor

Thank you for your interest in contributing! 🎉

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- macOS version and Python version
- Screenshots if applicable

### Suggesting Features

Feature requests are welcome! Please:
- Check existing issues first
- Describe the feature and use case
- Explain why it would be useful
- Consider implementation complexity

### Pull Requests

1. **Fork the repository**
   ```bash
   git clone https://github.com/elberdalfidan/localhost-monitor.git
   cd localhost-monitor
   ```

2. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Set up development environment**
   ```bash
   # Create virtual environment
   python3 -m venv venv
   source venv/bin/activate

   # Install dependencies
   pip install -r requirements.txt

   # Install development dependencies (optional)
   pip install -e ".[dev]"
   ```

4. **Run the app in development mode**
   ```bash
   ./scripts/run.sh
   # Or directly:
   python -m src.main
   ```

5. **Make your changes**
   - Follow existing code style
   - Add tests if applicable
   - Update documentation

6. **Test your changes**
   ```bash
   # Run unit tests
   python tests/test_scanner.py
   python tests/test_monitor.py

   # Manual testing
   ./scripts/run.sh
   ```

7. **Commit and push**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   git push origin feature/your-feature-name
   ```

8. **Create Pull Request**
   - Go to GitHub and create PR
   - Describe your changes
   - Link any related issues

## Development Guidelines

### Code Style

- **Python**: Follow PEP 8
- **Line length**: 100 characters max
- **Imports**: Group stdlib, third-party, local
- **Comments**: Explain *why*, not *what*

### Commit Messages

Use conventional commits format:
```
feat: add new feature
fix: fix bug in process monitoring
docs: update README
refactor: improve code structure
test: add unit tests
chore: update dependencies
```

### Project Structure

```
src/
├── main.py              # Main app logic
├── config.py            # Configuration
├── port_scanner.py      # Port scanning
├── process_monitor.py   # Process monitoring
├── ui_helpers.py        # UI utilities
└── quick_actions.py     # Batch operations
```

### Adding New Features

1. **Config Changes**: Add settings to `src/config.py`
2. **UI Changes**: Use `ui_helpers.py` for consistency
3. **Actions**: Add to `quick_actions.py` if it's a batch operation
4. **Documentation**: Update README.md and relevant docs

### Testing

- **Manual Testing**: Run `./scripts/run.sh`
- **Unit Tests**: Add to `tests/` directory
- **Test Coverage**: Aim for key functionality

## Building from Source

### Complete Build (Recommended)

```bash
# Build everything: .app + DMG in one command
./scripts/build_all.sh

# Output:
# - dist/Localhost Monitor.app
# - LocalhostMonitor-{version}.dmg
```

### Build macOS App Bundle Only

```bash
# Build the .app bundle (requires py2app)
./scripts/build_app.sh

# The app will be in: dist/Localhost Monitor.app
# Test it:
open "dist/Localhost Monitor.app"
```

### Build DMG Installer Only

```bash
# First build the app, then create DMG
./scripts/build_app.sh
./scripts/build_dmg.sh

# The DMG will be: LocalhostMonitor-{version}.dmg
```

### Build Requirements

- **py2app**: macOS app bundler (`pip install py2app`)
- **macOS**: Required for building .app and DMG
- **Xcode Command Line Tools**: `xcode-select --install`

### Build Artifacts

```
dist/
├── Localhost Monitor.app     # macOS app bundle
└── LocalhostMonitor-0.2.0.dmg  # DMG installer
```

## Running in Development

> **⚠️ Note**: Terminal execution is **development-only**. End users should use the DMG installer.

### Quick Start

```bash
# Activate virtual environment
source venv/bin/activate

# Run directly (development mode)
python -m src.main

# Or use the run script
./scripts/run.sh
```

### Development Mode Features

- ✅ Live code reload (restart app to see changes)
- ✅ Console output for debugging (print statements visible)
- ✅ No code signing required
- ✅ Faster iteration (no build step)

### Production vs Development

| Feature | Development (Terminal) | Production (DMG) |
|---------|----------------------|------------------|
| Launch | `python -m src.main` | Double-click app |
| Debugging | Console output visible | No console output |
| Code signing | Not required | Required for v1.0 |
| Auto-update | Manual git pull | Built-in (v0.3.0) |
| Distribution | Not for end users | DMG installer |

## Questions?

- Open an issue with the `question` label
- Check existing issues and discussions
- Be patient and respectful

## Code of Conduct

This project follows a Code of Conduct. By participating, you agree to uphold this code.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing! 🚀
