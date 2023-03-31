from twttr import shorten


def test_shorten():
    assert shorten("Aries Dave") == "Ars Dv"
