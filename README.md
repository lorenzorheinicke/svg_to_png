# SVG to PNG Converter

A Python utility to convert SVG files to PNG format with options for resizing and color modification.

## Features

- Convert SVG files to PNG format
- Resize output images by specifying width and/or height
- Replace all colors in the SVG with a new color
- Support for various color formats (hex, rgb, rgba, named colors)
- Command-line interface for easy use

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Installation

1. Clone this repository or download the files:

```bash
git clone [your-repository-url]
cd svg-to-png-converter
```

2. Create and activate a virtual environment:

```bash
# On Unix/macOS
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
.\venv\Scripts\activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

The script can be used in several ways:

1. Basic conversion:

```bash
python svg_to_png.py input.svg output.png
```

2. Specify dimensions:

```bash
python svg_to_png.py input.svg output.png --width 200 --height 200
```

3. Change all colors:

```bash
python svg_to_png.py input.svg output.png --color "#FF0000"
```

4. Combine options:

```bash
python svg_to_png.py input.svg output.png --width 200 --height 200 --color "#FF0000"
```

### Command Line Arguments

- `input`: Path to input SVG file (required)
- `output`: Path for output PNG file (required)
- `--width`: Desired width of output PNG (optional)
- `--height`: Desired height of output PNG (optional)
- `--color`: New color in hex format (#RRGGBB) (optional)

## Examples

Convert an SVG to a 200x200 PNG with red color:

```bash
python svg_to_png.py assets/image.svg output/image.png --width 200 --height 200 --color "#FF0000"
```

## Error Handling

The script includes error handling for:

- Invalid file paths
- Invalid color formats
- File read/write errors
- Conversion errors

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details

## Acknowledgments

- Uses CairoSVG for SVG to PNG conversion
