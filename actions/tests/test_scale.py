import argparse
from actions import scale
from PIL import Image

def test_parse():
    main_parser = argparse.ArgumentParser()
    subparsers = main_parser.add_subparsers()
    scale.subparser(subparsers)

    args = ["scale", "image.jpg", "2"]
    result = {"command": "scale", "path": "image.jpg", "scalar": 2,
              "save_as": None, "save_folder": None, "mode": None,
              "resample": None, "optimize": False, "background": (255,255,255)
              }

    assert vars(main_parser.parse_args(args)) == result

    args = ["scale", "image.jpg", "2", "--save_as=png",
            "--save_folder=home/output", "--mode=RGB", "--background=#bbb",
            "--resample=BOX", "-optimize"]
    result = {"command": "scale", "path": "image.jpg", "scalar": 2,
              "save_as": "png", "save_folder": "home/output", "mode": "RGB",
              "resample": "BOX", "optimize": True, "background": (187,187,187)
              }

    assert vars(main_parser.parse_args(args)) == result


def test_scale():
    im = Image.new("RGB", (300, 100))

    scale_im = scale.scale(im, 2, None)
    assert scale_im.size == (600, 200)

    scale_im = scale.scale(im, 2, "BICUBIC")
    assert scale_im.size == (600, 200)

    # Asserts the resulting image is at least 1x1 px
    scale_im = scale.scale(im, 0, None)
    assert scale_im.size == (1, 1)
