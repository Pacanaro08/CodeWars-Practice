# Given two arrays of strings, return the number of times each string of the second array appears in the first array.
# array1 = ['abc', 'abc', 'xyz', 'cde', 'uvw']
# array2 = ['abc', 'cde', 'uap']
# How many times do the elements in array2 appear in array1?
# 'abc' appears twice in the first array (2)
# 'cde' appears only once (1)
# 'uap' does not appear in the first array (0)
# Therefore, solve(array1, array2) = [2, 1, 0]

def solve(array1, array2):
    arr_return = []
    
    for string2 in array2:
        i = 0
        for string1 in array1:
            if string1 == string2:
                i += 1
        
        arr_return.append(i)
        
    return arr_return