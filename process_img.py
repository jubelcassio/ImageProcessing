import sys
import os
from PIL import Image

supported_formats = ["BMP","EPS","GIF","ICO","JPG","JPEG","PNG","TIFF","WEBP"]


def convert(path, filetype):
    if os.path.isfile(path):
        o_type = path[-3:]
        if o_type.upper() in supported_formats:
            im = Image.open(path)
            new_image_path = "{}.converted.{}".format(path[:-4], filetype)
            im.save(new_image_path)
            print("{} saved successfully.".format(new_image_path))
        else:
            msg = "{} is not a supported format.\nSupported formats: {}"
            print(msg.format(o_type, supported_formats))
    else:
        msg = "{} is not a valid file path."
        print(msg.format(path))


if __name__ == '__main__':
    action = sys.argv[1]

    if action == "convert":
        if len(sys.argv) < 4:
            print("Missing argument, try:\nprocess_img convert [image file] [image type]")
        else:
            img_file = sys.argv[2]
            img_type = sys.argv[3]
            convert(img_file, img_type)
