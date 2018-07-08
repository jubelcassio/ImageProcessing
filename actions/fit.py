import argparse
import os
from PIL import Image, ImageColor
from actions import supported_formats
import re

def hex_code(string):
    # Validator for hexadecimal colors.
    if re.match("^#(?:[0-9a-fA-F]{3}){1,2}$", string) is None:
        msg = "{} is not a valid hex code.".format(string)
        raise argparse.ArgumentTypeError(msg)
    return string

def eight_bit(n):
    try:
        n = int(n)
    except:
        msg = "alpha value {} must be a integer between 0 and 255".format(n)
        raise argparse.ArgumentTypeError(msg)
    if not (0 <= n & n < 256):
        msg = "alpha value {} must be between 0 and 255".format(n)
        raise argparse.ArgumentTypeError(msg)
    return n


def run(path, width, height, color, alpha):
    if path[-3:] not in supported_formats:
        print("{} does not have a supported file type.".format(path))
        return

    f_type = path[-3:]
    new_image_path = "{}.fit_{}_{}.{}".format(path[:-4], width, height, f_type)
    im = Image.open(path)
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
        width = round((new_im.height / im.height) * im.width)
        height = new_im.height
        resized_im = im.resize((width, height))
        topleft = ((new_im.width - width) // 2, 0)
    # im has to fit on new_im's width
    if im_ratio > new_im_ratio:
        width = new_im.width
        height = round((new_im.width / im.width) * im.height)
        topleft = (0, (new_im.height - height) // 2)
        resized_im = im.resize((width, height))

    new_im.paste(resized_im, box=topleft)
    new_im.save(new_image_path)
    print("{} saved successfully.".format(new_image_path))


def parse(user_args):
    ## Parse the inputs
    parser = argparse.ArgumentParser(prog="fit")

    parser.add_argument('width', type=int)
    parser.add_argument('height', type=int)
    parser.add_argument('-c', '--color', type=hex_code, default="#fff")
    parser.add_argument('-a', '--alpha', type=eight_bit, default=255)
    args = parser.parse_args(user_args)

    return vars(args)
