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