import pytest, sys
sys.path.append('..')
from kata20 import unique_in_order

@pytest.mark.parametrize('sequence, expected', [
    ("", []),
    ([], []),
    ((), []),
    ("A", ["A"]),
    (["A"], ["A"]),
    (("A",), ["A"]),
    ("AA", ["A"]),
    ("AAAABBBCCDAABBB", ["A", "B", "C", "D", "A", "B"]),
    ("ABBCcA", ["A", "B", "C", "c", "A"]),
    ([1, 2, 3, 3, -1], [1, 2, 3, -1]),
    (["a", "b", "b", "a"], ["a", "b", "a"]),
])

def test_unique_in_order(sequence, expected):
    assert unique_in_order(sequence) == expected