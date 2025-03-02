import pytest, sys
sys.path.append('..')
from kata14 import alphanumeric

@pytest.mark.parametrize('password, expected', [
    ("hello world_", False),
    ("PassW0rd", True),
    ("     ", False),
    ("__ * __", False),
    ("&)))(((", False),
    ("43534h56jmTHHF3k", True),
    ("", False)
])

def test_alphanumeric(password, expected):
    assert alphanumeric(password) == expected