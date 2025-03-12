# You have a keyboard like this:
# You strictly abide by the typing standard. That is, use the left hand hit the left part of the keyboard, use the right hand hit the right part of keyboard, the boundary is:
#  L     1.....5 | 6.....0     R
#  E     Q.....T | Y.....P     I
#  F     A.....G | H.....'     G
#  T     Z.....B | N...../     H
#           SPACEBAR           T
# Note: the SpaceBar is an exception, because both hands can be used to hit it.
# Complete the function that accepts a string.
# if the string can be typed by the left hand only, return "Left"
# if the string can be typed by the right hand only, return "Right"
# if both hands are needed to type the string, return "Both"
# if the string is empty or contains only spaces, return an empty string ""

def left_right_or_both(text):
    left = ['1','2','3','4','5','q','w','e','r','t','a','s','d','f','g','z','x','c','v','b','!','@','#','$','%','¨','|',]
    right = ['6','7','8','9','0','y','u','i','o','p','h','j','k','l','ç','n','m','^','&','*','(',')',':',',','.','>','<',';',"'",'"']
    
    is_right, is_left = False, False
    
    for letter in text.lower():
        if letter in right:
            is_right = True
        
        if letter in left:
            is_left = True
    
    if is_right and is_left:
        return "Both"
    elif is_right and is_left == False:
        return "Right"
    elif is_right == False and is_left:
        return "Left"
    
    return ''