import pytest, sys
sys.path.append('..')
from kata5 import rps

@pytest.mark.parametrize('player1, player2, expected', [
    ('rock', 'scissors', 'Player 1 won!'),
    ('scissors', 'paper', 'Player 1 won!'),
    ('paper', 'rock', 'Player 1 won!'),

    ('scissors', 'rock', 'Player 2 won!'),
    ('paper', 'scissors', 'Player 2 won!'),
    ('rock', 'paper', 'Player 2 won!'),

    ('rock', 'rock', 'Draw!'),
    ('scissors', 'scissors', 'Draw!'),
    ('paper', 'paper', 'Draw!'),

    ('', 'rock', ''),
    ('anything', 'anything else', '')
])

def test_rps(player1, player2, expected):
    assert rps(player1, player2) == expected