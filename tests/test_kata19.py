import pytest, sys
sys.path.append('..')
from kata19 import open_or_senior

@pytest.mark.parametrize('data, expected', [
    ([(45, 12),(55,21),(19, -2),(104, 20)],['Open', 'Senior', 'Open', 'Senior']),
    ([(3, 12),(55,1),(91, -2),(54, 23)],['Open', 'Open', 'Open', 'Open']),
    ([(59, 12),(55,-1),(12, -2),(12, 12)],['Senior', 'Open', 'Open', 'Open']),
    ([(74, 10),(55, 6),(12, -2),(68, 7)],['Senior', 'Open', 'Open', 'Open']),
    ([(16, 23),(56, 2),(56,  8),(54, 6)],['Open', 'Open', 'Senior', 'Open']),
])

def test_open_or_senior(data, expected):
    assert open_or_senior(data) == expected