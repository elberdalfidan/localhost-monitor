#!/bin/bash

# Complete build script: Build app bundle + DMG installer

set -e

echo "🚀 Localhost Monitor - Complete Build"
echo "======================================"
echo ""

# Check if in project root
if [ ! -f "setup.py" ]; then
    echo "❌ Error: setup.py not found. Run this from project root."
    exit 1
fi

# Step 1: Build app bundle
echo "📦 Step 1/2: Building app bundle..."
echo "-----------------------------------"
./scripts/build_app.sh

echo ""
echo "📀 Step 2/2: Creating DMG installer..."
echo "---------------------------------------"
./scripts/build_dmg.sh

# Read version from pyproject.toml
VERSION=$(grep '^version = ' pyproject.toml | sed 's/version = "\(.*\)"/\1/')
DMG_NAME="LocalhostMonitor-${VERSION}.dmg"

echo ""
echo "✅ Complete build successful!"
echo "======================================"
echo ""
echo "📦 App Bundle: dist/Localhost Monitor.app"
echo "📀 DMG Installer: ${DMG_NAME}"
echo ""
echo "🧪 Testing:"
echo "  open \"dist/Localhost Monitor.app\""
echo ""
echo "📤 Distribution:"
echo "  Upload ${DMG_NAME} to GitHub Releases"
echo ""
