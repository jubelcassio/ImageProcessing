import argparse
import os
from actions import all_modes
from actions import help_dict
from actions import resampling_filters
from actions import supported_formats
import util


def resize(im, width, height, resample):
    if width < 1: width = 1
    if height < 1: height = 1

    # In case the user hasn't given a resample filter, use NEAREST
    if resample is None:
        resample_filter = 0
    else:
        resample_filter = resampling_filters.index(resample)

    return im.resize((width, height), resample_filter)


# def run(path, width, height, save_folder, save_as, mode, resample, optimize,
#         background):
def run(path, namespace):

    im = util.open_image(path)
    if im is not None:
        resized_image = resize(im, namespace.width, namespace.height,
                               namespace.resample)
        util.save_image(resized_image, path, namespace.save_folder,
                        namespace.save_as, namespace.mode, "resized",
                        namespace.optimize, namespace.background)


def subparser(subparser):
    my_help = help_dict["modules"]["resize"]
    resize_parser = subparser.add_parser("resize", help=my_help["general"])

    ## This is used to identify which command is being run
    resize_parser.set_defaults(command="resize")

    resize_parser.add_argument('path', help=my_help["path"])
    resize_parser.add_argument('width', type=int, help=my_help["width"])
    resize_parser.add_argument('height', type=int, help=my_help["width"])
    resize_parser.add_argument('--save_folder', type=str, default=None,
                               help=my_help["--save_folder"])
    resize_parser.add_argument('--save_as', type=str, choices=supported_formats,
                               default=None, help=my_help["--save_as"])
    resize_parser.add_argument('--mode', type=str, choices=all_modes,
                               default=None, help=my_help["--mode"])
    resize_parser.add_argument('--background', type=util.rgb_color_type,
                               default="#fff", help=my_help["--background"])
    resize_parser.add_argument('-optimize', action="store_true",
                               help=my_help["-optimize"])
    resize_parser.add_argument('--resample', type=str, choices=resampling_filters,
                               default=None, help=my_help["--resample"])
