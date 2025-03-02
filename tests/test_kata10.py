import pytest, sys
sys.path.append('..')
from kata10 import smash

@pytest.mark.parametrize('words, expected', [
    ([], ''),
    (["hello"], "hello"),
    (["hello", "world"], "hello world"),
    (["hello", "amazing", "world"], "hello amazing world"),
    (["this", "is", "a", "really", "long", "sentence"], "this is a really long sentence"),
])

def test_smash(words, expected):
    assert smash(words) == expected