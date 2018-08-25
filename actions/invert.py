from PIL import Image, ImageOps
from actions import supported_formats
from actions import all_modes
import argparse
import util

def invert(im):
    ## ImageOps does not works with transparency, so we have to invert each
    # color channel separately
    if im.mode == "RGBA":
        r, g, b, a = im.split()
        r, g, b = map(ImageOps.invert, (r, g, b))
        return Image.merge(im.mode, (r,g,b,a))
    elif im.mode == "RGB":
        return ImageOps.invert(im)
    else:
        print("Can only invert RGB or RGBA images.")


def subparser(subparser):
    invert_parser = subparser.add_parser("invert")

    invert_parser.set_defaults(command="invert")

    invert_parser.add_argument('path')
    invert_parser.add_argument('--save_folder', type=str, default=None)
    invert_parser.add_argument('--save_as', type=str, choices=supported_formats,
                               default=None)
    invert_parser.add_argument('--mode', type=str, choices=all_modes, default=None)
    invert_parser.add_argument('--background', type=util.rgb_color_type,
                               default="#fff")
    invert_parser.add_argument('-optimize', action="store_true")


def run(path, namespace):
    im = util.open_image(path)
    if im is not None:
        inverted_im = invert(im)
        if inverted_im is None:
            return
        util.save_image(inverted_im, namespace.path, namespace.save_folder,
                        namespace.save_as, namespace.mode,
                        "inverted", namespace.optimize, namespace.background)
