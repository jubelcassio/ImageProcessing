import argparse
from actions import all_modes
from actions import help_dict
from actions import supported_formats
import util
from PIL import ImageOps

mirror_modes = ['v', 'vh', "hv", "h"]

def mirror(im, mirror):
    if "v" in mirror:
        im = ImageOps.mirror(im)
    if "h" in mirror:
        im = ImageOps.flip(im)
    return im

def subparser(subparser):
    my_help = help_dict["modules"]["mirror"]
    mirror_parser = subparser.add_parser("mirror", help=my_help['general'])

    ## This is used to identify which command is being run
    mirror_parser.set_defaults(command="mirror")

    mirror_parser.add_argument('path', help=my_help["path"])
    mirror_parser.add_argument('mirror_mode', type=str, choices=mirror_modes,
                               help=my_help["mirror_mode"])
    mirror_parser.add_argument('--save_folder', type=str, default=None,
                               help=my_help["--save_folder"])
    mirror_parser.add_argument('--save_as', type=str, choices=supported_formats,
                               default=None, help=my_help["--save_as"])
    mirror_parser.add_argument('--mode', type=str, choices=all_modes,
                               default=None, help=my_help["--mode"])
    mirror_parser.add_argument('--background', type=util.rgb_color_type,
                               default="#fff", help=my_help["--background"])
    mirror_parser.add_argument('-optimize', action="store_true",
                               help=my_help["-optimize"])



def run(path, namespace):
    im = util.open_image(path)
    if im is not None:
        mirrored_im = mirror(im, namespace.mirror_mode)
        util.save_image(mirrored_im, namespace.path, namespace.save_folder,
                        namespace.save_as, namespace.mode, "mirrored",
                        namespace.optimize, namespace.background)
