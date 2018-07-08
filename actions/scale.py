import argparse
import os
from PIL import Image
from actions import supported_formats


def scale(path, scalar):
    new_image_path = "{}.scaled.{}".format(path[:-4], path[-3:])
    im = Image.open(path)

    # Minimum width/height is 1 pixel.
    size = (max([1, round(im.size[0] * scalar)]),
            max([1, round(im.size[1] * scalar)]))

    resized_im = im.resize(size)
    resized_im.save(new_image_path)
    print("{} saved successfully.".format(new_image_path))


def call_scale(pos_args):
    ## Parse the inputs
    parser = argparse.ArgumentParser(prog="scale")

    parser.add_argument('path', type=str)
    parser.add_argument('scalar', type=float)

    args = parser.parse_args(pos_args)

    path, scalar = args.path, args.scalar


    ## Scale single file
    if os.path.isfile(path):
        if path[-3:] not in supported_formats:
            print("{} does not have a supported file type.".format(path))
        else:
            scale(path, scalar)


    ## Scale files in directory
    elif os.path.isdir(path):
        file_list = os.listdir(path)

        for file_ in file_list:
            f_path = os.path.join(path, file_)
            f_type = file_[-3:]
            if f_type in supported_formats:
                scale(f_path, scalar)

    else:
        msg = "{} is not a valid file path or directory."
        print(msg.format(path))
