from PIL import Image
from actions import resize

def test_parse():
    args = ["200", "100"]
    result = {"width": 200, "height": 100, "save_as": None, "optimize": False,
              "save_folder": None, "mode": None, "resample": None,
              "background": (255,255,255)}

    assert resize.parse(args) == result

    args = ["200", "100", "--save_as=png", "--save_folder=home/output",
            "--mode=RGB", "--background=#bbb", "--resample=BOX", "-optimize"]
    result = {"width": 200, "height": 100, "save_as": "png", "optimize": True,
              "save_folder": "home/output", "mode": "RGB", "resample": "BOX",
              "background": (187,187,187)}

    assert resize.parse(args) == result

def test_resize():
    im = Image.new("RGB", (300, 100))
    resized_im = resize.resize(im, 500, 200, None)

    assert resized_im.size == (500, 200)

    resized_im = resize.resize(im, 500, 200, "BICUBIC")

    assert resized_im.size == (500, 200)

    # Asserts the resulting image is at least 1x1 px
    resized_im = resize.resize(im, 0, 0, None)
    assert resized_im.size == (1, 1)
