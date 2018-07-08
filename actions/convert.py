import argparse
import os
from PIL import Image
from actions import supported_formats

def convert(path, filetype):
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

    parser.add_argument('path', type=str)
    parser.add_argument('filetype', type=str, choices=supported_formats)

    args = parser.parse_args(user_args)
    return (args.path, args.filetype)


def call_convert(user_args):
    path, filetype = parse(user_args)

    ## Convert single file
    if os.path.isfile(path):
        convert(path, filetype)

    ## Convert files in directory
    elif os.path.isdir(path):
        file_list = os.listdir(path)
        for file_ in file_list:
            f_path = os.path.join(path, file_)
            if os.path.isfile(f_path):
                convert(f_path, filetype)

    else:
        msg = "{} is not a valid file path or directory."
        print(msg.format(path))
