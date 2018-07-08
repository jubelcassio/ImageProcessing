'''
Wrapper for the scripts that interacts with the user.
'''


import sys
import os
from PIL import Image, ImageColor
import argparse
import re
import actions

supported_formats = ["bmp","eps","gif","ico","jpg","jpeg","png","tiff","webp"]
action_list = ['convert', 'resize', 'scale', 'fit']

if __name__ == '__main__':
    action = sys.argv[1]

    if action == "convert":
        actions.convert.call_convert(sys.argv[2:])
    elif action == "resize":
        actions.resize.call_resize(sys.argv[2:])
    elif action == "scale":
        actions.scale.call_scale(sys.argv[2:])
    elif action == "fit":
        actions.fit.call_fit(sys.argv[2:])
    else:
        msg = "Invalid action: '{}', choose from: {}".format(action,
                                                             action_list)
        print(msg)
