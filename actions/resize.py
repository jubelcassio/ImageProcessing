import argparse
import os
from PIL import Image
from actions import supported_formats
from actions import supported_modes

def open_image(path):
    extension = os.path.splitext(path)[1][1:]
    if extension not in supported_formats:
        print("{} does not have a supported file type.".format(path))
        return

    try:
        im = Image.open(path)
    except OSError:
        print("{} cannot be identified as an image file.".format(path))
        return
    return im

def save_image(im, path, save_as):
    name, extension = os.path.splitext(os.path.basename(path))
    # Removing the 'dot' at the start
    extension = extension[1:]

    if save_as == None:
        save_as = extension

        # Change the image mode, if needed
        if im.mode not in supported_modes[save_as]:
            new_mode = supported_modes[save_as][-1]
            im = im.convert(new_mode)
            print("Converting {} to {} image...".format(im.mode, new_mode))

    # New name, so the original image isn't overwritten
    new_image_path = "{}.resized.{}".format(name, save_as)

    im.save(new_image_path)
    print("{} saved successfully.".format(new_image_path))

def resize(im, width, height):
    if width < 1: width = 1
    if height < 1: height = 1
    if im.size == (width, height):
        print("{} is already of size {}".format(path, (width, height)))
    else:
        return im.resize((width, height))



def run(path, width, height, save_as):
    im = open_image(path)
    if im is not None:
        resized_image = resize(im, width, height)
        save_image(resized_image, path, save_as)

def parse(user_args):
    ## Parse the inputs
    parser = argparse.ArgumentParser(prog="resize")

    parser.add_argument('width', type=int)
    parser.add_argument('height', type=int)
    parser.add_argument('--save_as', type=str, choices=supported_formats,
                        default=None)

    return vars(parser.parse_args(user_args))
