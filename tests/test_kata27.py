import pytest, sys;
sys.path.append('..')
from kata27 import count_x_and_o

@pytest.mark.parametrize('string, expected', [
    ("xo",      True),
    ("XO",      True),
    ("xo0",     True),
    ("xxxoo",   False),
    ("ooxx",    True),
    ("xooxx",   False),
    ("ooxXm",   True),
    ("zpzpzpp", True),
    ("zzoo",    False),
    ("oxOx",    True),
    ("",        True),
    ("xxxxxoooxooo", True),
    ("xxxxxoooXooo", True),
    ("abcdefghijklmnopqrstuvwxyz", True)
])

def test_count_x_and_o(string, expected):
    assert count_x_and_o(string) == expected