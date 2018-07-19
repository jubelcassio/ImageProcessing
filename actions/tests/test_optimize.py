from actions import optimize
from PIL import Image

def test_parse():
    args = []
    result = {"save_as": None, "mode": None, "save_folder": None}

    assert optimize.parse(args) == result

    args = ["--save_as=png", "--mode=RGB", "--save_folder=home/output"]
    result = {"save_as": "png", "mode": "RGB", "save_folder": "home/output"}

    assert optimize.parse(args) == result


def test_optimize():
    im = Image.new("RGB", (300, 100))
    im.filename = "image.jpg"

    o_im, params =  optimize.optimize(im, "jpg")
    assert params == {"quality": 85, "optimize":True}

    o_im, params =  optimize.optimize(im, "png")
    assert o_im.mode == "P"
    assert params == {"optimize":True}
