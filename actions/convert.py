import argparse
import os
from PIL import Image
from actions import supported_formats

def convert(path, filetype):
    if path[-3:] == filetype:
        print("{} is already of type {}".format(path, filetype))
    else:
        new_image_path = "{}.converted.{}".format(path[:-4], filetype)
        im = Image.open(path)
        im.save(new_image_path)
        print("{} saved successfully.".format(new_image_path))


def call_convert(pos_args):
    ## Parse the inputs
    parser = argparse.ArgumentParser(prog="convert")

    parser.add_argument('path', type=str)
    parser.add_argument('filetype', type=str, choices=supported_formats)

    args = parser.parse_args(pos_args)

    path, filetype = args.path, args.filetype


    ## Convert single file
    if os.path.isfile(path):
        if path[-3:] not in supported_formats:
            print("{} does not have a supported file type.".format(path))
        else:
            convert(path, filetype)


    ## Convert files in directory
    elif os.path.isdir(path):
        file_list = os.listdir(path)
        for file_ in file_list:
            f_path = os.path.join(path, file_)
            f_type = file_[-3:]
            if f_type in supported_formats:
                convert(f_path, filetype)


    else:
        msg = "{} is not a valid file path or directory."
        print(msg.format(path))
