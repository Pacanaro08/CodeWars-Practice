import pytest, sys
sys.path.append('..')
from kata23 import solve

@pytest.mark.parametrize('array1, array2, expected', [
    (['abc', 'abc','xyz','abcd','cde'], ['abc', 'cde', 'uap'], [2, 1, 0]),
    (['abc', 'xyz','abc', 'xyz','cde'], ['abc', 'cde', 'xyz'], [2, 1, 2]),
    (['quick', 'brown', 'fox', 'is', 'quick'], ['quick', 'abc', 'fox'], [2, 0, 1]),
])

def test_solve(array1, array2, expected):
    assert solve(array1, array2) == expected