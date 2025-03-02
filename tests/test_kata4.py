import pytest, sys
sys.path.append('..')
from kata4 import histogram

@pytest.mark.parametrize('histogram_elements, expected', [
    ([7,3,70,15,0,5], '6|██ 5%\n5|\n4|███████ 15%\n3|███████████████████████████████████ 70%\n2|█ 3%\n1|███ 7%\n'),
    ([0,0,0,0,0,0], '6|\n5|\n4|\n3|\n2|\n1|\n'),
    ([0,0,11,0,0,0], '6|\n5|\n4|\n3|██████████████████████████████████████████████████ 100%\n2|\n1|\n'),
])

def test_histogram_kata4(histogram_elements, expected):
    assert histogram(histogram_elements) == expected