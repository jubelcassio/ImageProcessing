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
