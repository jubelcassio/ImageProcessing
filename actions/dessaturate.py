from actions import supported_formats
from actions import all_modes
import argparse
import util

def dessaturate(im):
    if im.mode == "RGBA":
        return im.convert("LA")

    elif im.mode == "L":
        return im

    else:
        return im.convert("L")


def run(path, save_folder, save_as, mode, optimize):
    im = util.open_image(path)
    if im is not None:
        dessaturated_im = dessaturate(im)
        if dessaturated_im is None:
            return
        util.save_image(dessaturated_im, path, save_folder, save_as, mode,
                        "dessaturated", optimize)


def parse(user_args):
    ## Parse the inputs
    parser = argparse.ArgumentParser(prog="dessaturate")

    parser.add_argument('--save_folder', type=str, default=None)
    parser.add_argument('--save_as', type=str, choices=supported_formats,
                        default=None)
    parser.add_argument('--mode', type=str, choices=all_modes, default=None)
    parser.add_argument('-optimize', action="store_true")

    return vars(parser.parse_args(user_args))