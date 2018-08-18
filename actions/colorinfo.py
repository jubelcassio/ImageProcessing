import argparse
import os
import util

def colorinfo(im, box):
    if box == None:
        colors = im.getcolors()
    else:
        crop = im.crop(box)
        colors = crop.getcolors()

    info = ""
    for query in colors:
        info += "{} pixels of {} color\n".format(query[0], query[1])

    print(info)

def run(path, box):
    im = util.open_image(path)
    if im is not None:
        colorinfo(im, box)


def parse(user_args):
    ## Parse the inputs
    parser = argparse.ArgumentParser(prog="colorinfo")

    parser.add_argument('--box', type=util.box_tuple)

    return vars(parser.parse_args(user_args))
