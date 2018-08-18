import argparse
import os
from actions import supported_formats
from actions import all_modes
import util
from PIL import ImageColor

def swap(image, before_color, after_color):
    ## Iterates over each pixel, if the pixel is from the given "before" color
    # change it to the "after" color.
    ## before_color and after_color must be tuples with the color values.
    pixels_swaped = 0
    pixel_data = image.load()

    for x in range(0, image.size[0]):
        for y in range(0, image.size[1]):
            if pixel_data[x, y] == before_color:
                pixel_data[x, y] = after_color
                pixels_swaped += 1

    print("Swaped {} pixels on the image.".format(pixels_swaped))

    return image


def run(path, before_color, after_color, save_as, save_folder, mode, optimize,
        background):
    im = util.open_image(path)
    if im is not None:
        im = swap(im, before_color, after_color)
        util.save_image(im, path, save_folder, save_as, mode, "colorswaped",
                        optimize, background)


def parse(user_args):
    ## Parse the inputs
    parser = argparse.ArgumentParser(prog="colorswap")

    ## NOTE: When using hex color codes as arguments for before and after
    # colors, use quotes around the color name (Example: "#ff0000ff").
    # Otherwise sys.argv will not read the arguments corretly.
    # I believe the reason is that sys.argv will think everything after the
    # pound sign is a python comment, except if the argument is inside quotes.

    parser.add_argument('before_color', type=util.rgb_color_type)
    parser.add_argument('after_color', type=util.rgb_color_type)
    parser.add_argument('--save_as', type=str, choices=supported_formats)
    parser.add_argument('--save_folder', type=str, default=None)
    parser.add_argument('--mode', type=str, choices=all_modes, default=None)
    parser.add_argument('--background', type=util.rgb_color_type,
                        default="#fff")
    parser.add_argument('-optimize', action="store_true")

    return vars(parser.parse_args(user_args))
