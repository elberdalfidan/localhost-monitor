#!/bin/bash

# Build DMG installer for macOS

set -e

echo "📦 Building Localhost Monitor DMG"
echo "=================================="
echo ""

# Check if app exists
if [ ! -d "dist/Localhost Monitor.app" ]; then
    echo "❌ Error: App bundle not found. Run build_app.sh first."
    exit 1
fi

# Configuration
APP_NAME="Localhost Monitor"
# Read version from pyproject.toml (in project root)
VERSION=$(grep '^version = ' pyproject.toml | sed 's/version = "\(.*\)"/\1/')
DMG_NAME="LocalhostMonitor-${VERSION}"
VOLUME_NAME="Localhost Monitor Installer"
SOURCE_DIR="dist"
DMG_DIR="dmg_build"

# Clean previous DMG builds
echo "🧹 Cleaning previous DMG builds..."
rm -rf "$DMG_DIR"
rm -f "${DMG_NAME}.dmg"

# Create temporary directory for DMG contents
echo "📁 Creating DMG structure..."
mkdir -p "$DMG_DIR"

# Copy app to DMG directory
cp -r "$SOURCE_DIR/$APP_NAME.app" "$DMG_DIR/"

# Create Applications symlink
ln -s /Applications "$DMG_DIR/Applications"

# Create DMG
echo "🔨 Creating DMG..."
hdiutil create -volname "$VOLUME_NAME" \
    -srcfolder "$DMG_DIR" \
    -ov -format UDZO \
    "${DMG_NAME}.dmg"

# Clean up
echo "🧹 Cleaning up..."
rm -rf "$DMG_DIR"

echo ""
echo "✅ DMG created successfully!"
echo "📂 DMG location: ${DMG_NAME}.dmg"
echo ""
echo "To install:"
echo "  1. Open ${DMG_NAME}.dmg"
echo "  2. Drag 'Localhost Monitor' to Applications"
echo "  3. Launch from Applications or Spotlight"
