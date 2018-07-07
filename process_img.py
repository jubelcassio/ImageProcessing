'''
General use scripts for image processing.

Usage:
    python process_img.py [action] [arguments]

Available actions:
    * convert: Converts image(s) to given format.
        python process_img.py convert [file/directory] [format to convert]
    * resize: Resizes image(s) to given width and height.
        python process_img.py resize [file/directory] [width] [height]
    * scale: Scale image(s) by given scalar.
        python process_img.py scale [file/directory] [scalar]
    * fit: Resize an image to a given width / height while maintaining its
            aspect ratio, offset area is transparent or filled with a white
            background.
        python process_img.py fit [file/directory] [width] [height]
'''


import sys
import os
from PIL import Image
import argparse

supported_formats = ["bmp","eps","gif","ico","jpg","jpeg","png","tiff","webp"]
actions = ['convert', 'resize', 'scale', 'fit']


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
    parser = argparse.ArgumentParser(prog="resize")

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


def fit(path, size):
    f_type = path[-3:]
    new_image_path = "{}.fit_{}_{}.{}".format(path[:-4], size[0], size[1], f_type)
    im = Image.open(path)
    new_im = Image.new(im.mode, size)

    im_ratio = im.width / im.height
    new_im_ratio = new_im.width / new_im.height

    # Both images have the same aspect ratio
    if im_ratio == new_im_ratio:
        resized_im = im.resize((new_im.width, new_im.height))
        topleft = (0, 0)
    # im has to fit on new_im's height
    if im_ratio < new_im_ratio:
        width = round((new_im.height / im.height) * im.width)
        height = new_im.height
        resized_im = im.resize((width, height))
        topleft = ((new_im.width - width) // 2, 0)
    # im has to fit on new_im's width
    if im_ratio > new_im_ratio:
        width = new_im.width
        height = round((new_im.width / im.width) * im.height)
        topleft = (0, (new_im.height - height) // 2)
        resized_im = im.resize((width, height))

    new_im.paste(resized_im, box=topleft)
    new_im.save(new_image_path)
    print("{} saved successfully.".format(new_image_path))


def call_fit(pos_args):
    ## Parse the inputs
    parser = argparse.ArgumentParser(prog="fit")

    parser.add_argument('path', type=str)
    parser.add_argument('width', type=int)
    parser.add_argument('height', type=int)

    args = parser.parse_args(pos_args)

    path, size = args.path, (args.width, args.height)


    ## Fit single file
    if os.path.isfile(path):
        if path[-3:] not in supported_formats:
            print("{} does not have a supported file type.".format(path))
        else:
            fit(path, size)


    ## Fit files in directory
    elif os.path.isdir(path):
        file_list = os.listdir(path)

        for file_ in file_list:
            f_path = os.path.join(path, file_)
            f_type = file_[-3:]
            if f_type in supported_formats:
                fit(f_path, size)

    else:
        msg = "{} is not a valid file path or directory."
        print(msg.format(path))



if __name__ == '__main__':
    action = sys.argv[1]

    if action == "convert":
        call_convert(sys.argv[2:])
    if action == "resize":
        call_resize(sys.argv[2:])
    if action == "scale":
        call_scale(sys.argv[2:])
    if action == "fit":
        call_fit(sys.argv[2:])
    else:
        print("Invalid action: '{}', choose from: {}".format(action, actions))
