import pytest, sys
sys.path.append('..')
from kata26 import get_animals_count

@pytest.mark.parametrize('legs_number, heads_number, horns_number, expected', [
    (34, 11, 6, {"rabbits" : 3, "chickens" : 5, "cows" : 3}),
    (154, 42, 10, {"rabbits" : 30, "chickens" : 7, "cows" : 5}),
    (74, 20, 34,  {"rabbits" : 0, "chickens" : 3, "cows" : 17}),
    (152, 38, 34,  {"rabbits" : 21, "chickens" : 0, "cows" : 17}),
    (56, 17, 0,  {"rabbits" : 11, "chickens" : 6, "cows" : 0}),
])

def test_get_animals_count(legs_number, heads_number, horns_number, expected):
    assert get_animals_count(legs_number, heads_number, horns_number) == expected