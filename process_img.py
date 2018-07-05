import sys
import os
from PIL import Image

supported_formats = ["BMP","EPS","GIF","ICO","JPG","JPEG","PNG","TIFF","WEBP"]


def convert(path, filetype):
    if os.path.isfile(path):
        o_type = path[-3:]
        if o_type.upper() == filetype.upper():
            print("{} is already of type {}".format(path, filetype))
        elif o_type.upper() in supported_formats:
            new_image_path = "{}.converted.{}".format(path[:-4], filetype)
            im = Image.open(path)
            im.save(new_image_path)
            print("{} saved successfully.".format(new_image_path))
        else:
            msg = "{} is not a supported format.\nSupported formats: {}"
            print(msg.format(o_type, supported_formats))

    if os.path.isdir(path):
        file_list = os.listdir(path)

        for file_ in file_list:
            f_path = os.path.join(path, file_)
            f_type = file_[-3:]
            if f_type.upper() == filetype.upper():
                print("{} is already of type {}".format(f_path, filetype))
            elif f_type.upper() in supported_formats:
                new_image_path = "{}.converted.{}".format(f_path[:-4], filetype)
                im = Image.open(f_path)
                im.save(new_image_path)
                print("{} saved successfully.".format(new_image_path))

    else:
        msg = "{} is not a valid file path or directory."
        print(msg.format(path))



if __name__ == '__main__':
    action = sys.argv[1]

    if action == "convert":
        if len(sys.argv) < 3:
            print("Missing argument, try:\nprocess_img convert [directory/file] [image type]")
        elif len(sys.argv) < 4:
            img_type = sys.argv[2]
            convert(".", img_type)
        else:
            img_file = sys.argv[2]
            img_type = sys.argv[3]
            convert(img_file, img_type)
