import argparse
import os
from PIL import Image
from actions import supported_formats


def scale(path, scalar):
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

    parser.add_argument('path', type=str)
    parser.add_argument('scalar', type=float)

    args = parser.parse_args(user_args)

    return args.path, args.scalar


def call_scale(user_args):
    path, scalar = parse(user_args)

    ## Scale single file
    if os.path.isfile(path):
        scale(path, scalar)

    ## Scale files in directory
    elif os.path.isdir(path):
        file_list = os.listdir(path)

        for file_ in file_list:
            f_path = os.path.join(path, file_)
            if os.path.isfile(f_path):
                scale(f_path, scalar)

    else:
        msg = "{} is not a valid file path or directory."
        print(msg.format(path))
