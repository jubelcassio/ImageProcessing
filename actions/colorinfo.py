import argparse
import os
import util

def colorinfo(im, box, pixel):
    if box == None:
        colors = im.getcolors()
    else:
        crop = im.crop(box)
        colors = crop.getcolors()

    if colors == None:
        print("{} has too many colors.".format(im.filename))
        return

    info = ""
    for query in colors:
        info += "{} pixels of {} color\n".format(query[0], query[1])

    print(info)

    if pixel != None:
        pixcolor = im.getpixel(pixel)
        print("The pixel at {} has {} color".format(pixel, pixcolor))


def run(path, namespace):
    im = util.open_image(path)
    if im is not None:
        colorinfo(im, namespace.box, namespace.pixel)

def subparser(subparser):
    colorinfo_parser = subparser.add_parser("colorinfo")
    colorinfo_parser.set_defaults(command="colorinfo")
    colorinfo_parser.add_argument('path')
    colorinfo_parser.add_argument('--box', type=util.rectangular_box_type)
    colorinfo_parser.add_argument('--pixel', type=util.coordinates_type)