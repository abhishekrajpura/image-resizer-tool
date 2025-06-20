# Image Resizer Tool

A simple Python script to resize images with interactive user input. This tool allows you to resize images while optionally maintaining aspect ratio.

## Features

- **Interactive CLI**: User-friendly command-line interface
- **Aspect Ratio Control**: Option to maintain or ignore aspect ratio
- **Format Support**: Supports all common image formats (JPEG, PNG, GIF, BMP, etc.)
- **Auto-naming**: Automatically generates output filenames if not specified
- **Image Preview**: Option to view the resized image after processing

## Prerequisites

- Python 3.6 or higher
- Pillow library

## Installation

1. Clone this repository:
```bash
git clone https://github.com/abhishekrajpura/image-resizer-tool.git
cd image-resizer-tool
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the script:
```bash
python image_resizer.py
```

The script will prompt you for:
- Input image path
- Output image path (optional - auto-generated if not provided)
- Target width and height
- Whether to maintain aspect ratio

### Example Usage

```
=== Image Resizer Tool ===

Enter the path to your image file: /path/to/your/image.jpg
Enter output file path (press Enter for auto-generated name): 
Enter target width (pixels): 800
Enter target height (pixels): 600
Maintain aspect ratio? (y/n): y

Original size: 1920x1080
Resized image saved as: /path/to/your/image_resized.jpg
New size: 800x450

✅ Image resized successfully!

Would you like to open the resized image? (y/n): y
```

## Supported Image Formats

- JPEG (.jpg, .jpeg)
- PNG (.png)
- GIF (.gif)
- BMP (.bmp)
- TIFF (.tiff, .tif)
- WebP (.webp)
- And many more supported by Pillow

## Features Explained

### Aspect Ratio Maintenance
When enabled, the tool automatically adjusts the dimensions to maintain the original image's proportions, preventing distortion.

### High-Quality Resampling
Uses Lanczos resampling for high-quality image resizing.

### Cross-Platform Compatibility
Works on Windows, macOS, and Linux systems.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Troubleshooting

### Common Issues

**"ModuleNotFoundError: No module named 'PIL'"**
- Install Pillow: `pip install Pillow`

**"FileNotFoundError"**
- Check that the input file path is correct
- Ensure the file exists and is accessible

**"Permission Error"**
- Check write permissions for the output directory
- Try running with administrator/sudo privileges if needed

## Changelog

### v1.0.0
- Initial release
- Basic image resizing functionality
- Interactive CLI interface
- Aspect ratio maintenance option
- Auto-generated output filenames