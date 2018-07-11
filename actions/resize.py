import argparse
import os
from actions import supported_formats
import util


def resize(im, width, height):
    if width < 1: width = 1
    if height < 1: height = 1
    if im.size == (width, height):
        print("{} is already of size {}".format(path, (width, height)))
    else:
        return im.resize((width, height))


def run(path, width, height, save_as):
    im = util.open_image(path)
    if im is not None:
        resized_image = resize(im, width, height)
        util.save_image(resized_image, path, save_as, "resized")

def parse(user_args):
    ## Parse the inputs
    parser = argparse.ArgumentParser(prog="resize")

    parser.add_argument('width', type=int)
    parser.add_argument('height', type=int)
    parser.add_argument('--save_as', type=str, choices=supported_formats,
                        default=None)

    return vars(parser.parse_args(user_args))
