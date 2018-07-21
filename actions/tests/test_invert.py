from PIL import Image
from actions import invert

def test_parse():
    args = []
    result = {"save_as": None, "save_folder": None, "mode": None,
              "optimize": False}

    assert invert.parse(args) == result

    args = ["--save_as=png", "--save_folder=home/output", "--mode=RGB",
            "-optimize"]
    result = {"save_as": "png", "save_folder": "home/output", "mode": "RGB",
              "optimize": True}

    assert invert.parse(args) == result

def test_invert():
    white = (255,255,255)
    black = (0,0,0)
    bg = Image.new("RGB", (100, 100), white)
    im = Image.new("RGB", (50, 50), black)
    bg.paste(im)

    inverted_im = invert.invert(bg)
    assert inverted_im.crop((0,0,50,50)).getcolors() == [(2500, white)]
    assert inverted_im.getcolors() == [(2500, white), (7500, black)]

    black = (0,0,0,255)
    white = (255,255,255,255)
    transparent = (255,255,255,0)
    bg = Image.new("RGBA", (100, 100))
    im = Image.new("RGBA", (50, 50), black)
    bg.paste(im)

    inverted_im = invert.invert(bg)
    assert inverted_im.crop((0,0,50,50)).getcolors() == [(2500, white)]
    assert inverted_im.getcolors() == [(2500, white), (7500, transparent)]
