from PIL import Image
from actions import colorswap

def test_parse():
    args = ["255,0,0,255", "255,0,0,0"]
    result = {"before_color": (255,0,0,255), "after_color": (255,0,0,0),
              "save_as": None, "save_folder": None, "mode": None,
              "optimize": False, "background": (255,255,255)}

    assert colorswap.parse(args) == result

    args = ["255,0,0,255", "255,0,0,0", "--save_as=png",
            "--save_folder=home/output", "--mode=RGB", "--background=#bbb",
            "-optimize"]
    result = {"before_color": (255,0,0,255), "after_color": (255,0,0,0),
              "save_as": "png", "save_folder": "home/output", "mode": "RGB",
              "optimize": True, "background": (187,187,187)}

    assert colorswap.parse(args) == result

def test_swap():
    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)
    im = Image.new("RGB", (100, 100), red)
    square = Image.new("RGB", (50, 50), green)
    im.paste(square)

    colorswaped_im = colorswap.swap(im, green, blue)
    assert colorswaped_im.crop((0,0,50,50)).getcolors() == [(2500, blue)]
    assert colorswaped_im.crop((0,0,100,100)).getcolors() == [(7500, red),
                                                              (2500, blue)]

    red = (*red, 255)
    green = (*green, 255)
    transparent = (0,0,0,0)
    im = Image.new("RGBA", (100, 100), red)
    square = Image.new("RGBA", (50, 50), green)
    im.paste(square)

    colorswaped_im = colorswap.swap(im, green, transparent)
    assert colorswaped_im.crop((0,0,50,50)).getcolors() == [(2500, transparent)]
    assert colorswaped_im.crop((0,0,100,100)).getcolors() == [(7500, red),
                                                              (2500, transparent)]
