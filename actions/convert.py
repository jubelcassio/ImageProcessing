import argparse
import os
from actions import all_modes
from actions import help_dict
from actions import supported_formats
import util


def subparser(subparser):
    my_help = help_dict["modules"]["convert"]
    convert_parser = subparser.add_parser("convert", help=my_help["general"])

    ## This is used to identify which command is being run
    convert_parser.set_defaults(command="convert")

    convert_parser.add_argument('path', help=my_help["path"])
    convert_parser.add_argument('save_as', type=str, choices=supported_formats,
                                help=my_help["save_as"])
    convert_parser.add_argument('--save_folder', type=str, default=None,
                               help=my_help["--save_folder"])
    convert_parser.add_argument('--mode', type=str, choices=all_modes,
                               default=None, help=my_help["--mode"])
    convert_parser.add_argument('--background', type=util.rgb_color_type,
                               default="#fff", help=my_help["--background"])
    convert_parser.add_argument('-optimize', action="store_true",
                               help=my_help["-optimize"])

def run(path, namespace):
    im = util.open_image(path)
    if im is not None:
        util.save_image(im, path, namespace.save_folder, namespace.save_as,
                        namespace.mode, "converted", namespace.optimize,
                        namespace.background)
