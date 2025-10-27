<div align="center">

# 🚀 Localhost Monitor

**Monitor and kill localhost development servers from your macOS menubar**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![macOS](https://img.shields.io/badge/platform-macOS-lightgrey.svg)](https://www.apple.com/macos/)
[![Version](https://img.shields.io/badge/version-0.2.0-green.svg)](https://github.com/elberdalfidan/localhost-monitor/releases)

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Contributing](#-contributing)

</div>

---

## ✨ Features

- 🔍 **Auto-detect** processes running on localhost ports (3000-9000)
- 🎯 **Smart Filtering** - Only shows development tools (node, python, etc.), hides system apps
- 📊 **Monitor** RAM, CPU usage, and uptime for each process
- ⚡ **Kill All Ports** - Terminate all dev servers with one click
- ❌ **Kill Individual Process** - Stop specific servers from the menubar
- 🔄 **Auto-refresh** every 3 seconds
- ℹ️ **About Dialog** - Version info and website link
- ⚙️ **Configurable** - Customize filters, ports, and refresh rate
- 🎨 **Section-Based UI** - Clean, organized menubar interface

## 📸 Screenshots

```
🚀 [N]
═══════════════════════════════
═══ ACTIVE PROCESSES ═══
🟢 :3000 → node
   ├─ PID: 12345
   ├─ RAM: 245 MB
   ├─ CPU: 8%
   ├─ ⏱  2h 15m
   └─ ❌ Kill Process
───────────────────────────────
═══ QUICK ACTIONS ═══
🔄 Refresh
⚡ Kill All Ports
📌 Favorites (v0.2.1)
───────────────────────────────
═══ ABOUT ═══
ℹ️  About Localhost Monitor
🌐 Website
⚙️  Settings (v0.2.2)
───────────────────────────────
⏏ Quit
```

## 🚀 Installation

### Download and Install

1. **Download** the latest DMG from [Releases](https://github.com/elberdalfidan/localhost-monitor/releases)
2. **Open** the DMG file
3. **Drag** "Localhost Monitor" to your Applications folder
4. **Launch** from Applications or Spotlight search

### Requirements

- **macOS** 10.13+ (High Sierra or later)

### First Launch

On first launch, macOS may show a security warning. To allow:
1. Open **System Settings** → **Privacy & Security**
2. Click **"Open Anyway"** next to the Localhost Monitor message
3. Confirm by clicking **"Open"**

Alternatively, right-click the app and select **"Open"**.

## 💡 Usage

1. **Launch**: Open "Localhost Monitor" from Applications
2. **Monitor**: Click 🚀 icon in menubar to see all active localhost processes
3. **Kill Individual**: Expand a process → Click "❌ Kill Process"
4. **Kill All**: Click "⚡ Kill All Ports" to stop all dev servers at once
5. **Refresh**: Manual refresh or auto-refresh every 3 seconds
6. **Quit**: Select "⏏ Quit" from the menu when done

## ⚙️ Configuration

Default settings work for most users:
- **Port Range**: 3000-9000 (common development ports)
- **Auto-refresh**: Every 3 seconds
- **Process Filter**: Shows only development tools (node, python, etc.)

**Advanced users** can customize settings in `src/config.py` or wait for the Settings GUI (coming in v0.2.2).

For detailed configuration options, see [docs/FILTERING_GUIDE.md](docs/FILTERING_GUIDE.md).

## 🛠️ Development

Want to contribute? See the [Contributing Guide](CONTRIBUTING.md) for:
- Development setup
- Building from source
- Running tests
- Project structure
- Code guidelines

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

See also: [Code of Conduct](CODE_OF_CONDUCT.md) | [Security Policy](SECURITY.md)

## 📝 Changelog

See [CHANGELOG.md](CHANGELOG.md) for all changes and version history.

**Latest: v0.2.0**
- ✨ Section-based UI layout
- ⚡ Kill All Ports action
- ℹ️ About dialog and website integration
- 🎯 Smart process filtering (v0.1.1)
- ⚡ Accurate CPU measurement (v0.1.1)

## 🗺️ Roadmap

- [x] Core functionality (scan, monitor, kill)
- [x] Auto-refresh
- [x] Smart process filtering (v0.1.1)
- [x] Section-based UI (v0.2.0)
- [x] Kill All Ports (v0.2.0)
- [x] DMG distribution (v0.2.0)
- [ ] Favorites/Pinning (v0.2.1 - planned)
- [ ] Preferences GUI (v0.2.2 - planned)
- [ ] Auto-update system (v0.3.0 - planned)
- [ ] Code signing & notarization (v1.0.0 - planned)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Elber Dalfidan**

- GitHub: [@elberdalfidan](https://github.com/elberdalfidan)

## 🙏 Acknowledgments

- Built with [rumps](https://github.com/jaredks/rumps) - Ridiculously Uncomplicated macOS Python Statusbar apps
- Process monitoring with [psutil](https://github.com/giampaolo/psutil)

---

<div align="center">

**⭐ Star this repo if you find it useful! ⭐**

[Report Bug](https://github.com/elberdalfidan/localhost-monitor/issues) • [Request Feature](https://github.com/elberdalfidan/localhost-monitor/issues) • [Ask Question](https://github.com/elberdalfidan/localhost-monitor/issues)

Made with ❤️ for developers who hate managing localhost processes

</div>
