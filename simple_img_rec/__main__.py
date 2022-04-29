import argparse
import os
from simple_img_rec.simrec import detect_template


def valid_file(parser, choices, fname):
    """function to validate file input

    Args:
        parser (ArgumentParser): ArgumentParser to throw argument error
        choices (tuple[str]): a tuple of file extensions to allow
        fname (str): the file name to validate

    Returns:
        str: the validated file name
    """
    ext = os.path.splitext(fname)[1]
    if ext == '' or ext.lower() not in choices:
        if len(choices) == 1:
            parser.error(f'{fname} doesn\'t end with {choices}')
        else:
            parser.error(f'{fname} doesn\'t end with one of {choices}')
    return fname


def parse_args():
    parser = argparse.ArgumentParser(description='Import STL into Minecraft')
    parser.add_argument(
        'image',
        type=lambda s: valid_file(parser, ('.png', '.jpg'), s),
        help='Image file')
    parser.add_argument(
        'template',
        type=lambda s: valid_file(parser, ('.png', '.jpg'), s),
        help='Template file')
    return parser.parse_args()


def main():
    args = parse_args()
    try:
        (x, y) = detect_template(args.image, args.template)
        print(x, y)
    except TypeError:
        print(f"Template: '{args.template}' not found in image: '{args.image}'")
