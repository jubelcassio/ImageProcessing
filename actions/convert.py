import argparse
import os
from PIL import Image
from actions import supported_formats
from actions import supported_modes

def run(path, filetype, mode):
    if path[-3:] not in supported_formats:
        print("{} does not have a supported file type.".format(path))
    elif path[-3:] == filetype:
        print("{} is already of type {}".format(path, filetype))
    else:
        new_image_path = "{}.converted.{}".format(path[:-4], filetype)
        im = Image.open(path)

        if mode == None:
            mode = im.mode

        if mode not in supported_modes[filetype]:
            msg = "{} is not supported by the {} image writer."
            print(msg.format(mode, filetype))

            mode = supported_modes[filetype][-1]

        if mode != im.mode:
            print("Converting {} to {} image...".format(im.mode, mode))
            im = im.convert(mode)

        im.save(new_image_path)
        print("{} saved successfully.".format(new_image_path))

def parse(user_args):
    ## Parse the inputs
    parser = argparse.ArgumentParser(prog="convert")

    parser.add_argument('filetype', type=str, choices=supported_formats)
    parser.add_argument('--mode', type=str, default=None)

    return vars(parser.parse_args(user_args))
