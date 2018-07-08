'''
Wrapper for the scripts that interacts with the user.
'''


import sys
import os
from PIL import Image, ImageColor
import argparse
import re
from actions import *


action_list = ['convert', 'resize', 'scale', 'fit']


if __name__ == '__main__':
    action = sys.argv[1]

    if action == "convert":
        convert.call_convert(sys.argv[2:])
    elif action == "resize":
        resize.call_resize(sys.argv[2:])
    elif action == "scale":
        scale.call_scale(sys.argv[2:])
    elif action == "fit":
        fit.call_fit(sys.argv[2:])
    else:
        msg = "Invalid action: '{}', choose from: {}".format(action,
                                                             action_list)
        print(msg)
