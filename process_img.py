import sys
import os
from PIL import Image
import argparse

supported_formats = ["bmp","eps","gif","ico","jpg","jpeg","png","tiff","webp"]
actions = ['convert', 'resize']

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


if __name__ == '__main__':
    '''
    python process_img.py [action] [arguments]
    '''
    action = sys.argv[1]

    if action == "convert":
        call_convert(sys.argv[2:])
    if action == "resize":
        call_resize(sys.argv[2:])
    else:
        print("Invalid action: '{}', choose from: {}".format(action, actions))
