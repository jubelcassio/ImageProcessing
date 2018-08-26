from actions import all_modes
from actions import help_dict
from actions import supported_formats
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
    my_help = help_dict["modules"]["dessaturate"]
    dessaturate_parser = subparser.add_parser("dessaturate", help=my_help["general"])

    ## This is used to identify which command is being run
    dessaturate_parser.set_defaults(command="dessaturate")

    dessaturate_parser.add_argument('path', help=my_help["path"])
    dessaturate_parser.add_argument('--save_folder', type=str, default=None,
                               help=my_help["--save_folder"])
    dessaturate_parser.add_argument('--save_as', type=str, choices=supported_formats,
                               default=None, help=my_help["--save_as"])
    dessaturate_parser.add_argument('--mode', type=str, choices=all_modes,
                               default=None, help=my_help["--mode"])
    dessaturate_parser.add_argument('--background', type=util.rgb_color_type,
                               default="#fff", help=my_help["--background"])
    dessaturate_parser.add_argument('-optimize', action="store_true",
                               help=my_help["-optimize"])


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