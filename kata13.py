# The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

# What if the string is empty? Then the result should be empty object literal, {}.

def count(string):
    count = {}
    for i in string:
        quantity = 0
        for j in string:
            if i == j:
                quantity += 1
        count[i] = quantity
    
    return count