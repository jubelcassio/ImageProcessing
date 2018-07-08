import argparse
import os
from PIL import Image
from actions import supported_formats

def run(path, width, height):
    size = (width, height)
    if path[-3:] not in supported_formats:
        print("{} does not have a supported file type.".format(path))
        return

    new_image_path = "{}.resized.{}".format(path[:-4], path[-3:])
    im = Image.open(path)

    if im.size == size:
        print("{} is already of size {}".format(path, size))
    else:
        resized_im = im.resize(size)
        resized_im.save(new_image_path)
        print("{} saved successfully.".format(new_image_path))

def parse(user_args):
    ## Parse the inputs
    parser = argparse.ArgumentParser(prog="resize")

    parser.add_argument('width', type=int)
    parser.add_argument('height', type=int)

    return vars(parser.parse_args(user_args))
