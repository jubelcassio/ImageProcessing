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
    return im

def scale(im, scalar):
    # Minimum width/height is 1 pixel.
    size = (max([1, round(im.size[0] * scalar)]),
            max([1, round(im.size[1] * scalar)]))

    return im.resize(size)

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
    new_image_path = "{}.scaled.{}".format(name, save_as)

    im.save(new_image_path)
    print("{} saved successfully.".format(new_image_path))


def run(path, scalar, save_as):
    im = open_image(path)
    if im is not None:
        resized_im = scale(im, scalar)
        save_image(resized_im, path, save_as)


def parse(user_args):
    ## Parse the inputs
    parser = argparse.ArgumentParser(prog="scale")

    parser.add_argument('scalar', type=float)
    parser.add_argument('--save_as', type=str, choices=supported_formats,
                        default=None)

    return vars(parser.parse_args(user_args))
