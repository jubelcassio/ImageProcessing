import argparse
import os
from actions import supported_formats
from actions import all_modes
import util


def run(path, filetype, mode):
    # TODO Fix mode conversion
    im = util.open_image(path)
    if im is not None:
        util.save_image(im, path, filetype, mode, "converted")


def parse(user_args):
    ## Parse the inputs
    parser = argparse.ArgumentParser(prog="convert")

    parser.add_argument('filetype', type=str, choices=supported_formats)
    parser.add_argument('--mode', type=str, choices=all_modes, default=None)

    return vars(parser.parse_args(user_args))
