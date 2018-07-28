from PIL import Image
from actions import scale

def test_parse():
    args = ["2"]
    result = {"scalar": 2, "save_as": None, "save_folder": None,
              "mode": None, "resample": None, "optimize": False,
              "background": (255,255,255)}

    assert scale.parse(args) == result

    args = ["2", "--save_as=png", "--save_folder=home/output", "--mode=RGB",
            "--background=#bbb", "--resample=BOX", "-optimize"]
    result = {"scalar": 2, "save_as": "png", "save_folder": "home/output",
              "mode": "RGB", "resample": "BOX", "optimize": True,
              "background": (187,187,187)}

    assert scale.parse(args) == result

def test_scale():
    im = Image.new("RGB", (300, 100))

    scale_im = scale.scale(im, 2, None)
    assert scale_im.size == (600, 200)

    scale_im = scale.scale(im, 2, "BICUBIC")
    assert scale_im.size == (600, 200)

    # Asserts the resulting image is at least 1x1 px
    scale_im = scale.scale(im, 0, None)
    assert scale_im.size == (1, 1)
