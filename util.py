import os
from actions import supported_formats
from actions import supported_modes
from PIL import Image


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


def save_image(im, path, save_as, mode, string="processed"):
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

    if mode != im.mode:
        im = im.convert(mode)

    # New name, so the original image isn't overwritten
    new_image_path = "{}.{}.{}".format(name, string, save_as)

    im.save(new_image_path)
    print("{} saved successfully.".format(new_image_path))
