import pytest, sys
sys.path.append('..')
from kata13 import count

@pytest.mark.parametrize('string, expected', [
    ('aba', {'a': 2, 'b': 1}),
    ('', {}),
    ('aa', {'a' : 2}),
    ('aabb', {'b' : 2, 'a' : 2})
])

def test_count(string, expected):
    assert count(string) == expected