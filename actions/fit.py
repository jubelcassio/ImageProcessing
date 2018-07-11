import argparse
import os
from PIL import Image, ImageColor
from actions import supported_formats
from actions import supported_modes
import re

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

def open_image(path):
    extension = os.path.splitext(path)[1][1:]
    if extension not in supported_formats:
        print("{} does not have a supported file type.".format(path))
        return

    try:
        im = Image.open(path)
    except OSError:
        print("{} cannot be identified as an image file.".format(path))
        return
    return im

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

def save_image(im, path, save_as):
    name, extension = os.path.splitext(os.path.basename(path))
    # Removing the 'dot' at the start
    extension = extension[1:]

    if save_as == None:
        save_as = extension

        # Change the image mode, if needed
        if im.mode not in supported_modes[save_as]:
            new_mode = supported_modes[save_as][-1]
            im = im.convert(new_mode)
            print("Converting {} to {} image...".format(im.mode, new_mode))

    # New name, so the original image isn't overwritten
    new_image_path = "{}.fit.{}".format(name, save_as)

    im.save(new_image_path)
    print("{} saved successfully.".format(new_image_path))


def run(path, width, height, color, alpha, save_as):
    im = open_image(path)
    if im is not None:
        fit_image = fit(im, width, height, color, alpha)
        save_image(fit_image, path, save_as)


def parse(user_args):
    ## Parse the inputs
    parser = argparse.ArgumentParser(prog="fit")

    parser.add_argument('width', type=int)
    parser.add_argument('height', type=int)
    parser.add_argument('-c', '--color', type=hex_code, default="#fff")
    parser.add_argument('-a', '--alpha', type=eight_bit, default=255)
    parser.add_argument('--save_as', type=str, choices=supported_formats,
                        default=None)
    args = parser.parse_args(user_args)

    return vars(args)
