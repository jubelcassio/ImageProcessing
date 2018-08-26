import argparse
from PIL import Image
from actions import invert

def test_parse():
    main_parser = argparse.ArgumentParser()
    subparsers = main_parser.add_subparsers()
    invert.subparser(subparsers)

    args = ["invert", "image.jpg"]
    result = {"command": "invert", "path": "image.jpg", "save_as": None,
              "save_folder": None, "mode": None, "optimize": False,
              "background": (255,255,255)}

    assert vars(main_parser.parse_args(args)) == result

    args = ["invert", "image.jpg", "--save_as=png",
            "--save_folder=home/output", "--mode=RGB", "--background=#bbb", "-optimize"]
    result = {"command": "invert", "path": "image.jpg", "save_as": "png",
              "save_folder": "home/output", "mode": "RGB", "optimize": True,
              "background": (187,187,187)}

    assert vars(main_parser.parse_args(args)) == result

def test_invert():
    white = (255,255,255)
    black = (0,0,0)
    bg = Image.new("RGB", (100, 100), white)
    im = Image.new("RGB", (50, 50), black)
    bg.paste(im)

    inverted_im = invert.invert(bg)

    ## Expected results
    box_0_0_50_50 = [(2500, white)]
    box_total = [(2500, white), (7500, black)]

    assert inverted_im.crop((0,0,50,50)).getcolors() == box_0_0_50_50
    assert inverted_im.getcolors() == box_total

    black = (0,0,0,255)
    white = (255,255,255,255)
    transparent = (255,255,255,0)
    bg = Image.new("RGBA", (100, 100))
    im = Image.new("RGBA", (50, 50), black)
    bg.paste(im)

    inverted_im = invert.invert(bg)

    box_0_0_50_50 = [(2500, white)]
    box_total = [(2500, white), (7500, transparent)]

    assert inverted_im.crop((0,0,50,50)).getcolors() == box_0_0_50_50
    assert inverted_im.getcolors() == box_total
