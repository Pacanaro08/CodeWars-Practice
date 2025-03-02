import pytest, sys
sys.path.append('..')
from kata12 import array_diff

@pytest.mark.parametrize('array1, array2, expected', [
    ([1,2], [1], [2]),
    ([1,2,2], [1], [2,2]),
    ([1,2,2], [2], [1]),
    ([1,2,2], [], [1,2,2]),
    ([], [1,2], []),
    ([1,2,3], [1, 2], [3]),
])

def test_array_diff(array1, array2, expected):
    assert array_diff(array1, array2) == expected