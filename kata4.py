# A 6-sided die is rolled a number of times and the results are plotted as percentages in a character-based horizontal histogram.
# Example:

# 6|██ 5%
# 5|
# 4|███████ 15%
# 3|███████████████████████████████████ 70%
# 2|█ 3%
# 1|███ 7%
# Task
# You will be passed the dice value frequencies, and your task is to write the code to return a string representing a histogram, so that when it is printed it has the same format as the example.

# Notes
# There are no trailing spaces on the lines
# All lines (including the last) end with a newline \n
# The percentage is displayed beside each bar except where it is 0%
# The total number of rolls varies, but won't exceed 10,000
# The bar lengths are scaled so that 100% = 50 x bar characters
# The bar character is █, which is the Unicode U+2588 char
# When calculating percentages and bar lengths always floor/truncate to the nearest integer

def histogram(results):
    res = ''
    total = 0
    i = len(results)
    total = sum(results)
    while i > 0:
        j = 0
        res += str(i) + '|'
        if results[i-1] != 0:
            squares = int(((results[i-1])*50)/total)
            percentage = int(((results[i-1])*100)/total)
            while j < squares:
                res += '█'
                j += 1
            res += ' ' + str(percentage) + '%\n'
        else:
            res += '\n'
        i -= 1
    return res