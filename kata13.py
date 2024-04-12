# The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

# What if the string is empty? Then the result should be empty object literal, {}.

def count(s):
    count = {}
    for i in s:
        quantity = 0
        for j in s:
            if i == j:
                quantity += 1
        count[i] = quantity
    
    return count