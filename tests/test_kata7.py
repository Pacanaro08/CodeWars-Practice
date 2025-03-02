import pytest, sys
sys.path.append('..')
from kata7 import grandchild, child

magpie1 = "BWBWBW"
magpie2 = "BWBWBB"
magpie3 = "WWWWBB"
equal_magpie1, equal_magpie2 = 'WB'

"""Child or not Child"""
@pytest.mark.parametrize('bird1, bird2, expected', [
    (magpie1,magpie2,True),
    (magpie2,magpie3,True),
    (magpie1,magpie3,False),
    (magpie1,magpie1,False),
    (equal_magpie1, equal_magpie2, True),
    (magpie2,magpie1,True),
    (magpie3,magpie1,False),
])

def test_child(bird1, bird2, expected):
    assert child(bird1, bird2) == expected

"""Grandchild"""
@pytest.mark.parametrize('bird1, bird2, expected', [
    (magpie1,magpie3,True),
    (magpie1,magpie2,True),
    (magpie3,magpie1,True)
])

def test_grandchild(bird1, bird2, expected):
    assert grandchild(bird1, bird2) == expected

