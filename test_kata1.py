import pytest
from kata1 import trilingual_democracy

@pytest.mark.parametrize('group, expected', [
    ('DDD', 'D'),
    ('ddd', 'D'),
    ('eee', ''),
    ('EEE', ''),
    ('DFI', 'K'),
    ('', ''),
    ('DDDD', ''),
    ('DFD', 'F'),
    ('FFF', 'F'),
    ('IIK', 'K'),
    ('DFK', 'I'),
])


def test_trilingual_democracy(group, expected):
    assert trilingual_democracy(group) == expected
