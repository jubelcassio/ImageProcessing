import argparse
import os
from PIL import Image, ImageColor
from actions import supported_formats
from actions import all_modes
from actions import resampling_filters
import re
import util


def is_rgb(color):
    try:
        [int(c) for c in color]
        return True
    except ValueError:
        return False


def rgb_color(color):

    if color.startswith("#"):
        if re.match("^#(([0-9a-fA-F]{2}){3,4}|([0-9a-fA-F]){3})$", color):
            return ImageColor.getrgb(color)
        else:
            msg = "{} is not a valid hex color code.".format(color)
            raise argparse.ArgumentTypeError(msg)

    color = color.split(',')
    if 3 <= len(color) <= 4 and is_rgb(color):
        return tuple(int(c) for c in color)
    else:
        msg = "{} is not a valid rgb color.".format(color)
        raise argparse.ArgumentTypeError(msg)


def fit(im, width, height, color, resample):
    if width < 1: width = 1
    if height < 1: height = 1

    new_im = Image.new(im.mode, (width, height), color=color)

    im_ratio = im.width / im.height
    new_im_ratio = new_im.width / new_im.height

    if resample is None:
        resample_filter = 0
    else:
        resample_filter = resampling_filters.index(resample)

    # Both images have the same aspect ratio
    if im_ratio == new_im_ratio:
        resized_im = im.resize((new_im.width, new_im.height), resample_filter)
        topleft = (0, 0)

    # im has to fit on new_im's height
    if im_ratio < new_im_ratio:
        # Minimum width is 1 pixel.
        width = max([1, round((new_im.height / im.height) * im.width)])
        height = new_im.height
        resized_im = im.resize((width, height), resample_filter)
        topleft = ((new_im.width - width) // 2, 0)

    # im has to fit on new_im's width
    if im_ratio > new_im_ratio:
        width = new_im.width
        # Minimum height is 1 pixel.
        height = max([1, round((new_im.width / im.width) * im.height)])
        topleft = (0, (new_im.height - height) // 2)
        resized_im = im.resize((width, height), resample_filter)

    new_im.paste(resized_im, box=topleft)

    return new_im


def run(path, width, height, color, save_folder, save_as, mode, resample,
        optimize):
    im = util.open_image(path)
    if im is not None:
        fit_image = fit(im, width, height, color, resample)
        util.save_image(fit_image, path, save_folder, save_as, mode, "fit",
                        optimize)


def parse(user_args):
    ## Parse the inputs
    parser = argparse.ArgumentParser(prog="fit")

    parser.add_argument('width', type=int)
    parser.add_argument('height', type=int)
    parser.add_argument('-c', '--color', type=rgb_color, default="#fff")
    parser.add_argument('--save_folder', type=str, default=None)
    parser.add_argument('--save_as', type=str, choices=supported_formats,
                        default=None)
    parser.add_argument('--mode', type=str, choices=all_modes, default=None)
    parser.add_argument('--resample', type=str, choices=resampling_filters,
                        default=None)
    parser.add_argument('-optimize', action="store_true")

    args = parser.parse_args(user_args)

    return vars(args)
