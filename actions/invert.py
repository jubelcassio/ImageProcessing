from PIL import Image, ImageOps
from actions import all_modes
from actions import help_dict
from actions import supported_formats
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
    my_help = help_dict["modules"]["invert"]
    invert_parser = subparser.add_parser("invert", help=my_help["general"])

    ## This is used to identify which command is being run
    invert_parser.set_defaults(command="invert")

    invert_parser.add_argument('path', help=my_help["path"])
    invert_parser.add_argument('--save_folder', type=str, default=None,
                               help=my_help["--save_folder"])
    invert_parser.add_argument('--save_as', type=str, choices=supported_formats,
                               default=None, help=my_help["--save_as"])
    invert_parser.add_argument('--mode', type=str, choices=all_modes,
                               default=None, help=my_help["--mode"])
    invert_parser.add_argument('--background', type=util.rgb_color_type,
                               default="#fff", help=my_help["--background"])
    invert_parser.add_argument('-optimize', action="store_true",
                               help=my_help["-optimize"])


def run(path, namespace):
    im = util.open_image(path)
    if im is not None:
        inverted_im = invert(im)
        if inverted_im is None:
            return
        util.save_image(inverted_im, namespace.path, namespace.save_folder,
                        namespace.save_as, namespace.mode,
                        "inverted", namespace.optimize, namespace.background)
