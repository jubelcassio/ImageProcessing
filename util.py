import os
from actions import supported_formats
from actions import supported_modes
from PIL import Image


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
               optimize=False):
    if save_folder:
        folder = os.path.abspath(os.path.dirname(save_folder))
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
