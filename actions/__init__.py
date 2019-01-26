import json
import os

cur_dir = os.path.dirname(os.path.realpath(__file__))

supported_formats = ["bmp","eps","gif","ico","jpg","jpeg","png","tiff",
                     "BMP","EPS","GIF","ICO","JPG","JPEG","PNG","TIFF"]
supported_modes = {
    "bmp":  ["1","L","P","RGB"],
    "eps":  ["L", "LAB", "CMYK", "RGB"],
    "gif":  ["L", "P", "RGB", "RGBA"],
    "ico":  ["1","L","P","RGB", "RGBA"],
    "jpg":  ["L", "CMYK", "RGB"],
    "jpeg": ["L", "CMYK", "RGB"],
    "png":  ["1","L","P","RGB", "RGBA"],
    "tiff": ["1","L", "LAB","P", "CMYK","RGB", "RGBA"]
}
all_modes = ["1", "L", "LAB", "P", "CMYK", "RGB", "RGBA"]
resampling_filters = ["NEAREST", "LANCZOS", "BILINEAR", "BICUBIC", "BOX",
                      "HAMMING"]

help_dict = {}
with open(os.path.join(cur_dir, "help.json")) as f:
    help_dict = json.load(f)
    f.close()


__all__ = ['convert', 'resize', 'fit', 'scale', 'info', 'optimize', 'invert',
           'mirror', 'dessaturate', 'colorswap', 'colorinfo']

from . import *

modules = {
    "convert" : convert,
    "resize" : resize,
    "fit" : fit,
    "scale" : scale,
    "info" : info,
    "optimize" : optimize,
    "invert" : invert,
    "mirror" : mirror,
    "dessaturate" : dessaturate,
    "colorswap" : colorswap,
    "colorinfo" : colorinfo
    }
