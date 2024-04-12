# Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

# Examples:

# * 'abc' =>  ['ab', 'c_']
# * 'abcdef' => ['ab', 'cd', 'ef']

def solution(s):
    group = ''
    i = 0
    j = 0
    result = []

    for character in s:
        i += 1
        j += 1
        group = group + character
        if i == 2:
            result.append(group)
            group = ''
            i = 0
        elif len(group) == 1 and j == len(s):
            group = group + '_'
            result.append(group)

    return result

solution('abc')
