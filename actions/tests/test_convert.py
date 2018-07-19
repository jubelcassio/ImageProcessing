from actions import convert

def test_parse():
    args = ["png"]
    result = {"filetype": "png", "mode": None, "save_folder": None}

    assert convert.parse(args) == result

    args = ["png", "--mode=RGB", "--save_folder=home/output"]
    result = {"filetype": "png", "mode": "RGB", "save_folder": "home/output"}

    assert convert.parse(args) == result
