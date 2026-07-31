"""Convert images into ASCII art and write or print the result."""

import argparse
import sys
from pathlib import Path

from PIL import Image, UnidentifiedImageError

ASCII_CHARS = "@%#*+=-:. "


def rotate_image(img: Image.Image, angle: int) -> Image.Image:
    """Rotate an image by one of the supported angles."""
    if angle == 0:
        return img
    if angle == 90:
        return img.transpose(Image.Transpose.ROTATE_90)
    if angle == 180:
        return img.transpose(Image.Transpose.ROTATE_180)
    if angle == -90:
        return img.transpose(Image.Transpose.ROTATE_270)
    raise ValueError("rotate must be one of 0, 90, 180, -90")


def image_to_ascii(image_path: str, width: int = 80, rotate: int = 0) -> str:
    """Return ASCII art for an image path using a simple grayscale mapping."""
    if width <= 0:
        raise ValueError("width must be a positive integer")
    if not image_path:
        raise ValueError("image_path must not be empty")

    with Image.open(image_path) as img:
        img = rotate_image(img, rotate).convert("L")
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


def build_parser() -> argparse.ArgumentParser:
    """Create the CLI parser for the ASCII art converter."""
    parser = argparse.ArgumentParser(description="Convert an image to ASCII art")
    parser.add_argument("input_image", help="Path to the input image file")
    parser.add_argument("-o", "--output", help="Optional path to write the ASCII art text")
    parser.add_argument("-w", "--width", type=int, default=80, help="Output width in characters")
    parser.add_argument(
        "--rotate",
        type=int,
        default=0,
        choices=[0, 90, 180, -90],
        help="Rotate the output by 0, 90, 180, or -90 degrees",
    )
    parser.add_argument("--show", action="store_true", help="Print the ASCII art to the terminal")
    return parser


def main() -> int:
    """Run the CLI and return an exit code."""
    args = build_parser().parse_args()

    try:
        ascii_art = image_to_ascii(args.input_image, width=args.width, rotate=args.rotate)
    except FileNotFoundError:
        print(f"Error: file not found: {args.input_image}", file=sys.stderr)
        return 1
    except UnidentifiedImageError:
        print(f"Error: unsupported or invalid image file: {args.input_image}", file=sys.stderr)
        return 1
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    if args.output:
        Path(args.output).write_text(ascii_art, encoding="utf-8")
    if args.show or not args.output:
        print(ascii_art)

    return 0


if __name__ == "__main__":
    sys.exit(main())
