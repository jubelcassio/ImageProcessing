import argparse
import os
from PIL import Image
from actions import supported_formats
from actions import supported_modes

def run(path, filetype):
    if path[-3:] not in supported_formats:
        print("{} does not have a supported file type.".format(path))
    elif path[-3:] == filetype:
        print("{} is already of type {}".format(path, filetype))
    else:
        new_image_path = "{}.converted.{}".format(path[:-4], filetype)
        im = Image.open(path)
        if im.mode in supported_modes[filetype]:
            new_im = im
        else:
            new_mode = supported_modes[filetype][-1]
            new_im = im.convert(new_mode)
            print("Converting {} to {} image...".format(im.mode, new_mode))
        new_im.save(new_image_path)
        print("{} saved successfully.".format(new_image_path))

def parse(user_args):
    ## Parse the inputs
    parser = argparse.ArgumentParser(prog="convert")

    parser.add_argument('filetype', type=str, choices=supported_formats)

    return vars(parser.parse_args(user_args))
