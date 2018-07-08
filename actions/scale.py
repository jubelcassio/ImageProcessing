import argparse
import os
from PIL import Image
from actions import supported_formats


def run(path, scalar):
    if path[-3:] not in supported_formats:
        print("{} does not have a supported file type.".format(path))
        return

    new_image_path = "{}.scaled.{}".format(path[:-4], path[-3:])
    im = Image.open(path)

    # Minimum width/height is 1 pixel.
    size = (max([1, round(im.size[0] * scalar)]),
            max([1, round(im.size[1] * scalar)]))

    resized_im = im.resize(size)
    resized_im.save(new_image_path)
    print("{} saved successfully.".format(new_image_path))


def parse(user_args):
    ## Parse the inputs
    parser = argparse.ArgumentParser(prog="scale")

    parser.add_argument('scalar', type=float)

    return vars(parser.parse_args(user_args))
