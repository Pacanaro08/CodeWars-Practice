# It is a little known fact^ that the black & white colours of baby magpies differ by at least one place and at most two places from the colours of the mother magpie.

# So now you can work out if any two magpies may be related.

# ...and Quardle oodle ardle wardle doodle the magpies said

# Kata Task
# Given the colours of two magpies, determine if one is a possible child or grand-child of the other.

# Notes
# Each pair of birds being compared will have same number of colour areas
# B = Black
# W = White
# Example
# Given these three magpies

# Magpie 1  BWBWBW
# Magpie 2  BWBWBB
# Magpie 3  WWWWBB
# You can see:

# Magpie 2 may be a child of Magpie 1 because there is only one difference
# Magpie 3 may be child of Magpie 2 because there are two differences
# So Magpie 3 may be a grand-child of Magpie 1
# On the other hand, Magpie 3 cannot be a child of Magpie 1 because there are three differences

def child(bird1, bird2):
    differences = 0
    i = 0
    while i < len(bird1):
        if bird1[i] != bird2[i]:
            differences += 1
        i += 1

    if differences != 0 and differences <= 2:
        return True
    else:
        return False

def grandchild(bird1, bird2):
    differences = 0
    i = 0
    while i < len(bird1):
        if bird1[i] != bird2[i]:
            differences += 1
        i += 1

    if (differences >= 1 and differences <= 4 and len(bird1) > 1) or (differences == 0 and len(bird1) <= 7):
        return True
    elif (differences == 1 and len(bird1) == 1) or (differences == 2 and len(bird1) == 2):
        return False
    else:
        return False
    