import argparse
import os
from actions import all_modes
from actions import help_dict
from actions import supported_formats
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


def run(path, namespace):
    im = util.open_image(path)
    if im is not None:
        im = swap(im, namespace.before_color, namespace.after_color)
        util.save_image(im, path, namespace.save_folder, namespace.save_as,
                        namespace.mode, "colorswaped", namespace.optimize,
                        namespace.background)


def subparser(subparser):
    my_help = help_dict["modules"]["colorswap"]
    colorswap_parser = subparser.add_parser("colorswap", help=my_help["general"])

    ## This is used to identify which command is being run
    colorswap_parser.set_defaults(command="colorswap")

    colorswap_parser.add_argument('path', help=my_help["path"])
    ## NOTE: When using hex color codes as arguments for before and after
    # colors, use quotes around the color name (Example: "#ff0000ff").
    # Otherwise sys.argv will not read the arguments corretly.
    # I believe the reason is that sys.argv will think everything after the
    # pound sign is a python comment, except if the argument is inside quotes.
    colorswap_parser.add_argument('before_color', type=util.rgb_color_type,
                                  help=my_help["before_color"])
    colorswap_parser.add_argument('after_color', type=util.rgb_color_type,
                                  help=my_help["after_color"])
    colorswap_parser.add_argument('--save_folder', type=str, default=None,
                               help=my_help["--save_folder"])
    colorswap_parser.add_argument('--save_as', type=str, choices=supported_formats,
                               default=None, help=my_help["--save_as"])
    colorswap_parser.add_argument('--mode', type=str, choices=all_modes,
                               default=None, help=my_help["--mode"])
    colorswap_parser.add_argument('--background', type=util.rgb_color_type,
                               default="#fff", help=my_help["--background"])
    colorswap_parser.add_argument('-optimize', action="store_true",
                               help=my_help["-optimize"])
