from PIL import Image

import util

def test_rgb_color_type():

    assert util.rgb_color_type("#4286f4") == (66, 134, 244)
    assert util.rgb_color_type("#fff") == (255, 255, 255)
    assert util.rgb_color_type("#000") == (0, 0, 0)
    assert util.rgb_color_type("66,134,244") == (66, 134, 244)


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
