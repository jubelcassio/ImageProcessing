import argparse
from actions import colorswap
from PIL import Image

def test_parse():
    main_parser = argparse.ArgumentParser()
    subparsers = main_parser.add_subparsers()
    colorswap.subparser(subparsers)

    ## Create a main_parser and add the module subparser to it
    ## Add entries for the 'command' and 'path' arguments
    ## Parse the results and run the output through vars() to obtain a dict

    args = ["colorswap", "image.jpg", "255,0,0,255", "255,0,0,0"]
    result = {"command": "colorswap", "path": "image.jpg",
              "before_color": (255,0,0,255), "after_color": (255,0,0,0),
              "save_as": None, "save_folder": None, "mode": None,
              "optimize": False, "background": (255,255,255)}

    assert vars(main_parser.parse_args(args)) == result

    args = ["colorswap", "image.jpg", "255,0,0,255", "255,0,0,0",
            "--save_as=png", "--save_folder=home/output", "--mode=RGB",
            "--background=#bbb", "-optimize"]
    result = {"command": "colorswap", "path": "image.jpg",
              "before_color": (255,0,0,255), "after_color": (255,0,0,0),
              "save_as": "png", "save_folder": "home/output", "mode": "RGB",
              "optimize": True, "background": (187,187,187)}

    assert vars(main_parser.parse_args(args)) == result

def test_swap():
    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)
    im = Image.new("RGB", (100, 100), red)
    square = Image.new("RGB", (50, 50), green)
    im.paste(square)

    colorswaped_im = colorswap.swap(im, green, blue)

    # The expected results
    box_0_0_50_50 = [(2500, blue)]
    box_0_0_100_100 = [(7500, red), (2500, blue)]

    assert colorswaped_im.crop((0,0,50,50)).getcolors() == box_0_0_50_50
    assert colorswaped_im.crop((0,0,100,100)).getcolors() == box_0_0_100_100

    red = (*red, 255)
    green = (*green, 255)
    transparent = (0,0,0,0)
    im = Image.new("RGBA", (100, 100), red)
    square = Image.new("RGBA", (50, 50), green)
    im.paste(square)

    colorswaped_im = colorswap.swap(im, green, transparent)

    # The expected results
    box_0_0_50_50 = [(2500, transparent)]
    box_0_0_100_100 = [(7500, red), (2500, transparent)]

    assert colorswaped_im.crop((0,0,50,50)).getcolors() == box_0_0_50_50
    assert colorswaped_im.crop((0,0,100,100)).getcolors() == box_0_0_100_100
