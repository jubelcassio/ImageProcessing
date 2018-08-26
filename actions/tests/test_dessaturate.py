import argparse
from PIL import Image
from actions import dessaturate

def test_parse():
    main_parser = argparse.ArgumentParser()
    subparsers = main_parser.add_subparsers()
    dessaturate.subparser(subparsers)

    args = ["dessaturate", "image.jpg"]
    result = {"command": "dessaturate", "path": "image.jpg", "save_as": None,
              "save_folder": None, "mode": None, "optimize": False,
              "background": (255,255,255)}

    assert vars(main_parser.parse_args(args)) == result

    args = ["dessaturate", "image.jpg", "--save_as=png",
            "--save_folder=home/output", "--mode=RGB", "--background=#bbb",
            "-optimize"]
    result = {"command": "dessaturate", "path": "image.jpg", "save_as": "png",
              "save_folder": "home/output", "mode": "RGB", "optimize": True,
              "background": (187,187,187)}

    assert vars(main_parser.parse_args(args)) == result

def test_dessaturate():
    white = (255,255,255)
    red = (255,0,0)
    grayed_red = 76
    bg = Image.new("RGB", (100, 100), white)
    im = Image.new("RGB", (50, 50), red)
    bg.paste(im)

    dessaturated_im = dessaturate.dessaturate(bg)

    ## Expected results
    box_0_0_50_50 = [(2500, grayed_red)]

    assert dessaturated_im.crop((0,0,50,50)).getcolors() == box_0_0_50_50

    transparent = (0,0)
    grayed_red = (76, 255)
    bg = Image.new("RGBA", (100, 100))
    im = Image.new("RGBA", (50, 50), red)
    bg.paste(im)

    dessaturated_im = dessaturate.dessaturate(bg)

    ## Expected results
    box_0_0_50_50 = [(2500, grayed_red)]
    box_total = [(2500, grayed_red), (7500, transparent)]

    assert dessaturated_im.crop((0,0,50,50)).getcolors() == box_0_0_50_50
    assert dessaturated_im.getcolors() == box_total
