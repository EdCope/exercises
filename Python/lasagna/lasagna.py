from re import A


EXPECTED_BAKE_TIME = 40

def bake_time_remaining(actual_time):
    return EXPECTED_BAKE_TIME - actual_time

def preparation_time_in_minutes(number_of_layers):
    return number_of_layers * 2