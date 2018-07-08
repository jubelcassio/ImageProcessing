import argparse
import os
from PIL import Image
from actions import supported_formats

def run(path, filetype):
    if path[-3:] not in supported_formats:
        print("{} does not have a supported file type.".format(path))
    elif path[-3:] == filetype:
        print("{} is already of type {}".format(path, filetype))
    else:
        new_image_path = "{}.converted.{}".format(path[:-4], filetype)
        im = Image.open(path)
        im.save(new_image_path)
        print("{} saved successfully.".format(new_image_path))

def parse(user_args):
    ## Parse the inputs
    parser = argparse.ArgumentParser(prog="convert")

    parser.add_argument('filetype', type=str, choices=supported_formats)

    return vars(parser.parse_args(user_args))
