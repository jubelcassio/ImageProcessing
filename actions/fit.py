import argparse
import os
from PIL import Image, ImageColor
from actions import supported_formats
from actions import all_modes
import re
import util

def hex_code(string):
    # Validator for hexadecimal colors.
    if re.match("^#(?:[0-9a-fA-F]{3}){1,2}$", string) is None:
        msg = "{} is not a valid hex code.".format(string)
        raise argparse.ArgumentTypeError(msg)
    return string

def eight_bit(n):
    # Asserts n is an integer between 0 and 255
    try:
        n = int(n)
    except:
        msg = "alpha value {} must be a integer between 0 and 255".format(n)
        raise argparse.ArgumentTypeError(msg)
    if not (0 <= n & n < 256):
        msg = "alpha value {} must be between 0 and 255".format(n)
        raise argparse.ArgumentTypeError(msg)
    return n

def fit(im, width, height, color, alpha):
    if width < 1: width = 1
    if height < 1: height = 1


    # background color
    color = (*ImageColor.getrgb(color), alpha)

    new_im = Image.new(im.mode, (width, height), color=color)

    im_ratio = im.width / im.height
    new_im_ratio = new_im.width / new_im.height

    # Both images have the same aspect ratio
    if im_ratio == new_im_ratio:
        resized_im = im.resize((new_im.width, new_im.height))
        topleft = (0, 0)

    # im has to fit on new_im's height
    if im_ratio < new_im_ratio:
        # Minimum width is 1 pixel.
        width = max([1, round((new_im.height / im.height) * im.width)])
        height = new_im.height
        resized_im = im.resize((width, height))
        topleft = ((new_im.width - width) // 2, 0)

    # im has to fit on new_im's width
    if im_ratio > new_im_ratio:
        width = new_im.width
        # Minimum height is 1 pixel.
        height = max([1, round((new_im.width / im.width) * im.height)])
        topleft = (0, (new_im.height - height) // 2)
        resized_im = im.resize((width, height))

    new_im.paste(resized_im, box=topleft)

    return new_im

def run(path, width, height, color, alpha, save_as, mode):
    im = util.open_image(path)
    if im is not None:
        fit_image = fit(im, width, height, color, alpha)
        util.save_image(fit_image, path, save_as, mode, "fit")


def parse(user_args):
    ## Parse the inputs
    parser = argparse.ArgumentParser(prog="fit")

    parser.add_argument('width', type=int)
    parser.add_argument('height', type=int)
    parser.add_argument('-c', '--color', type=hex_code, default="#fff")
    parser.add_argument('-a', '--alpha', type=eight_bit, default=255)
    parser.add_argument('--save_as', type=str, choices=supported_formats,
                        default=None)
    parser.add_argument('--mode', type=str, choices=all_modes, default=None)
    args = parser.parse_args(user_args)

    return vars(args)
