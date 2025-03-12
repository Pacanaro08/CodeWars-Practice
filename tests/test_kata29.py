import pytest, sys;
sys.path.append('..')
from kata29 import left_right_or_both

@pytest.mark.parametrize('keys, expected', [
    ("qwert", "Left"),
    ("yuiop", "Right"),
    ("abc", "Left"),
    ("ABC", "Left"),
    ("a b c", "Left"),
    ("xyz", "Both"),
    ("look up", "Right"),
    ("^&*()", "Right"),
    ("", ""),
    ("  ", ""),
])

def test_left_right_or_both(keys, expected):
    assert left_right_or_both(keys) == expected