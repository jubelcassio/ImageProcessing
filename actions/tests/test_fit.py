from PIL import Image
from actions import fit
import pytest
from argparse import ArgumentTypeError

def test_parse():
    args = ["200", "100"]
    result = {"width": 200, "height": 100, "color": "#fff", "alpha": 255,
              "save_as": None, "mode": None, "resample": None}

    assert fit.parse(args) == result

    args = ["200", "100", "--color=#234aaa", "--alpha=50", "--save_as=png",
            "--mode=RGB", "--resample=BOX"]
    result = {"width": 200, "height": 100, "color": "#234aaa", "alpha": 50,
              "save_as": "png", "mode": "RGB", "resample": "BOX"}
    assert fit.parse(args) == result

    args = ["200", "100", "--color=234aaa", "--alpha=50", "--save_as=png",
            "--mode=RGB", "--resample=BOX"]
    result = {"width": 200, "height": 100, "color": "#234aaa", "alpha": 50,
              "save_as": "png", "mode": "RGB", "resample": "BOX"}
    assert fit.parse(args) == result


def test_hex_code():
    # Valid codes
    assert fit.hex_code("234aaa") == "#234aaa"
    assert fit.hex_code("#234aaa") == "#234aaa"
    assert fit.hex_code("#23f") == "#23f"

    # Invalid codes
    with pytest.raises(ArgumentTypeError) as e_info:
        fit.hex_code("#234a")
    with pytest.raises(ArgumentTypeError) as e_info:
        fit.hex_code("#GGG")
    with pytest.raises(ArgumentTypeError) as e_info:
        fit.hex_code("#ff$")
    with pytest.raises(ArgumentTypeError) as e_info:
        fit.hex_code("#fffffff")

def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(*rgb)


def test_eight_bit():
    # Valid integers
    assert fit.eight_bit('0') == 0
    assert fit.eight_bit('100') == 100
    assert fit.eight_bit('255') == 255

    # Invalid integers
    with pytest.raises(ArgumentTypeError) as e_info:
        fit.eight_bit('-1')
    with pytest.raises(ArgumentTypeError) as e_info:
        fit.eight_bit('256')
    with pytest.raises(ArgumentTypeError) as e_info:
        fit.eight_bit('10.5')


def test_fit():
    ## TODO Improve this test by checking if the background matches the
    # predicted result for multiple images
    im = Image.new("RGB", (300, 100))

    fit_im = fit.fit(im, 600, 600, "#fff", 255, None)
    assert fit_im.size == (600, 600)

    fit_im = fit.fit(im, 0, 0, "#fff", 255, None)
    assert fit_im.size == (1, 1)

    # Testing if the fiting is correct:
    red_rgba = (255,179,128,255)
    green_hex = "#008080"
    green_rgba = (0,128,128,50)
    im = Image.new("RGBA", (40, 30), red_rgba)

    # Test image fiting into same aspect ratio:
    fit_im = fit.fit(im, 80, 60, green_hex, 50, None)
    assert fit_im.getcolors() == [(4800, red_rgba)]

    ## Test fiting 4:3 into 6:3 ratio, the resulting image will have left and
    # right margins.
    fit_im = fit.fit(im, 120, 60, green_hex, 50, None)
    # Left Margin
    assert fit_im.crop((0,0,20,60)).getcolors() == [(1200, green_rgba)]
    # Pasted Image
    assert fit_im.crop((20,0,100,60)).getcolors() == [(4800, red_rgba)]
    # Right Margin
    assert fit_im.crop((100,0,120,60)).getcolors() == [(1200, green_rgba)]
    # Total
    assert fit_im.getcolors() == [(4800, red_rgba), (2400, green_rgba)]

    ## Test fiting 4:3 into 4:5 ratio, the resulting image will have top and
    # bottom margins.
    fit_im = fit.fit(im, 80, 100, green_hex, 50, None)
    # Top Margin
    assert fit_im.crop((0,0,80,20)).getcolors() == [(1600, green_rgba)]
    # Pasted Image
    assert fit_im.crop((0,20,80,80)).getcolors() == [(4800, red_rgba)]
    # Bottom Margin
    assert fit_im.crop((0,80,80,100)).getcolors() == [(1600, green_rgba)]
    # Total
    assert fit_im.getcolors() == [(4800, red_rgba), (3200, green_rgba)]
