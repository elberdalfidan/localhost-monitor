# 🎨 Custom Icon Setup - Quick Guide

## Step 1: Prepare Your Logo

### Required Specifications
- **Size**: 44x44 pixels (Retina)
- **Format**: PNG with transparency
- **Colors**: Black shapes only (#000000)
- **Background**: Transparent

### Why Black Only?
macOS automatically inverts menubar icons:
- **Light mode**: Black icon on light background
- **Dark mode**: White icon on dark background

This is called "template image" mode and it's standard for macOS menubar apps.

## Step 2: Export Your Logo

### From Figma/Sketch:
1. Select your logo
2. Export as PNG
3. Size: 44x44 pixels
4. Background: Transparent
5. Make sure all colors are black

### From Photoshop/Illustrator:
1. File → Export → Export As
2. Format: PNG-24
3. Canvas: 44x44 pixels
4. Transparency: Checked
5. Convert all colors to black (#000000)

## Step 3: Place Files

Save your icon as **one of these names**:

```bash
assets/icons/icon@2x.png   # 44x44 (Retina) - RECOMMENDED
# or
assets/icons/icon.png      # 22x22 (Standard)
```

**Tip**: Just create the 44x44 version (`icon@2x.png`). macOS will automatically scale it down if needed.

## Step 4: Test

### Test in Development
```bash
# Run in terminal to see if icon loads
python -m src.main
```

### Test in Production
```bash
# Build the app
./scripts/build_app.sh

# Launch and check menubar
open "dist/Localhost Monitor.app"
```

## Example Structure

```
localhost-monitor/
├── assets/
│   └── icons/
│       ├── icon@2x.png       ← Your 44x44 logo here
│       ├── ICON_SETUP.md     ← This guide
│       └── README.md         ← Detailed guidelines
├── src/
└── ...
```

## Current Behavior

- ✅ **With icon**: Your custom logo appears in menubar
- ✅ **Without icon**: Fallback to default (no menubar icon shown, just text)
- ✅ **Automatic**: App detects icon automatically, no config needed

## Design Tips

✅ **Good menubar icons:**
- Simple geometric shapes
- Clear silhouette
- 2-3px line thickness minimum
- Centered with 2-4px padding

❌ **Avoid:**
- Too much detail (won't be visible at 22px)
- Thin lines (<2px)
- Gradients (will be converted to solid)
- Colors other than black

## Testing Both Themes

1. Build and run the app
2. Open **System Settings** → **Appearance**
3. Toggle between **Light** and **Dark**
4. Check if your icon looks good in both

## Troubleshooting

**Icon not showing?**
- Check file name: `icon@2x.png` or `icon.png`
- Check location: `assets/icons/`
- Check format: PNG with transparency
- Rebuild the app: `./scripts/build_app.sh`

**Icon looks weird?**
- Make sure it's black shapes only
- Remove any colors/gradients
- Check transparency is working
- Try simpler design

## Need Help?

See detailed guidelines: [icons/README.md](icons/README.md)
