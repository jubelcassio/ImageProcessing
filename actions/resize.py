import argparse
import os
from actions import supported_formats
from actions import all_modes
from actions import resampling_filters
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


def run(path, width, height, save_folder, save_as, mode, resample, optimize,
        background):
    im = util.open_image(path)
    if im is not None:
        resized_image = resize(im, width, height, resample)
        util.save_image(resized_image, path, save_folder, save_as, mode,
                        "resized", optimize, background)

def parse(user_args):
    ## Parse the inputs
    parser = argparse.ArgumentParser(prog="resize")

    parser.add_argument('width', type=int)
    parser.add_argument('height', type=int)
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
