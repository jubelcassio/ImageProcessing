import argparse
import os
import util

def info(im):
    infotext ="\n{}\nformat: {}\nmode: {}\nsize: {}"
    print(infotext.format(im.filename, im.format, im.mode, im.size))


def run(path, namespace):
    im = util.open_image(path)
    if im is not None:
        info(im)

def subparser(subparser):
    info_parser = subparser.add_parser("info")

    info_parser.set_defaults(command="info")

    info_parser.add_argument('path')