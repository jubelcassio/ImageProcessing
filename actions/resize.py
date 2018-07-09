import argparse
import os
from PIL import Image
from actions import supported_formats
from actions import supported_modes

def run(path, width, height, save_as):
    size = (width, height)
    if path[-3:] not in supported_formats:
        print("{} does not have a supported file type.".format(path))
        return

    im = Image.open(path)

    if save_as == None:
        save_as = path[-3:]
    else:
        if im.mode not in supported_modes[save_as]:
            new_mode = supported_modes[save_as][-1]
            im = im.convert(new_mode)
            print("Converting {} to {} image...".format(im.mode, new_mode))

    new_image_path = "{}.resized.{}".format(path[:-4], save_as)

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
    parser.add_argument('--save_as', type=str, choices=supported_formats,
                        default=None)

    return vars(parser.parse_args(user_args))
