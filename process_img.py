import sys
import os
from PIL import Image
import argparse

supported_formats = ["bmp","eps","gif","ico","jpg","jpeg","png","tiff","webp"]
actions = ['convert']

def convert(path, filetype):
    if os.path.isfile(path):
        o_type = path[-3:]
        if o_type == filetype:
            print("{} is already of type {}".format(path, filetype))
        elif o_type in supported_formats:
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



if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('action', type=str, choices=actions)
    parser.add_argument('path', type=str)
    parser.add_argument('filetype', type=str, choices=supported_formats)

    args = parser.parse_args(sys.argv[1:])

    if args.action == "convert":
            convert(args.path, args.filetype)
