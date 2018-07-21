from PIL import ImageOps
from actions import supported_formats
from actions import all_modes
import argparse
import util

def invert(im):
    return ImageOps.invert(im)


def run(path, save_folder, save_as, mode, resample, optimize):
    im = util.open_image(path)
    if im is not None:
        inverted_im = invert(im)
        util.save_image(inverted_im, path, save_folder, save_as, mode,
                        "inverted", optimize)


def parse(user_args):
    ## Parse the inputs
    parser = argparse.ArgumentParser(prog="invert")

    parser.add_argument('--save_folder', type=str, default=None)
    parser.add_argument('--save_as', type=str, choices=supported_formats,
                        default=None)
    parser.add_argument('--mode', type=str, choices=all_modes, default=None)
    parser.add_argument('-optimize', action="store_true")

    return vars(parser.parse_args(user_args))
