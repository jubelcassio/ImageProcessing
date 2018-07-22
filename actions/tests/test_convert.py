from actions import convert

def test_parse():
    args = ["png"]
    result = {"save_as": "png", "mode": None, "save_folder": None,
              "optimize": False}

    assert convert.parse(args) == result

    args = ["png", "--mode=RGB", "--save_folder=home/output", "-optimize"]
    result = {"save_as": "png", "mode": "RGB", "save_folder": "home/output",
              "optimize": True}

    assert convert.parse(args) == result
