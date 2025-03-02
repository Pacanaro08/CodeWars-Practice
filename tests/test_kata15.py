import pytest, sys
sys.path.append('..')
from kata15 import initials

@pytest.mark.parametrize('name, expected', [
    ("Sam Harris","S.H"),
    ("Patrick Feenan","P.F"),
    ("Evan Cole","E.C"),
    ("P Favuzzi","P.F"),
    ("David Mendieta","D.M"),
])

def test_initials(name, expected):
    assert initials(name) == expected