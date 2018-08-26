from actions import supported_formats
from actions import all_modes
import argparse
import util

def dessaturate(im):
    if im.mode == "RGBA":
        return im.convert("LA")

    elif im.mode == "L":
        return im

    else:
        return im.convert("L")


def subparser(subparser):
    dessaturate_parser = subparser.add_parser("dessaturate")
    dessaturate_parser.set_defaults(command="dessaturate")

    dessaturate_parser.add_argument('path')
    dessaturate_parser.add_argument('--save_folder', type=str, default=None)
    dessaturate_parser.add_argument('--save_as', type=str, choices=supported_formats,
                                    default=None)
    dessaturate_parser.add_argument('--mode', type=str, choices=all_modes, default=None)
    dessaturate_parser.add_argument('--background', type=util.rgb_color_type,
                                    default="#fff")
    dessaturate_parser.add_argument('-optimize', action="store_true")


def run(path, namespace):
    ## NOTE: By default, the image is grayscaled and saved as the original.
    # image's mode. To save as 'L' or 'LA' the user must pass them explicitily
    # with 'mode' optional argument.
    im = util.open_image(path)
    if im is not None:
        dessaturated_im = dessaturate(im)
        if dessaturated_im is None:
            return
        util.save_image(dessaturated_im, path, namespace.save_folder,
                        namespace.save_as, namespace.mode, "dessaturated",
                        namespace.optimize, namespace.background)