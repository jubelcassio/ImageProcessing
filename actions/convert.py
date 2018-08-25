import argparse
import os
from actions import supported_formats
from actions import all_modes
import util


def subparser(subparser):
    convert_parser = subparser.add_parser("convert")
    convert_parser.set_defaults(command="convert")

    convert_parser.add_argument('path')
    convert_parser.add_argument('save_as', type=str, choices=supported_formats)
    convert_parser.add_argument('--save_folder', type=str, default=None)
    convert_parser.add_argument('--mode', type=str, choices=all_modes,
                                default=None)
    convert_parser.add_argument('--background', type=util.rgb_color_type,
                                default="#fff")
    convert_parser.add_argument('-optimize', action="store_true")


def run(path, namespace):
    im = util.open_image(path)
    if im is not None:
        util.save_image(im, path, namespace.save_folder, namespace.save_as,
                        namespace.mode, "converted", namespace.optimize,
                        namespace.background)
