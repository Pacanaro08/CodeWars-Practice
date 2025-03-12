# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

def count_x_and_o(string):
    return (string.lower().count('o') == string.lower().count('x'))