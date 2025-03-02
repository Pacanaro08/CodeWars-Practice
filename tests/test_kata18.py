import pytest, sys
sys.path.append('..')
from kata18 import decode_morse

@pytest.mark.parametrize('morse_code, expected', [
    ('.-', 'A'),
    ('--...', '7'),
    ('...-..-', '$'),
    ('.', 'E'),
    ('..', 'I'),
    ('. .', 'EE'),
    ('.   .', 'E E'),
    ('...-..- ...-..- ...-..-', '$$$'),
    ('----- .---- ..--- ---.. ----.', '01289'),
    ('.-... ---...   -..-. --...', '&: /7'),
    ('...---...', 'SOS'),
    ('... --- ...', 'SOS'),
    ('...   ---   ...', 'S O S'),
    (' . ', 'E'),
    ('   .   . ', 'E E'),
    ('      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  ', 'SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.'),
])

def test_decode_morse(morse_code, expected):
    assert decode_morse(morse_code) == expected