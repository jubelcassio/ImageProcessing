from actions import convert

def test_parse():
    args = ["png"]
    result = {"save_as": "png", "mode": None, "save_folder": None,
              "optimize": False, "background": (255,255,255)}

    assert convert.parse(args) == result

    args = ["png", "--mode=RGB", "--save_folder=home/output",
            "--background=#bbb", "-optimize"]
    result = {"save_as": "png", "mode": "RGB", "save_folder": "home/output",
              "optimize": True, "background": (187,187,187)}

    assert convert.parse(args) == result
