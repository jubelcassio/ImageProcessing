import argparse
import os
from PIL import Image
from actions import supported_formats

def resize(path, size):
    new_image_path = "{}.resized.{}".format(path[:-4], path[-3:])
    im = Image.open(path)

    if im.size == size:
        print("{} is already of size {}".format(path, size))
    else:
        resized_im = im.resize(size)
        resized_im.save(new_image_path)
        print("{} saved successfully.".format(new_image_path))


def call_resize(pos_args):
    ## Parse the inputs
    parser = argparse.ArgumentParser(prog="resize")

    parser.add_argument('path', type=str)
    parser.add_argument('width', type=int)
    parser.add_argument('height', type=int)

    args = parser.parse_args(pos_args)

    path, size = args.path, (args.width, args.height)


    ## Resize single file
    if os.path.isfile(path):
        if path[-3:] not in supported_formats:
            print("{} does not have a supported file type.".format(path))
        else:
            resize(path, size)


    ## Resize files in directory
    elif os.path.isdir(path):
        file_list = os.listdir(path)

        for file_ in file_list:
            f_path = os.path.join(path, file_)
            f_type = file_[-3:]
            if f_type in supported_formats:
                resize(f_path, size)

    else:
        msg = "{} is not a valid file path or directory."
        print(msg.format(path))
