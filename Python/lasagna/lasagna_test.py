from lasagna import *

def test_EXPECTED_BAKE_TIME():
    assert EXPECTED_BAKE_TIME == 40

def test_bake_time_remaining():
    actualTimeRemaining = 20
    assert bake_time_remaining(actualTimeRemaining) == 20
    assert bake_time_remaining(30) == 10
    assert bake_time_remaining(35) == 5

def test_preparation_time_in_minutes():
    number_of_layers = 3
    assert preparation_time_in_minutes(number_of_layers) == 6
    assert preparation_time_in_minutes(1) == 2

def test_elapsed_time_in_minutes():
    number_of_layers = 3
    elapsed_bake_time = 20
    assert elapsed_time_in_minutes(number_of_layers, elapsed_bake_time) == 26