# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.
# "a" = 1, "b" = 2, etc.

def alphabet_position(text:str):
    text = text.lower()

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    positions = []
    for char in text:
        if char.isalpha():
            position = alphabet.index(char) + 1
            positions.append(str(position))
    
    return ' '.join(positions)

alphabet_position('Basic Test Cases')