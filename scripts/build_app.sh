#!/bin/bash

# Build standalone .app bundle using py2app

set -e

echo "🔨 Building Localhost Monitor.app"
echo "=================================="
echo ""

# Check if in project root
if [ ! -f "setup.py" ]; then
    echo "❌ Error: setup.py not found. Run this from project root."
    exit 1
fi

# Clean previous builds
echo "🧹 Cleaning previous builds..."
rm -rf build dist

# Activate venv if exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Install py2app if not installed
if ! pip show py2app > /dev/null 2>&1; then
    echo "📦 Installing py2app..."
    pip install py2app
fi

# Build the app
echo "🔨 Building app bundle..."
python setup.py py2app

# Check if build succeeded
if [ -d "dist/Localhost Monitor.app" ]; then
    echo ""
    echo "✅ Build successful!"
    echo "📂 App location: dist/Localhost Monitor.app"
    echo ""
    echo "To test the app:"
    echo "  open \"dist/Localhost Monitor.app\""
    echo ""
    echo "To install the app:"
    echo "  cp -r \"dist/Localhost Monitor.app\" /Applications/"
else
    echo ""
    echo "❌ Build failed!"
    exit 1
fi
