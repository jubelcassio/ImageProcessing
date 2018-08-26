import argparse
from argparse import ArgumentTypeError
import os
from actions import all_modes
from actions import help_dict
from actions import supported_formats
from PIL import Image
import util


def subparser(subparser):
    my_help = help_dict["modules"]["optimize"]

    optimize_parser = subparser.add_parser("optimize", help=my_help["general"])

    ## This is used to identify which command is being run
    optimize_parser.set_defaults(command="optimize")

    optimize_parser.add_argument('path', help=my_help["path"])
    optimize_parser.add_argument('--save_folder', type=str, default=None,
                               help=my_help["--save_folder"])
    optimize_parser.add_argument('--save_as', type=str, choices=supported_formats,
                               default=None, help=my_help["--save_as"])
    optimize_parser.add_argument('--mode', type=str, choices=all_modes,
                               default=None, help=my_help["--mode"])
    optimize_parser.add_argument('--background', type=util.rgb_color_type,
                               default="#fff", help=my_help["--background"])

def run(path, namespace):
    im = util.open_image(path)
    if im is not None:
        util.save_image(im, path, namespace.save_folder, namespace.save_as,
                        namespace.mode, "optimized", optimize=True,
                        background=namespace.background)

