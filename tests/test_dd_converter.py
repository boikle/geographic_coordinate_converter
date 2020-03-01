from converter import dd_converter

def test_dd_to_ddmm():
    dd_to_ddmm = dd_converter.dd_to_ddmm(45.50)
    assert dd_to_ddmm == "45° 30.0'"
