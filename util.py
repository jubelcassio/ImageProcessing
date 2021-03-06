import os
from actions import supported_formats
from actions import supported_modes
from PIL import Image, ImageColor
import re
import argparse


def coordinates_type(xy):
    ## Checks if xy can be turned into a coordinate tuple (int, int)
    xy = xy.split(',')

    if len(xy) != 2:
        msg = ("The coordinates {} must have 2 values (x,y)".format(xy))
        raise argparse.ArgumentTypeError(msg)
    
    try:
        xy = int(xy[0]), int(xy[1])
    except ValueError:
        msg = ("The coordinates {} must be 2 integers (x,y)".format(xy))
        raise argparse.ArgumentTypeError(msg)
    
    if xy[0] < 0 or xy[1] < 0:
        msg = ("The coordinates {} must positive".format(xy))
        raise argparse.ArgumentTypeError(msg)
    
    return xy


def rectangular_box_type(box):
    ## Checks if size can be turned into a tuple of four integer values greater
    # than 1
    box = box.split(',')

    if len(box) != 4:
        msg = ("The box {} must have 4 values (left,upper,right,lower)".format(box))
        raise argparse.ArgumentTypeError(msg)

    if all([n.isdigit() for n in box]):
        # Values must be integers
        box = tuple( [int(n) for n in box] )
    else:
        msg = ("{} values must be integer numbers".format(box))
        raise argparse.ArgumentTypeError(msg)

    if any([coord < 0 for coord in box]):
        # Values must not negative
        msg = ("{} values must be positive numbers".format(box))
        raise argparse.ArgumentTypeError(msg)

    if box[0] >= box[2]:
        msg = ("(left, upper, right, lower)={} LEFT must be smaller than RIGHT.".format(box))
        raise argparse.ArgumentTypeError(msg)

    if box[1] >= box[3]:
        msg = ("(left, upper, right, lower)={} UPPER must be smaller than LOWER.".format(box))
        raise argparse.ArgumentTypeError(msg)
    
    return box


def rgb_color_type(color):

    if color.startswith("#"):
        if re.match("^#(([0-9a-fA-F]{2}){3,4}|([0-9a-fA-F]){3})$", color):
            return ImageColor.getrgb(color)
        else:
            msg = "{} is not a valid hex color code.".format(color)
            raise argparse.ArgumentTypeError(msg)

    color = color.split(',')

    if len(color) < 3 or len(color) > 4:
        # Must be a 3 or 4 length tuple
        msg = "{} must have 3 or 4 values.".format(color)
        raise argparse.ArgumentTypeError(msg)
    elif not all([c.isdigit() for c in color]):
        # All values must be integers
        msg = "{} values must be integers.".format(color)
        raise argparse.ArgumentTypeError(msg)
    elif not all([0 <= int(c) <= 255 for c in color]):
        # All values must in positive 8 bit range
        msg = "{} values must be between 0 and 255".format(color)
        raise argparse.ArgumentTypeError(msg)
    else:
        return tuple(int(c) for c in color)


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


def validate_mode(im, user_mode, save_as):
    # User has given a mode
    if user_mode:
        if user_mode in supported_modes[save_as.lower()]:
            return user_mode
        else:
            # User has given a mode, but it is NOT valid
            print("{} mode is not compatible with {} files".format(user_mode,
                                                                   save_as))
            print("Aborting")
            return

    else:
        if im.mode in supported_modes[save_as.lower()]:
            return im.mode
        else:
            # Original image's mode is not valid, use one of modes supported
            # by the saving format
            print("{} mode is not compatible with {} files".format(im.mode,
                                                                   save_as))
            mode = supported_modes[save_as][-1]
            print("Saving {} image as {} mode...".format(im.mode, mode))
            return mode


def replace_alpha(im, bg_color):
    # Replaces the alpha channel of the given image with the given color
    alpha = im.getchannel('A')
    bg = Image.new("RGBA", im.size, bg_color)
    bg.paste(im, mask=alpha)
    return bg


def optimize_img(im, save_as, mode):
    if save_as.lower() == "jpg":
        im = im.convert(mode)
        save_params = {"quality": 85, "optimize":True}
        return (im, save_params)

    elif save_as.lower() == "png":
        im = im.convert("P", palette=Image.ADAPTIVE)
        save_params = {"optimize":True}
        return (im, save_params)

    else:
        msg = "Error! Can only optimize when saving as jpg or png."
        print(msg)
        return



def validate_save_folder(save_folder, path):
    if save_folder:
        if os.path.isdir(save_folder):
            folder = os.path.abspath(save_folder)
        else:
            print("{} is not a valid directory.".format(save_folder))
            return
    else:
        # Save folder was not given by the user
        folder = os.path.abspath(os.path.dirname(path))

    return folder


def validate_save_format(save_as, extension):
    # Removing the 'dot' at the start
    if extension.startswith("."):
        extension = extension[1:]

    if save_as == None:
        if extension in supported_formats:
            return extension
        else:
            print("{} is not a supported image type.".format(extension))
    elif save_as in supported_formats:
        return save_as
    else:
        print("{} is not a supported image type.".format(save_as))



def save_image(im, path, save_folder, save_as, mode, string="processed",
               optimize=False, background=None):

    ## Validate save folder
    folder = validate_save_folder(save_folder, path)

    ## Extract name and extension of source file
    name, extension = os.path.splitext(os.path.basename(path))

    save_as = validate_save_format(save_as, extension)
    mode = validate_mode(im, mode, save_as)

    ## If an image with alpha channel is going to be converted to a image mode
    # with no alpha channel, we replace the alpha channel with a solid color.
    if im.mode.endswith("A") and not mode.endswith("A"):
        im = replace_alpha(im, background)

    # Optimize image, if needed.
    if optimize:
        im, save_params = optimize_img(im, save_as, mode)
    else:
        save_params = {}
        im = im.convert(mode)

    # New name, so the original image isn't overwritten
    new_image_name = "{}.{}.{}".format(name, string, save_as)
    new_image_path = os.path.join(folder, new_image_name)
    im.save(new_image_path, **save_params)
    print("{} saved successfully.".format(new_image_path))
