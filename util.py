import os
from actions import supported_formats
from actions import supported_modes
from PIL import Image, ImageColor
import re

def is_rgb(color):
    try:
        [int(c) for c in color]
        return True
    except ValueError:
        return False


def rgb_color_type(color):

    if color.startswith("#"):
        if re.match("^#(([0-9a-fA-F]{2}){3,4}|([0-9a-fA-F]){3})$", color):
            return ImageColor.getrgb(color)
        else:
            msg = "{} is not a valid hex color code.".format(color)
            raise argparse.ArgumentTypeError(msg)

    color = color.split(',')
    if 3 <= len(color) <= 4 and is_rgb(color):
        return tuple(int(c) for c in color)
    else:
        msg = "{} is not a valid rgb color.".format(color)
        raise argparse.ArgumentTypeError(msg)


def open_image(path):
    path = os.path.realpath(path)
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


def save_image(im, path, save_folder, save_as, mode, string="processed",
               optimize=False, background=None):
    if save_folder:
        if os.path.isdir(save_folder):
            folder = os.path.abspath(save_folder)
        else:
            print("{} is not a valid directory.".format(save_folder))
            return
    else:
        folder = os.path.abspath(os.path.dirname(path))
    name, extension = os.path.splitext(os.path.basename(path))
    # Removing the 'dot' at the start
    extension = extension[1:]

    if save_as == None:
        save_as = extension

    if mode is None:
        # User hasn't given a mode
        mode = im.mode
    elif mode not in supported_modes[save_as]:
        # User has given a mode, but it is not compatible
        print("{} mode is not compatible with {} files".format(mode, save_as))
        print("Aborting")
        return

    if mode not in supported_modes[save_as]:
        # Original image's mode is not compatible
        print("{} mode is not compatible with {} files".format(mode, save_as))
        mode = supported_modes[save_as][-1]
        print("Saving image as {} mode...".format(mode))

    ## If a image with alpha channel is going to be convert to a mode with no
    # alpha channel, we replace the alpha channel with a color.
    if im.mode.endswith("A") and not mode.endswith("A"):
        alpha = im.getchannel('A')
        bg = Image.new("RGBA", im.size, background)
        bg.paste(im, mask=alpha)
        im = bg

    if optimize:
        if save_as.lower() == "jpg":
            im = im.convert(mode)
            params = {"quality": 85, "optimize":True}

        elif save_as.lower() == "png":
            im = im.convert("P", palette=Image.ADAPTIVE)
            params = {"optimize":True}
        else:
            msg = "Error! Can only optimize when saving as jpg or png."
            print(msg)
            return
    else:
        params = {}
        im = im.convert(mode)

    # New name, so the original image isn't overwritten
    new_image_name = "{}.{}.{}".format(name, string, save_as)
    new_image_path = os.path.join(folder, new_image_name)
    im.save(new_image_path, **params)
    print("{} saved successfully.".format(new_image_path))
