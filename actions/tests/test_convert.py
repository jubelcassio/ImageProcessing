from actions import convert

def test_parse():
    args = ["png"]
    result = {"filetype": "png", "mode": None}

    assert convert.parse(args) == result

    args = ["png", "--mode=RGB"]
    result = {"filetype": "png", "mode": "RGB"}

    assert convert.parse(args) == result
