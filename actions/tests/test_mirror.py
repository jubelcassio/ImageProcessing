import argparse
from PIL import Image
from actions import mirror

def test_parse():
    main_parser = argparse.ArgumentParser()
    subparsers = main_parser.add_subparsers()
    mirror.subparser(subparsers)

    args = ["mirror", "image.jpg", "v"]
    result = {"command": "mirror", "path": "image.jpg", "mirror_mode": "v",
              "save_as": None, "save_folder": None, "mode": None,
              "optimize": False, "background": (255,255,255)}
    assert vars(main_parser.parse_args(args)) == result

    args = ["mirror", "image.jpg", "h"]
    result = {"command": "mirror", "path": "image.jpg", "mirror_mode": "h",
              "save_as": None, "save_folder": None, "mode": None,
              "optimize": False, "background": (255,255,255)}
    assert vars(main_parser.parse_args(args)) == result

    args = ["mirror", "image.jpg", "vh"]
    result = {"command": "mirror", "path": "image.jpg", "mirror_mode": "vh",
              "save_as": None, "save_folder": None, "mode": None,
              "optimize": False, "background": (255,255,255)}
    assert vars(main_parser.parse_args(args)) == result

    args = ["mirror", "image.jpg", "hv"]
    result = {"command": "mirror", "path": "image.jpg", "mirror_mode": "hv",
              "save_as": None, "save_folder": None, "mode": None,
              "optimize": False, "background": (255,255,255)}
    assert vars(main_parser.parse_args(args)) == result

    args = ["mirror", "image.jpg", "vh", "--save_as=png",
            "--save_folder=home/output", "--mode=RGB", "--background=#bbb",
            "-optimize"]
    result = {"command": "mirror", "path": "image.jpg", "mirror_mode": "vh",
              "save_as": "png", "save_folder": "home/output", "mode": "RGB",
              "optimize": True, "background": (187,187,187)}
    assert vars(main_parser.parse_args(args)) == result

def test_invert():
    white = (255,255,255)
    black = (0,0,0)
    bg = Image.new("RGB", (100, 100), white)
    im = Image.new("RGB", (50, 50), black)
    bg.paste(im)

    mirrored_im = mirror.mirror(bg, 'v')
    box_50_0_100_50 = [(2500, black)]
    box_total = [(7500, white), (2500, black)]
    assert mirrored_im.crop((50,0,100,50)).getcolors() == box_50_0_100_50
    assert mirrored_im.getcolors() == box_total

    mirrored_im = mirror.mirror(bg, 'h')
    box_0_50_50_100 = [(2500, black)]
    box_total = [(7500, white), (2500, black)]
    assert mirrored_im.crop((0,50,50,100)).getcolors() == box_0_50_50_100
    assert mirrored_im.getcolors() == box_total

    mirrored_im = mirror.mirror(bg, 'vh')
    box_50_50_100_100 = [(2500, black)]
    box_total = [(7500, white), (2500, black)]
    assert mirrored_im.crop((50,50,100,100)).getcolors() == box_50_50_100_100
    assert mirrored_im.getcolors() == box_total
