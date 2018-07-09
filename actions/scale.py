import argparse
import os
from PIL import Image
from actions import supported_formats
from actions import supported_modes


def run(path, scalar, save_as):
    extension = os.path.splitext(filename)[1]
    if extension not in supported_formats:
        print("{} does not have a supported file type.".format(path))
        return

    im = Image.open(path)

    if save_as == None:
        save_as = extension
    if im.mode not in supported_modes[save_as]:
        new_mode = supported_modes[save_as][-1]
        im = im.convert(new_mode)
        print("Converting {} to {} image...".format(im.mode, new_mode))

    new_image_path = "{}.scaled.{}".format(path[:-4], save_as)

    # Minimum width/height is 1 pixel.
    size = (max([1, round(im.size[0] * scalar)]),
            max([1, round(im.size[1] * scalar)]))

    resized_im = im.resize(size)
    resized_im.save(new_image_path)
    print("{} saved successfully.".format(new_image_path))


def parse(user_args):
    ## Parse the inputs
    parser = argparse.ArgumentParser(prog="scale")

    parser.add_argument('scalar', type=float)
    parser.add_argument('--save_as', type=str, choices=supported_formats,
                        default=None)

    return vars(parser.parse_args(user_args))
