# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.
# For example:
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']

def unique_in_order(sequence:str):
    result = []
    i = 0
    while i < len(sequence):
        if i == 0:
            result.append(sequence[i])
        else:
            if sequence[i] != sequence[i-1]:
                result.append(sequence[i])
        i+=1
    return (result)

unique_in_order("AAAABBBCCDAABBB")
#expected = ['A', 'B', 'C', 'D', 'A', 'B']