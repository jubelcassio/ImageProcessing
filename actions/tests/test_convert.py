import argparse
from actions import convert

def test_parse():
    main_parser = argparse.ArgumentParser()
    subparsers = main_parser.add_subparsers()
    convert.subparser(subparsers)

    args = ["convert", "image.jpg", "png"]
    result = {"command": "convert", "path": "image.jpg", "save_as": "png",
              "mode": None, "save_folder": None, "optimize": False,
              "background": (255,255,255)}

    assert vars(main_parser.parse_args(args)) == result

    args = ["convert", "image.jpg", "png", "--mode=RGB",
            "--save_folder=home/output", "--background=#bbb", "-optimize"]
    result = {"command": "convert", "path": "image.jpg", "save_as": "png",
              "mode": "RGB", "save_folder": "home/output", "optimize": True,
              "background": (187,187,187)}

    assert vars(main_parser.parse_args(args)) == result
