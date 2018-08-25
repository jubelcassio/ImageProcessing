import argparse
from argparse import ArgumentTypeError
import os
from actions import supported_formats
from actions import all_modes
from PIL import Image
import util


def subparser(subparser):
    optimize_parser = subparser.add_parser("optimize")
    optimize_parser.set_defaults(command="optimize")
    optimize_parser.add_argument('path')
    optimize_parser.add_argument('--save_as', type=str, choices=supported_formats)
    optimize_parser.add_argument('--save_folder', type=str, default=None)
    optimize_parser.add_argument('--mode', type=str, choices=all_modes, default=None)
    optimize_parser.add_argument('--background', type=util.rgb_color_type,
                                 default="#fff")

def run(path, namespace):
    im = util.open_image(path)
    if im is not None:
        util.save_image(im, path, namespace.save_folder, namespace.save_as,
                        namespace.mode, "optimized", optimize=True,
                        background=namespace.background)

