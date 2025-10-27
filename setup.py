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
    'plist': {
        'LSUIElement': True,  # Makes it a menubar-only app (no dock icon)
        'CFBundleName': 'Localhost Monitor',
        'CFBundleDisplayName': 'Localhost Monitor',
        'CFBundleIdentifier': 'com.localhost-monitor',
        'CFBundleVersion': __version__,
        'CFBundleShortVersionString': __version__,
        'NSHumanReadableCopyright': 'Copyright © 2025 Elber Dalfidan',
    },
    'packages': ['rumps', 'psutil', 'subprocess', 'threading'],
    'includes': ['src.port_scanner', 'src.process_monitor', 'src.config'],
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
