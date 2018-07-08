import argparse
import os
from PIL import Image
from actions import supported_formats

def resize(path, size):
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

    parser.add_argument('path', type=str)
    parser.add_argument('width', type=int)
    parser.add_argument('height', type=int)

    args = parser.parse_args(user_args)

    return args.path, (args.width, args.height)


def call_resize(user_args):
    path, size = parse(user_args)

    ## Resize single file
    if os.path.isfile(path):
        resize(path, size)


    ## Resize files in directory
    elif os.path.isdir(path):
        file_list = os.listdir(path)

        for file_ in file_list:
            f_path = os.path.join(path, file_)
            if os.path.isfile(f_path):
                resize(f_path, size)

    else:
        msg = "{} is not a valid file path or directory."
        print(msg.format(path))
