import pytest, sys
sys.path.append('..')
from kata16 import find_average

@pytest.mark.parametrize('numbers, expected', [
    ([1, 2, 3], 2),
    ([], 0),
    ([1, 2], 1.5),
])

def test_find_average(numbers, expected):
    assert find_average(numbers) == expected