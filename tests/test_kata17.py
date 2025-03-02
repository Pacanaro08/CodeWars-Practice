import pytest, sys
sys.path.append('..')
from kata17 import sum_mix

@pytest.mark.parametrize('list, expected', [
    ([9, 3, '7', '3'], 22),
    (['5', '0', 9, 3, 2, 1, '9', 6, 7], 42),
    (['3', 6, 6, 0, '5', 8, 5, '6', 2,'0'], 41),
    (['1', '5', '8', 8, 9, 9, 2, '3'], 45),
    ([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7], 61),
])

def test_sum_mix(list, expected):
    assert sum_mix(list) == expected