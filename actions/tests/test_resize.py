import argparse
from actions import resize
from PIL import Image

def test_parse():
    main_parser = argparse.ArgumentParser()
    subparsers = main_parser.add_subparsers()
    resize.subparser(subparsers)

    args = ["resize", "image.jpg", "200", "100"]
    result = {"command": "resize", "path": "image.jpg", "width": 200,
              "height": 100, "save_as": None, "optimize": False,
              "save_folder": None, "mode": None, "resample": None,
              "background": (255,255,255)}

    assert vars(main_parser.parse_args(args)) == result

    args = ["resize", "image.jpg", "200", "100", "--save_as=png",
            "--save_folder=home/output", "--mode=RGB", "--background=#bbb",
            "--resample=BOX", "-optimize"]
    result = {"command": "resize", "path": "image.jpg", "width": 200,
              "height": 100, "save_as": "png", "optimize": True,
              "save_folder": "home/output", "mode": "RGB", "resample": "BOX",
              "background": (187,187,187)}

    assert vars(main_parser.parse_args(args)) == result


def test_resize():
    im = Image.new("RGB", (300, 100))
    resized_im = resize.resize(im, 500, 200, None)

    assert resized_im.size == (500, 200)

    resized_im = resize.resize(im, 500, 200, "BICUBIC")

    assert resized_im.size == (500, 200)

    # Asserts the resulting image is at least 1x1 px
    resized_im = resize.resize(im, 0, 0, None)
    assert resized_im.size == (1, 1)
