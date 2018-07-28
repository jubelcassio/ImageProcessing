import argparse
from argparse import ArgumentTypeError
import os
from actions import supported_formats
from actions import all_modes
from PIL import Image
import util


def run(path, save_as, save_folder, mode, background):
    im = util.open_image(path)
    if im is not None:
        util.save_image(im, path, save_folder, save_as, mode, "optimized",
                        optimize=True, background=background)

def parse(user_args):
    ## Parse the inputs
    parser = argparse.ArgumentParser(prog="optimize")

    parser.add_argument('--save_as', type=str, choices=supported_formats)
    parser.add_argument('--save_folder', type=str, default=None)
    parser.add_argument('--mode', type=str, choices=all_modes, default=None)
    parser.add_argument('--background', type=util.rgb_color_type,
                        default="#fff")

    return vars(parser.parse_args(user_args))
