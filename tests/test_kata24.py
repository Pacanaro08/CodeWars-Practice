import pytest, sys
sys.path.append('..')
from kata24 import is_divisible_by_6

@pytest.mark.parametrize('numbers_string, expected', [
    ("1*0",["120","150","180"]),
    ("*",["0","6"]),
    ("*1",[]),
    ("*2",["12", "42", "72"]),
    ("81234567890*",["812345678904"]),
    ("41*",["414"]),
    ("*6",["6", "36", "66", "96"]),
    ("2345*345729",[]),
    ("34234*2",["3423402","3423432","3423462","3423492"]),
    ("1234567890123456789012345678*0",["123456789012345678901234567800", "123456789012345678901234567830", "123456789012345678901234567860", "123456789012345678901234567890"]) ,
])

def test_is_divisible_by_6(numbers_string, expected):
    assert is_divisible_by_6(numbers_string) == expected