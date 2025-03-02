import pytest, sys
sys.path.append('..')
from kata3 import histogram


@pytest.mark.parametrize('histogram_elements, expected', [
    ([7,3,10,1,0,5], '6|##### 5\n5|\n4|# 1\n3|########## 10\n2|### 3\n1|####### 7'),
    ([0,0,0,0,0,0], '6|\n5|\n4|\n3|\n2|\n1|'),
])

def test_histogram(histogram_elements, expected):
    assert histogram(histogram_elements) == expected
