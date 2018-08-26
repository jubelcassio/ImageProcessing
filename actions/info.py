import argparse
import os
import util
from actions import help_dict

def info(im):
    infotext ="\n{}\nformat: {}\nmode: {}\nsize: {}"
    print(infotext.format(im.filename, im.format, im.mode, im.size))


def run(path, namespace):
    im = util.open_image(path)
    if im is not None:
        info(im)

def subparser(subparser):
    my_help = help_dict["modules"]["info"]
    info_parser = subparser.add_parser("info", help=my_help["general"])

    ## This is used to identify which command is being run
    info_parser.set_defaults(command="info")

    info_parser.add_argument('path', help=my_help["path"])