# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
# The output should be two capital letters with a dot separating them.
# It should look like this:

# Sam Harris => S.H
# patrick feeney => P.F

def initials(name:str):
    name_initials = ''
    i = 0
    while i <= len(name):
        if i == 0 or name[i - 1] == ' ':
            name_initials += name[i].capitalize()
            name_initials += '.'
        i += 1
    print(name_initials[0:len(name_initials) - 1])
    

initials('pietro pacanaro')