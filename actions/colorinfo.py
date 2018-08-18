import argparse
import os
import util

def colorinfo(im, box, pixel):
    if box == None:
        colors = im.getcolors()
    else:
        crop = im.crop(box)
        colors = crop.getcolors()

    info = ""
    for query in colors:
        info += "{} pixels of {} color\n".format(query[0], query[1])

    print(info)

    if pixel != None:
        pixcolor = im.getpixel(pixel)
        print("The pixel at {} has {} color".format(pixel, pixcolor))


def run(path, box, pixel):
    im = util.open_image(path)
    if im is not None:
        colorinfo(im, box, pixel)


def parse(user_args):
    ## Parse the inputs
    parser = argparse.ArgumentParser(prog="colorinfo")

    parser.add_argument('--box', type=util.box_tuple)
    parser.add_argument('--pixel', type=util.coordinates)

    return vars(parser.parse_args(user_args))
