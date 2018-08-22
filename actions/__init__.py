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

__all__ = ['convert', 'resize', 'fit', 'scale', 'info', 'optimize', 'invert',
           'mirror', 'dessaturate', 'colorswap', 'colorinfo']

from . import *
