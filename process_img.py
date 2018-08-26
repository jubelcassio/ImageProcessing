#!/usr/bin/python

'''
Wrapper for the scripts that interacts with the user.
'''

import sys
import os
import argparse
from actions import modules


def call_action(namespace):
    '''
    Calls one of the scripts on the 'actions/' package to process the
    image/images on the given namespace.path
    The namespace argument is the output of the main parser.
    '''
    ## Execute script on a single file.
    if os.path.isfile(namespace.path):
        modules[namespace.command].run(namespace.path, namespace)

    ## Execute script on all image files in a directory.
    elif os.path.isdir(namespace.path):
        file_list = os.listdir(namespace.path)
        for file_ in file_list:
            f_path = os.path.join(namespace.path, file_)
            if os.path.isfile(f_path):
                print("\n...Processing {} file".format(f_path))
                modules[namespace.command].run(f_path, namespace)

    else:
        msg = "{} is not a valid file path or directory."
        print(msg.format(path))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    for module in modules.keys():
        modules[module].subparser(subparsers)

    namespace = parser.parse_args(sys.argv[1:])

    call_action(namespace)

