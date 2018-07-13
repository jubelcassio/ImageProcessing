import argparse
import os
from actions import supported_formats
from actions import all_modes
import util


def scale(im, scalar):
    # Minimum width/height is 1 pixel.
    size = (max([1, round(im.size[0] * scalar)]),
    max([1, round(im.size[1] * scalar)]))

    return im.resize(size)


def run(path, scalar, save_as, mode):
    im = util.open_image(path)
    if im is not None:
        scaled_im = scale(im, scalar)
        util.save_image(scaled_im, path, save_as, mode, "scaled")


def parse(user_args):
    ## Parse the inputs
    parser = argparse.ArgumentParser(prog="scale")

    parser.add_argument('scalar', type=float)
    parser.add_argument('--save_as', type=str, choices=supported_formats,
                        default=None)
    parser.add_argument('--mode', type=str, choices=all_modes, default=None)

    return vars(parser.parse_args(user_args))
