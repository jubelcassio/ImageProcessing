import argparse
from argparse import ArgumentTypeError
import os
from actions import supported_formats
from actions import all_modes
from PIL import Image
import util


def optimize(im, save_as):
    if save_as == "jpg" or (im.filename.lower().endswith("jpg") and save_as is None):
        params = {"quality": 85, "optimize":True}

    elif save_as == "png" or (im.filename.lower().endswith("png") and save_as is None):
        im = im.convert("P", palette=Image.ADAPTIVE)
        params = {"optimize":True}

    else:
        msg = "Can only optimize when saving as jpg or png."
        raise ArgumentTypeError(msg)
        return

    return (im, params)


def run(path, save_as, save_folder, mode):
    im = util.open_image(path)
    if im is not None:
        im, params = optimize(im, save_as)
        util.save_image(im, path, save_folder, save_as, mode, "optimized",
                        params)

def parse(user_args):
    ## Parse the inputs
    parser = argparse.ArgumentParser(prog="optimize")

    parser.add_argument('--save_as', type=str, choices=supported_formats)
    parser.add_argument('--save_folder', type=str, default=None)
    parser.add_argument('--mode', type=str, choices=all_modes, default=None)

    return vars(parser.parse_args(user_args))
