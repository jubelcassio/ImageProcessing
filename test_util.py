from PIL import Image
from unittest.mock import patch, MagicMock
import argparse
import pytest
import os
import util

def test_coordinates_type():
    # Test a correct value
    assert util.coordinates_type("25,52") == (25,52)

    # Test trying to input a tuple raises Exception
    with pytest.raises(argparse.ArgumentTypeError) as e:
        util.coordinates_type("(25,52)")

    # Test trying to input float values raises Exception
    with pytest.raises(argparse.ArgumentTypeError) as e:
        util.coordinates_type("2.5,5.2")

    # Test trying to input negative values raises Exception
    with pytest.raises(argparse.ArgumentTypeError) as e:
        util.coordinates_type("-5,-10")


def test_rectangular_box_type():
    # Test a correct value
    assert util.rectangular_box_type("0,0,10,10") == (0,0,10,10)

    # Test dimensions dont match
    # In this case, the UPPER dimension is greater than the LOWER dimension
    with pytest.raises(argparse.ArgumentTypeError):
        util.rectangular_box_type("10,10,20,5")

    # Test float values raises Exception
    with pytest.raises(argparse.ArgumentTypeError):
        util.rectangular_box_type("10.1,10.1,20.3,20.3")

    # Test negative values raises Exception
    with pytest.raises(argparse.ArgumentTypeError):
        util.rectangular_box_type("-1,0,10,10")


def test_rgb_color_type():

    assert util.rgb_color_type("#4286f4") == (66, 134, 244)
    assert util.rgb_color_type("#fff") == (255, 255, 255)
    assert util.rgb_color_type("#000") == (0, 0, 0)
    assert util.rgb_color_type("66,134,244") == (66, 134, 244)

    # Test invalid hex code raises Exception
    with pytest.raises(argparse.ArgumentTypeError):
        util.rgb_color_type("#ggg")

    # Test invalid not enough color channels raises Exception
    with pytest.raises(argparse.ArgumentTypeError):
        util.rgb_color_type("200,200")

    # Test invalid float values raises Exception
    with pytest.raises(argparse.ArgumentTypeError):
        util.rgb_color_type("25.8,2.56,25.6")

    # Test invalid rgb values raises Exception
    with pytest.raises(argparse.ArgumentTypeError):
        util.rgb_color_type("258,250,250")

    # Test negative rgb values raises Exception
    with pytest.raises(argparse.ArgumentTypeError):
        util.rgb_color_type("-25,26,26")


@patch('util.Image')
def test_open_image(mocked_PIL_Image):

    real_path = os.path.realpath("")

    ## Test opening image with supported extension
    image_path = "imagepath.jpg"
    path = os.path.join(real_path, image_path)

    util.open_image(path)
    mocked_PIL_Image.open.assert_any_call(path)


    # Reseting the calls
    mocked_PIL_Image.open.reset_mock()


    ## Test opening image with UNsupported extension
    image_path = "imagepath.ubs"
    path = os.path.join(real_path, image_path)

    util.open_image(path)
    mocked_PIL_Image.open.assert_not_called()


    # Reseting the calls
    mocked_PIL_Image.open.reset_mock()


    ## Test opening image with UPPERCASE extension
    image_path = "imagepath.JPG"
    path = os.path.join(real_path, image_path)

    util.open_image(path)
    mocked_PIL_Image.open.assert_any_call(path)


def test_validate_mode():
    rgb_im = Image.new("RGB", (100,100))
    rgba_im = Image.new("RGBA", (100,100))

    ## User passed no mode, but the source image mode is compatible with the
    # saving format
    assert util.validate_mode(rgb_im, None, "jpg") == "RGB"

    ## User passed no mode, and the source image mode is NOT compatible with
    # the saving format
    assert util.validate_mode(rgba_im, None, "jpg") == "RGB"

    ## User passed a mode, and it is valid for the saving format
    assert util.validate_mode(rgb_im, "CMYK", "jpg") == "CMYK"

    ## User passed a mode, but it is NOT valid for the saving format
    assert util.validate_mode(rgb_im, "RGBA", "jpg") == None


def test_replace_alpha():
    back = Image.new("RGBA", (100,100))
    front = Image.new("RGBA", (50,50), (100,20,20))
    back.paste(front)
    im = util.replace_alpha(back, (20,20,100))

    assert im.getpixel((1,1)) == (100,20,20,255)
    assert im.getpixel((80,80)) == (20,20,100,255)


def test_optimize_img():
    im = Image.new("RGB", (100,100))

    jpg_im, params = util.optimize_img(im, "jpg", "RGB")
    assert (jpg_im.mode, params) == ("RGB", {"quality": 85, "optimize":True})

    png_im, params = util.optimize_img(im, "png", "RGBA")
    assert (png_im.mode, params) == ("P", {"optimize":True})

    assert util.optimize_img(im, "invalid", "RGBA") == None



def test_validate_save_format():

    # User gave a valid saving format
    assert util.validate_save_format("jpg", ".jpg") == "jpg"
    # User gave a INVALID saving format
    assert util.validate_save_format("txt", ".jpg") == None
    # User did not gave a valid saving format, but the file extension is valid
    assert util.validate_save_format(None, ".jpg") == "jpg"
    # User did not gave a valid saving format and the file extension is invalid
    assert util.validate_save_format(None, ".txt") == None


def test_save_image():
    # TODO
    pass