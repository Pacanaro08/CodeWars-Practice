import pytest, sys
sys.path.append('..')
from kata22 import get_honor_path

@pytest.mark.parametrize('honor_score, target_honor_score, expected', [
    (2, 11, {"2kyus": 1, "1kyus": 4}),
    (2, 10, {"2kyus": 0, "1kyus": 4}),
    (2,  3, {"2kyus": 1, "1kyus": 0}),
    (11,  2, {}),
    (11, 11, {}),
])

def test_get_honor_path(honor_score, target_honor_score, expected):
    assert get_honor_path(honor_score, target_honor_score) == expected