import argparse
from actions import optimize
from PIL import Image

def test_parse():
    main_parser = argparse.ArgumentParser()
    subparsers = main_parser.add_subparsers()
    optimize.subparser(subparsers)

    args = ["optimize", "image.jpg"]
    result = {"command": "optimize", "path": "image.jpg", "save_as": None,
              "mode": None, "save_folder": None, "background": (255,255,255)}

    assert vars(main_parser.parse_args(args)) == result

    args = ["optimize", "image.jpg", "--save_as=png", "--mode=RGB",
            "--background=#bbb", "--save_folder=home/output"]
    result = {"command": "optimize", "path": "image.jpg", "save_as": "png",
              "mode": "RGB", "save_folder": "home/output",
              "background": (187,187,187)}

    assert vars(main_parser.parse_args(args)) == result
