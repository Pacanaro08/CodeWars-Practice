import pytest, sys
sys.path.append('..')
from kata11 import solution

@pytest.mark.parametrize('string, expected', [
    ("asdfadsf", ['as', 'df', 'ad', 'sf']),
    ("asdfads", ['as', 'df', 'ad', 's_']),
    ("", []),
    ("x", ["x_"]),
])

def test_solution(string, expected):
    assert solution(string) == expected