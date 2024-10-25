import argparse
import os
import re
from pathlib import Path

import cairosvg


def replace_color_in_svg(svg_content: str, new_color: str) -> str:
    """
    Replace all color values in an SVG with a new color.
    Handles hex colors, rgb(), rgba(), named colors, and fill/stroke attributes.
    
    Args:
        svg_content (str): Original SVG content
        new_color (str): New color to replace with (hex format: #RRGGBB)
    
    Returns:
        str: Modified SVG content
    """
    # Regular expressions for different color formats
    color_patterns = [
        r'#[0-9a-fA-F]{3,6}',  # Hex colors
        r'rgb\([^)]+\)',        # RGB colors
        r'rgba\([^)]+\)',       # RGBA colors
        r'(?:fill|stroke)="[^"]+"',  # fill/stroke attributes
        r'(?:aliceblue|antiquewhite|aqua|aquamarine|azure|beige|bisque|black|blanchedalmond|blue|blueviolet|brown|burlywood|cadetblue|chartreuse|chocolate|coral|cornflowerblue|cornsilk|crimson|cyan|darkblue|darkcyan|darkgoldenrod|darkgray|darkgreen|darkgrey|darkkhaki|darkmagenta|darkolivegreen|darkorange|darkorchid|darkred|darksalmon|darkseagreen|darkslateblue|darkslategray|darkslategrey|darkturquoise|darkviolet|deeppink|deepskyblue|dimgray|dimgrey|dodgerblue|firebrick|floralwhite|forestgreen|fuchsia|gainsboro|ghostwhite|gold|goldenrod|gray|green|greenyellow|grey|honeydew|hotpink|indianred|indigo|ivory|khaki|lavender|lavenderblush|lawngreen|lemonchiffon|lightblue|lightcoral|lightcyan|lightgoldenrodyellow|lightgray|lightgreen|lightgrey|lightpink|lightsalmon|lightseagreen|lightskyblue|lightslategray|lightslategrey|lightsteelblue|lightyellow|lime|limegreen|linen|magenta|maroon|mediumaquamarine|mediumblue|mediumorchid|mediumpurple|mediumseagreen|mediumslateblue|mediumspringgreen|mediumturquoise|mediumvioletred|midnightblue|mintcream|mistyrose|moccasin|navajowhite|navy|oldlace|olive|olivedrab|orange|orangered|orchid|palegoldenrod|palegreen|paleturquoise|palevioletred|papayawhip|peachpuff|peru|pink|plum|powderblue|purple|rebeccapurple|red|rosybrown|royalblue|saddlebrown|salmon|sandybrown|seagreen|seashell|sienna|silver|skyblue|slateblue|slategray|slategrey|snow|springgreen|steelblue|tan|teal|thistle|tomato|turquoise|violet|wheat|white|whitesmoke|yellow|yellowgreen)'  # Named colors
    ]
    
    modified_content = svg_content
    
    for pattern in color_patterns:
        if pattern.startswith('(?:fill|stroke)'):
            # Handle fill and stroke attributes
            modified_content = re.sub(
                pattern,
                lambda m: f'{m.group().split("=")[0]}="{new_color}"',
                modified_content
            )
        else:
            # Handle direct color values
            modified_content = re.sub(pattern, new_color, modified_content)
    
    return modified_content

def convert_svg_to_png(
    input_path: str,
    output_path: str,
    width: int = None,
    height: int = None,
    color: str = None
) -> None:
    """
    Convert SVG file to PNG with optional resizing and color replacement.
    
    Args:
        input_path (str): Path to input SVG file
        output_path (str): Path for output PNG file
        width (int, optional): Desired width of output PNG
        height (int, optional): Desired height of output PNG
        color (str, optional): New color to replace all colors in SVG (hex format: #RRGGBB)
    """
    try:
        # Create output directory if it doesn't exist
        output_dir = os.path.dirname(output_path)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
            
        # Read SVG content
        with open(input_path, 'r') as f:
            svg_content = f.read()
            
        # Replace colors if specified
        if color:
            if not re.match(r'^#[0-9a-fA-F]{6}$', color):
                raise ValueError("Color must be in hex format: #RRGGBB")
            svg_content = replace_color_in_svg(svg_content, color)
        
        # Convert to PNG
        cairosvg.svg2png(
            bytestring=svg_content.encode('utf-8'),
            write_to=output_path,
            output_width=width,
            output_height=height
        )
        print(f"Successfully converted {input_path} to {output_path}")
        
    except Exception as e:
        print(f"Error converting SVG to PNG: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Convert SVG to PNG with optional resizing and color replacement')
    parser.add_argument('input', help='Input SVG file path')
    parser.add_argument('output', help='Output PNG file path')
    parser.add_argument('--width', type=int, help='Output width')
    parser.add_argument('--height', type=int, help='Output height')
    parser.add_argument('--color', help='New color in hex format (#RRGGBB)')
    
    args = parser.parse_args()
    
    convert_svg_to_png(
        args.input,
        args.output,
        args.width,
        args.height,
        args.color
    )

if __name__ == "__main__":
    main()