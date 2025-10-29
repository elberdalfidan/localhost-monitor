"""Setup script for creating standalone macOS .app bundle."""

from setuptools import setup
import sys
import os
sys.path.insert(0, '.')
from src import __version__

APP = ['src/main.py']

# Include assets (icons, resources)
DATA_FILES = []
assets_icons = []
if os.path.exists('assets/icons/icon.png'):
    assets_icons.append('assets/icons/icon.png')
if os.path.exists('assets/icons/icon@2x.png'):
    assets_icons.append('assets/icons/icon@2x.png')
if assets_icons:
    DATA_FILES.append(('assets/icons', assets_icons))

OPTIONS = {
    'argv_emulation': False,
    'iconfile': 'assets/app.icns',  # App icon for Finder/Dock
    'plist': {
        'LSUIElement': True,  # Makes it a menubar-only app (no dock icon)
        'CFBundleName': 'Localhost Monitor',
        'CFBundleDisplayName': 'Localhost Monitor',
        'CFBundleIdentifier': 'com.localhost-monitor',
        'CFBundleVersion': __version__,
        'CFBundleShortVersionString': __version__,
        'CFBundleIconFile': 'app.icns',  # Icon reference in Info.plist
        'NSHumanReadableCopyright': 'Copyright © 2025 Elber Dalfidan',
    },
    'packages': [
        'rumps',
        'psutil',
        'urllib',
        'json',
        'webbrowser',
        'pkg_resources',
        'setuptools'
    ],
    'includes': [
        'src.port_scanner',
        'src.process_monitor',
        'src.config',
        'src.ui_helpers',
        'src.quick_actions',
        'src.updater',
        'jaraco',
        'jaraco.text',
        'jaraco.functools',
        'jaraco.context'
    ],
    'excludes': [
        'tkinter',
        'PyQt5',
        'PyQt6',
        'test',
        'unittest',
        'distutils'
    ],
    # Use semi_standalone to avoid setuptools/pkg_resources issues
    'semi_standalone': False,
    'site_packages': True,
}

setup(
    name='Localhost Monitor',
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    install_requires=[
        'rumps>=0.4.0',
        'psutil>=5.9.0',
    ],
)
