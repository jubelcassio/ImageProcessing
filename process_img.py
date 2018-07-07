import sys
import os
from PIL import Image
import argparse

supported_formats = ["bmp","eps","gif","ico","jpg","jpeg","png","tiff","webp"]
actions = ['convert', 'resize']

def convert(pos_args):
    parser = argparse.ArgumentParser(prog="convert")

    parser.add_argument('path', type=str)
    parser.add_argument('filetype', type=str, choices=supported_formats)

    args = parser.parse_args(pos_args)

    path, filetype = args.path, args.filetype

    if os.path.isfile(path):
        o_type = path[-3:]
        if o_type not in supported_formats:
            print("{} does not have a supported file type.".format(path))
        elif o_type == filetype:
            print("{} is already of type {}".format(path, filetype))
        else:
            new_image_path = "{}.converted.{}".format(path[:-4], filetype)
            im = Image.open(path)
            im.save(new_image_path)
            print("{} saved successfully.".format(new_image_path))

    elif os.path.isdir(path):
        file_list = os.listdir(path)

        for file_ in file_list:
            f_path = os.path.join(path, file_)
            f_type = file_[-3:]
            if f_type == filetype:
                print("{} is already of type {}".format(f_path, filetype))
            elif f_type in supported_formats:
                new_image_path = "{}.converted.{}".format(f_path[:-4], filetype)
                im = Image.open(f_path)
                im.save(new_image_path)
                print("{} saved successfully.".format(new_image_path))

    else:
        msg = "{} is not a valid file path or directory."
        print(msg.format(path))

def resize(pos_args):
    parser = argparse.ArgumentParser(prog="resize")

    parser.add_argument('path', type=str)
    parser.add_argument('width', type=int)
    parser.add_argument('height', type=int)

    args = parser.parse_args(pos_args)

    path, width, height = args.path, args.width, args.height

    if os.path.isfile(path):
        o_type = path[-3:]
        if o_type not in supported_formats:
            print("{} does not have a supported file type.".format(path))
        else:
            new_image_path = "{}.resized.{}".format(path[:-4], o_type)
            im = Image.open(path)
            if im.size == (width, height):
                print("{} is already of size {}".format(path, (width, height)))
            else:
                resized_im = im.resize((width, height))
                resized_im.save(new_image_path)
                print("{} saved successfully.".format(new_image_path))

    elif os.path.isdir(path):
        file_list = os.listdir(path)

        for file_ in file_list:
            f_path = os.path.join(path, file_)
            f_type = file_[-3:]
            if f_type in supported_formats:
                new_image_path = "{}.resized.{}".format(f_path[:-4], f_type)
                im = Image.open(f_path)
                if im.size == (width, height):
                    print("{} is already of size {}".format(f_path, (width, height)))
                else:
                    resized_im = im.resize((width, height))
                    resized_im.save(new_image_path)
                    print("{} saved successfully.".format(new_image_path))

    else:
        msg = "{} is not a valid file path or directory."
        print(msg.format(path))


if __name__ == '__main__':
    '''
    python process_img.py [action] [arguments]
    '''
    action = sys.argv[1]

    if action == "convert":
        convert(sys.argv[2:])
    if action == "resize":
        resize(sys.argv[2:])
    else:
        print("Invalid action: '{}', choose from: {}".format(action, actions))
