import argparse
import os
from actions import supported_formats
from actions import all_modes
from actions import resampling_filters
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
    scale_parser = subparser.add_parser("scale")

    scale_parser.set_defaults(command="scale")

    scale_parser.add_argument('path')
    scale_parser.add_argument('scalar', type=float)
    scale_parser.add_argument('--save_folder', type=str, default=None)
    scale_parser.add_argument('--save_as', type=str, choices=supported_formats,
                        default=None)
    scale_parser.add_argument('--mode', type=str, choices=all_modes, default=None)
    scale_parser.add_argument('--background', type=util.rgb_color_type,
                        default="#fff")
    scale_parser.add_argument('--resample', type=str, choices=resampling_filters,
                        default=None)
    scale_parser.add_argument('-optimize', action="store_true")


def run(path, namespace):
    im = util.open_image(path)
    if im is not None:
        scaled_im = scale(im, namespace.scalar, namespace.resample)
        util.save_image(scaled_im, path, namespace.save_folder,
                        namespace.save_as, namespace.mode, "scaled",
                        namespace.optimize, namespace.background)