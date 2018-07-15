from PIL import Image
from actions import fit
import pytest
from argparse import ArgumentTypeError

def test_parse():
    # No arguments
    args = ["200", "100"]
    result = {"width": 200, "height": 100, "color": (255,255,255),
              "save_as": None, "mode": None, "resample": None}
    assert fit.parse(args) == result

    # All arguments
    args = ["200", "100", "--color=#234aaa", "--save_as=png", "--mode=RGB",
            "--resample=BOX"]
    result = {"width": 200, "height": 100, "color": (35,74,170),
              "save_as": "png", "mode": "RGB", "resample": "BOX"}
    assert fit.parse(args) == result

    # Color hex code with alpha
    args = ["200", "100", "--color=#234aaa11"]
    result = {"width": 200, "height": 100, "color": (35,74,170,17),
              "save_as": None, "mode": None, "resample": None}
    assert fit.parse(args) == result

    # Color rgb
    args = ["200", "100", "--color=35,74,170"]
    result = {"width": 200, "height": 100, "color": (35,74,170),
              "save_as": None, "mode": None, "resample": None}
    assert fit.parse(args) == result

    # Color rgba
    args = ["200", "100", "--color=35,74,170,17"]
    result = {"width": 200, "height": 100, "color": (35,74,170,17),
              "save_as": None, "mode": None, "resample": None}
    assert fit.parse(args) == result


def test_fit():
    im = Image.new("RGB", (300, 100))

    fit_im = fit.fit(im, 600, 600, "#fff", None)
    assert fit_im.size == (600, 600)

    fit_im = fit.fit(im, 0, 0, "#fff", None)
    assert fit_im.size == (1, 1)

    fit_im = fit.fit(im, 0, 0, "#008080ff", None)
    assert fit_im.size == (1, 1)

    # Testing if the fiting is correct:
    red = (255,179,128,255)
    green = (0,128,128,50)
    im = Image.new("RGBA", (40, 30), red)

    # Test image fiting into same aspect ratio:
    fit_im = fit.fit(im, 80, 60, green, None)
    assert fit_im.getcolors() == [(4800, red)]

    ## Test fiting 4:3 into 6:3 ratio, the resulting image will have left and
    # right margins.
    fit_im = fit.fit(im, 120, 60, green, None)
    # Left Margin
    assert fit_im.crop((0,0,20,60)).getcolors() == [(1200, green)]
    # Pasted Image
    assert fit_im.crop((20,0,100,60)).getcolors() == [(4800, red)]
    # Right Margin
    assert fit_im.crop((100,0,120,60)).getcolors() == [(1200, green)]
    # Total
    assert fit_im.getcolors() == [(4800, red), (2400, green)]

    ## Test fiting 4:3 into 4:5 ratio, the resulting image will have top and
    # bottom margins.
    fit_im = fit.fit(im, 80, 100, green, None)
    # Top Margin
    assert fit_im.crop((0,0,80,20)).getcolors() == [(1600, green)]
    # Pasted Image
    assert fit_im.crop((0,20,80,80)).getcolors() == [(4800, red)]
    # Bottom Margin
    assert fit_im.crop((0,80,80,100)).getcolors() == [(1600, green)]
    # Total
    assert fit_im.getcolors() == [(4800, red), (3200, green)]
