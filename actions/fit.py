import argparse
import os
from PIL import Image
from actions import supported_formats
from actions import all_modes
from actions import resampling_filters
import util


def fit(im, width, height, color, resample):
    if width < 1: width = 1
    if height < 1: height = 1

    new_im = Image.new(im.mode, (width, height), color=color)

    im_ratio = im.width / im.height
    new_im_ratio = new_im.width / new_im.height

    if resample is None:
        resample_filter = 0
    else:
        resample_filter = resampling_filters.index(resample)

    # Both images have the same aspect ratio
    if im_ratio == new_im_ratio:
        resized_im = im.resize((new_im.width, new_im.height), resample_filter)
        topleft = (0, 0)

    # im has to fit on new_im's height
    if im_ratio < new_im_ratio:
        # Minimum width is 1 pixel.
        width = max([1, round((new_im.height / im.height) * im.width)])
        height = new_im.height
        resized_im = im.resize((width, height), resample_filter)
        topleft = ((new_im.width - width) // 2, 0)

    # im has to fit on new_im's width
    if im_ratio > new_im_ratio:
        width = new_im.width
        # Minimum height is 1 pixel.
        height = max([1, round((new_im.width / im.width) * im.height)])
        topleft = (0, (new_im.height - height) // 2)
        resized_im = im.resize((width, height), resample_filter)

    new_im.paste(resized_im, box=topleft)

    return new_im


def subparser(subparser):
    fit_parser = subparser.add_parser("fit")

    fit_parser.set_defaults(command="fit")

    fit_parser.add_argument('path')
    fit_parser.add_argument('width', type=int)
    fit_parser.add_argument('height', type=int)
    fit_parser.add_argument('-c', '--color', type=util.rgb_color_type,
                            default="#fff")
    fit_parser.add_argument('--save_folder', type=str, default=None)
    fit_parser.add_argument('--save_as', type=str, choices=supported_formats,
                            default=None)
    fit_parser.add_argument('--mode', type=str, choices=all_modes, default=None)
    fit_parser.add_argument('--background', type=util.rgb_color_type,
                            default="#fff")
    fit_parser.add_argument('--resample', type=str, choices=resampling_filters,
                            default=None)
    fit_parser.add_argument('-optimize', action="store_true")



def run(path, namespace):
    im = util.open_image(path)
    if im is not None:
        fit_image = fit(im, namespace.width, namespace.height, namespace.color,
                        namespace.resample)
        util.save_image(fit_image, namespace.path, namespace.save_folder,
                        namespace.save_as, namespace.mode, "fit",
                        namespace.optimize, namespace.background)