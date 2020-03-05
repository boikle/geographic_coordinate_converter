# import pytest
from converter import dd_converter

def test_dd_to_ddmm():
    dd_to_ddmm = dd_converter.dd_to_ddmm(43.23)
    assert dd_to_ddmm == "43° 13.799999999999812'"

def test_dd_to_ddmmss():
    dd_to_ddmmss = dd_converter.dd_to_ddmmss(43.23)
    assert dd_to_ddmmss == "43° 13' 47.999999999988745\""
