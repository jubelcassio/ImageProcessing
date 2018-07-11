import argparse
import os
import util

def info(im):
    infotext ="{}\nformat: {}\nmode: {}\nsize: {}"
    print(infotext.format(im.filename, im.format, im.mode, im.size))


def run(path):
    im = util.open_image(path)
    if im is not None:
        info(im)


def parse(user_args):
    ## Parse the inputs
    parser = argparse.ArgumentParser(prog="convert")

    return vars(parser.parse_args(user_args))
