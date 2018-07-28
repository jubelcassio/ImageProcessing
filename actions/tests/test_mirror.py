from PIL import Image
from actions import mirror

def test_parse():
    args = ["v"]
    result = {"mirror_mode": "v", "save_as": None, "save_folder": None,
              "mode": None, "optimize": False, "background": (255,255,255)}
    assert mirror.parse(args) == result

    args = ["h"]
    result = {"mirror_mode": "h", "save_as": None, "save_folder": None,
    "mode": None, "optimize": False, "background": (255,255,255)}
    assert mirror.parse(args) == result

    args = ["vh"]
    result = {"mirror_mode": "vh", "save_as": None, "save_folder": None,
    "mode": None, "optimize": False, "background": (255,255,255)}
    assert mirror.parse(args) == result

    args = ["hv"]
    result = {"mirror_mode": "hv", "save_as": None, "save_folder": None,
    "mode": None, "optimize": False, "background": (255,255,255)}
    assert mirror.parse(args) == result

    args = ["vh", "--save_as=png", "--save_folder=home/output", "--mode=RGB",
            "--background=#bbb", "-optimize"]
    result = {"mirror_mode": "vh", "save_as": "png",
              "save_folder": "home/output", "mode": "RGB", "optimize": True,
              "background": (187,187,187)}
    assert mirror.parse(args) == result

def test_invert():
    white = (255,255,255)
    black = (0,0,0)
    bg = Image.new("RGB", (100, 100), white)
    im = Image.new("RGB", (50, 50), black)
    bg.paste(im)

    mirrored_im = mirror.mirror(bg, 'v')
    assert mirrored_im.crop((50,0,100,50)).getcolors() == [(2500, black)]
    assert mirrored_im.getcolors() == [(7500, white), (2500, black)]

    mirrored_im = mirror.mirror(bg, 'h')
    assert mirrored_im.crop((0,50,50,100)).getcolors() == [(2500, black)]
    assert mirrored_im.getcolors() == [(7500, white), (2500, black)]

    mirrored_im = mirror.mirror(bg, 'vh')
    assert mirrored_im.crop((50,50,100,100)).getcolors() == [(2500, black)]
    assert mirrored_im.getcolors() == [(7500, white), (2500, black)]
