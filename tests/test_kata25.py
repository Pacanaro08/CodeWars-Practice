import pytest, sys
sys.path.append('..')
from kata25 import elimination

@pytest.mark.parametrize('array, expected', [
    ([2, 5, 34, 1, 22, 1], 1),
    ([2, 2, 34, 1, 22], 2),
    ([2, 5, 34, 1, 22], None),
    ([], None),
    ([5], None),
    ([8, 2], None),
    ([3, 3], 3),
    ([0, 0], 0),
])

def test_elimination(array, expected):
    assert elimination(array) == expected