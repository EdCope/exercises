from lasagna import *

def test_EXPECTED_BAKE_TIME():
    assert EXPECTED_BAKE_TIME == 40

def test_bake_time_remaining():
    actualTimeRemaining = 20
    assert bake_time_remaining(actualTimeRemaining) == 20
    assert bake_time_remaining(30) == 10