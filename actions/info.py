import argparse
import os
from PIL import Image
from actions import supported_formats
from actions import supported_modes

def run(path):
    extension = path.split(".")[-1]
    if extension not in supported_formats:
        print("{} does not have a supported file type.".format(path))
    else:
        im = Image.open(path)
        infotext ="{}\nformat: {}\nmode: {}\nsize: {}"
        print(infotext.format(im.filename, im.format, im.mode, im.size))

def parse(user_args):
    ## Parse the inputs
    parser = argparse.ArgumentParser(prog="convert")

    return vars(parser.parse_args(user_args))
