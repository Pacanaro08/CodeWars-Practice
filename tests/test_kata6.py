import pytest, sys
sys.path.append('..')
from kata6 import rpsls

@pytest.mark.parametrize('player1, player2, expected', [
    ('rock', 'lizard', 'Player 1 Won!'),
    ('paper', 'rock', 'Player 1 Won!'),
    ('scissors', 'lizard', 'Player 1 Won!'),
    ('lizard', 'paper', 'Player 1 Won!'),
    ('spock', 'rock', 'Player 1 Won!'),

    ('lizard','scissors', 'Player 2 Won!'),
    ('spock','lizard', 'Player 2 Won!'),
    ('paper','lizard', 'Player 2 Won!'),
    ('scissors','spock', 'Player 2 Won!'),
    ('rock','spock', 'Player 2 Won!'),

    ('rock', 'rock', 'Draw!'),
    ('spock', 'spock', 'Draw!'),

    ('any', '', 'Not a valid play!'),
])

def test_rpsls(player1, player2, expected):
    assert rpsls(player1, player2) == expected