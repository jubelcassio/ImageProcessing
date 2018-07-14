from PIL import Image
from actions import resize

def test_parse():
    args = ["200", "100"]
    result = {"width": 200, "height": 100, "save_as": None, "mode": None,
              "resample": None}

    assert resize.parse(args) == result

    args = ["200", "100", "--save_as=png", "--mode=RGB", "--resample=BOX"]
    result = {"width": 200, "height": 100, "save_as": "png", "mode": "RGB",
              "resample": "BOX"}

    assert resize.parse(args) == result

def test_resize():
    im = Image.new("RGB", (300, 100))
    resized_im = resize.resize(im, 500, 200, None)

    assert resized_im.size == (500, 200)

    resized_im = resize.resize(im, 500, 200, "BICUBIC")

    assert resized_im.size == (500, 200)
