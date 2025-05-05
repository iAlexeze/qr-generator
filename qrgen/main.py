import argparse
import os
import qrcode
from PIL import Image
import sys
import logging

def main():
    parser = argparse.ArgumentParser(
        prog="Automated QR Code Generator",
        description="Generate a QR code from a target string or URL.",
        epilog="""Examples:
        qrgen -t "https://www.linkedin.com/in/alexeze" -o myqr --fill-color navy --back-color ivory
        """,
        formatter_class=argparse.MetavarTypeHelpFormatter
    )

    parser.add_argument("-t", "--target", help="Content to encode (or use TARGET env)", type=str)
    parser.add_argument("-o", "--output", help="Output filename (no extension)", type=str)
    parser.add_argument("-f", "--format", help="Image format: PNG (default), JPEG, BMP", type=str.upper, choices=["PNG", "JPEG", "BMP"])
    parser.add_argument("--no-preview", action="store_true", help="Disable automatic image preview")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable debug output")

    # Customization options
    parser.add_argument("--box-size", type=int, default=10, help="Size of each box in pixels (default: 10)")
    parser.add_argument("--border", type=int, default=4, help="Width of the border (default: 4)")
    parser.add_argument("--fill-color", type=str, default="black", help="QR pattern color (default: black)")
    parser.add_argument("--back-color", type=str, default="white", help="Background color (default: white)")

    args = parser.parse_args()

    # Set up logging
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format='%(asctime)s - %(levelname)s: %(message)s'
    )

    target = args.target or os.getenv("TARGET")
    if not target:
        logging.error("No target provided. Use -t or set the TARGET environment variable.")
        sys.exit(1)

    output = args.output or os.getenv("OUTPUT") or "qrcode_output"
    output = os.path.splitext(output)[0]

    image_format = (args.format or os.getenv("FORMAT") or "PNG").upper()

    make_qrcode(
        target, output, image_format,
        box_size=args.box_size,
        border=args.border,
        fill_color=args.fill_color,
        back_color=args.back_color,
        preview=not args.no_preview
    )

def make_qrcode(target, output_filename, image_format, box_size, border, fill_color, back_color, preview=True):
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=box_size,
            border=border
        )
        qr.add_data(target)
        qr.make(fit=True)

        img = qr.make_image(fill_color=fill_color, back_color=back_color).convert('RGB')
        extension = image_format.lower()
        filepath = f"{output_filename}.{extension}"
        img.save(filepath, image_format)
        logging.info(f"QR code saved as '{filepath}'")

        if preview:
            try:
                Image.open(filepath).show()
                logging.debug("Image preview opened.")
            except Exception as e:
                logging.warning(f"Could not open image preview: {e}")

    except Exception as e:
        logging.error(f"Failed to generate or save QR code: {e}")
        sys.exit(1)

def entry_point():
    main()

if __name__ == "__main__":
    main()
