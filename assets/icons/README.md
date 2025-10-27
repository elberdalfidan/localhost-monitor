# Icon Guidelines

## Menubar Icon Requirements

### Format & Size
- **Format**: PNG with transparency
- **Standard**: `icon.png` → 22x22 pixels
- **Retina**: `icon@2x.png` → 44x44 pixels (recommended)
- **Color**: Black shapes on transparent background

### Design Guidelines

1. **Template Image Style**
   - Use solid black (#000000) for the icon shape
   - Transparent background
   - macOS will automatically invert colors based on menu bar theme (light/dark mode)

2. **Visual Design**
   - Simple, recognizable silhouette
   - Clear at small sizes (22x22)
   - Avoid fine details that won't be visible
   - Maintain visual balance

3. **Safe Area**
   - Keep important elements within 18x18 center area
   - Leave 2px padding on all sides

### File Structure

```
assets/icons/
├── icon.png          # 22x22 standard resolution
├── icon@2x.png       # 44x44 retina resolution (recommended)
└── README.md         # This file
```

### How to Add Your Logo

1. **Export your logo as PNG** with these specs:
   ```
   - Size: 44x44 pixels
   - Background: Transparent
   - Color: Black (#000000) shapes only
   - Format: PNG-24 with alpha channel
   ```

2. **Create both versions**:
   ```bash
   # If you only have 44x44:
   icon@2x.png  (44x44 - your original)
   icon.png     (22x22 - downscaled version)
   ```

3. **Place files in**: `assets/icons/`

4. **Test**: Run `./scripts/build_app.sh` and launch the app

### Design Tools

- **Figma/Sketch**: Export as PNG, 44x44, transparent background
- **Preview.app**: Resize if needed (Tools → Adjust Size)
- **ImageMagick**: Batch resize
  ```bash
  # Create standard from retina
  convert icon@2x.png -resize 22x22 icon.png
  ```

### Example Icons

Good menubar icons:
- ✅ Simple geometric shapes
- ✅ Clear silhouettes
- ✅ High contrast edges
- ✅ Recognizable at 22px

Avoid:
- ❌ Too much detail
- ❌ Gradients (will be lost)
- ❌ Colors (will be converted to black)
- ❌ Text that's too small

### Testing

```bash
# Build and test
./scripts/build_app.sh
open "dist/Localhost Monitor.app"

# Check both light and dark menu bar themes
# System Settings → Appearance → Light/Dark
```

### Current Icon

If no custom icon is provided, the app will use the default emoji (🚀).

### Tips

- Start with 88x88 or 128x128, then downscale for crisp edges
- Test in both light and dark mode
- Ensure icon is clearly visible against menu bar background
- Keep it simple - menubar icons are tiny!
