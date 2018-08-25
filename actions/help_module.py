import argparse
import json

def print_help(user_args):
    with open("actions/help.json") as f:
        help_dict = json.load(f)
        f.close()

    print(help_dict["global"])
    for module in help_dict["modules"].keys():
        description = help_dict["modules"][module]["summarized"]
        msg = "    {} : {}".format(module, description)
        print(msg)

def run(user_args):
    print_help(user_args)


def parse(user_args):
    ## Parse the inputs
    parser = argparse.ArgumentParser(prog="help")

    return vars(parser.parse_args(user_args))
