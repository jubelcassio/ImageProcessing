from actions import convert

def test_parse():
    args = ["png"]
    result = {"filetype": "png", "mode": None, "save_folder": None,
              "optimize": False}

    assert convert.parse(args) == result

    args = ["png", "--mode=RGB", "--save_folder=home/output", "-optimize"]
    result = {"filetype": "png", "mode": "RGB", "save_folder": "home/output",
              "optimize": True}

    assert convert.parse(args) == result
