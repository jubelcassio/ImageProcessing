import argparse
from argparse import ArgumentTypeError
import os
from actions import supported_formats
from actions import all_modes
from PIL import Image
import util


def run(path, save_as, save_folder, mode):
    im = util.open_image(path)
    if im is not None:
        util.save_image(im, path, save_folder, save_as, mode, "optimized",
                        optimize=True)

def parse(user_args):
    ## Parse the inputs
    parser = argparse.ArgumentParser(prog="optimize")

    parser.add_argument('--save_as', type=str, choices=supported_formats)
    parser.add_argument('--save_folder', type=str, default=None)
    parser.add_argument('--mode', type=str, choices=all_modes, default=None)

    return vars(parser.parse_args(user_args))
