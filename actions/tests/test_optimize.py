from actions import optimize
from PIL import Image

def test_parse():
    args = []
    result = {"save_as": None, "mode": None, "save_folder": None}

    assert optimize.parse(args) == result

    args = ["--save_as=png", "--mode=RGB", "--save_folder=home/output"]
    result = {"save_as": "png", "mode": "RGB", "save_folder": "home/output"}

    assert optimize.parse(args) == result
