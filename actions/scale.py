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


def run(path, scalar, save_folder, save_as, mode, resample, optimize,
        background):
    im = util.open_image(path)
    if im is not None:
        scaled_im = scale(im, scalar, resample)
        util.save_image(scaled_im, path, save_folder, save_as, mode, "scaled",
                        optimize, background)


def parse(user_args):
    ## Parse the inputs
    parser = argparse.ArgumentParser(prog="scale")

    parser.add_argument('scalar', type=float)
    parser.add_argument('--save_folder', type=str, default=None)
    parser.add_argument('--save_as', type=str, choices=supported_formats,
                        default=None)
    parser.add_argument('--mode', type=str, choices=all_modes, default=None)
    parser.add_argument('--background', type=util.rgb_color_type,
                        default="#fff")
    parser.add_argument('--resample', type=str, choices=resampling_filters,
                        default=None)
    parser.add_argument('-optimize', action="store_true")

    return vars(parser.parse_args(user_args))
