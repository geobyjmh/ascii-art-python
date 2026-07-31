import argparse
import sys
from pathlib import Path

from PIL import Image, UnidentifiedImageError

ASCII_CHARS = "@%#*+=-:. "


def image_to_ascii(image_path: str, width: int = 80) -> str:
    # TODO: add stronger input validation for width and file types.
    # TODO: improve brightness mapping for better-looking output.
    # TODO: add automated tests for success and failure cases.
    with Image.open(image_path) as img:
        img = img.convert("L")
        aspect_ratio = img.height / img.width
        height = max(1, int(width * aspect_ratio / 2))
        img = img.resize((width, height))
        pixels = list(img.getdata())

    lines = []
    for i in range(0, len(pixels), width):
        row = pixels[i : i + width]
        line = "".join(
            ASCII_CHARS[min(len(ASCII_CHARS) - 1, int(pixel / 255 * (len(ASCII_CHARS) - 1)))]
            for pixel in row
        )
        lines.append(line)
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Convert an image to ASCII art")
    parser.add_argument("input_image", help="Path to the input image file")
    parser.add_argument("-o", "--output", help="Optional path to write the ASCII art text")
    parser.add_argument("-w", "--width", type=int, default=80, help="Output width in characters")
    parser.add_argument("--show", action="store_true", help="Print the ASCII art to the terminal")
    args = parser.parse_args()

    try:
        ascii_art = image_to_ascii(args.input_image, width=args.width)
    except FileNotFoundError:
        print(f"Error: file not found: {args.input_image}", file=sys.stderr)
        return 1
    except UnidentifiedImageError:
        print(f"Error: unsupported or invalid image file: {args.input_image}", file=sys.stderr)
        return 1

    if args.output:
        Path(args.output).write_text(ascii_art, encoding="utf-8")
    if args.show or not args.output:
        print(ascii_art)

    return 0


if __name__ == "__main__":
    sys.exit(main())