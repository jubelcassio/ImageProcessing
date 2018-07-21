import argparse
from actions import supported_formats
from actions import all_modes
import util
from PIL import ImageOps

mirror_modes = ['v', 'vh', "hv", "h"]

def mirror(im, mirror):
    if "v" in mirror:
        im = ImageOps.mirror(im)
    if "h" in mirror:
        im = ImageOps.flip(im)
    return im



def run(path, mirror_mode, save_folder, save_as, mode, optimize):
    im = util.open_image(path)
    if im is not None:
        mirrored_im = mirror(im, mirror_mode)
        util.save_image(mirrored_im, path, save_folder, save_as, mode,
                        "mirrored", optimize)

def parse(user_args):
    ## Parse the inputs
    parser = argparse.ArgumentParser(prog="mirror")

    parser.add_argument('mirror_mode', type=str, choices=mirror_modes)
    parser.add_argument('--save_folder', type=str, default=None)
    parser.add_argument('--save_as', type=str, choices=supported_formats,
                        default=None)
    parser.add_argument('--mode', type=str, choices=all_modes, default=None)
    parser.add_argument('-optimize', action="store_true")

    return vars(parser.parse_args(user_args))
