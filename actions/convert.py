import argparse
import os
from actions import supported_formats
from actions import all_modes
import util


def run(path, save_as, save_folder, mode, optimize, background):
    im = util.open_image(path)
    if im is not None:
        util.save_image(im, path, save_folder, save_as, mode, "converted",
                        optimize, background)


def parse(user_args):
    ## Parse the inputs
    parser = argparse.ArgumentParser(prog="convert")

    parser.add_argument('save_as', type=str, choices=supported_formats)
    parser.add_argument('--save_folder', type=str, default=None)
    parser.add_argument('--mode', type=str, choices=all_modes, default=None)
    parser.add_argument('--background', type=util.rgb_color_type,
                        default="#fff")
    parser.add_argument('-optimize', action="store_true")

    return vars(parser.parse_args(user_args))
