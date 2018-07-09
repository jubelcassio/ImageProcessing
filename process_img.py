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

def call_action(action, path, user_args):
    '''
    Calls one of the scripts on the 'actions/' package to process the
    image/images on the given path.
    user_args is parsed into a dictionary by the script's parse function.
    '''
    kwargs = action.parse(user_args)

    ## Execute script on a single file.
    if os.path.isfile(path):
        action.run(path, **kwargs)

    ## Execute script on all image files in a directory.
    elif os.path.isdir(path):
        file_list = os.listdir(path)
        for file_ in file_list:
            f_path = os.path.join(path, file_)
            if os.path.isfile(f_path):
                action.run(f_path, **kwargs)

    else:
        msg = "{} is not a valid file path or directory."
        print(msg.format(path))



if __name__ == '__main__':
    action = sys.argv[1]

    if action == "convert":
        call_action(convert, sys.argv[2], sys.argv[3:])
    elif action == "resize":
        call_action(resize, sys.argv[2], sys.argv[3:])
    elif action == "scale":
        call_action(scale, sys.argv[2], sys.argv[3:])
    elif action == "fit":
        call_action(fit, sys.argv[2], sys.argv[3:])
    else:
        msg = "Invalid action: '{}', choose from: {}".format(action,
                                                             action_list)
        print(msg)
