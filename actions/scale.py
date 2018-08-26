import argparse
import os
from actions import all_modes
from actions import help_dict
from actions import resampling_filters
from actions import supported_formats
import util


def scale(im, scalar, resample):
    # Minimum width/height is 1 pixel.
    size = (max([1, round(im.size[0] * scalar)]),
    max([1, round(im.size[1] * scalar)]))

    # In case the user hasn't given a resample filter, use NEAREST
    if resample is None:
        resample_filter = 0
    else:
        resample_filter = resampling_filters.index(resample)

    return im.resize(size, resample=resample_filter)


def subparser(subparser):
    my_help = help_dict["modules"]["scale"]
    scale_parser = subparser.add_parser("scale", help=my_help["general"])

    ## This is used to identify which command is being run
    scale_parser.set_defaults(command="scale")

    scale_parser.add_argument('path', help=my_help["path"])
    scale_parser.add_argument('scalar', type=float, help=my_help["scalar"])
    scale_parser.add_argument('--save_folder', type=str, default=None,
                               help=my_help["--save_folder"])
    scale_parser.add_argument('--save_as', type=str, choices=supported_formats,
                               default=None, help=my_help["--save_as"])
    scale_parser.add_argument('--mode', type=str, choices=all_modes,
                               default=None, help=my_help["--mode"])
    scale_parser.add_argument('--background', type=util.rgb_color_type,
                               default="#fff", help=my_help["--background"])
    scale_parser.add_argument('-optimize', action="store_true",
                               help=my_help["-optimize"])
    scale_parser.add_argument('--resample', type=str, choices=resampling_filters,
                               default=None, help=my_help["--resample"])



def run(path, namespace):
    im = util.open_image(path)
    if im is not None:
        scaled_im = scale(im, namespace.scalar, namespace.resample)
        util.save_image(scaled_im, path, namespace.save_folder,
                        namespace.save_as, namespace.mode, "scaled",
                        namespace.optimize, namespace.background)