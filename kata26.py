# Farmer Bob has a big farm where he grows chickens, rabbits, and cows. It is very difficult to count the number of animals for each type manually, so he decided to buy a system to do it. 
# However, he bought a cheap system that can only count the total number of heads, legs, and horns of the animals on the farm. 
# Can you help Bob figure out how many chickens, rabbits, and cows he has?

# All chickens have 2 legs, 1 head and no horns; all rabbits have 4 legs, 1 head and no horns; all cows have 4 legs, 1 head and 2 horns.

def get_animals_count(legs_number, heads_number, horns_number):
    cows, rabbits, chickens = 0, 0, 0
    
    #Cows:
    cows = horns_number // 2
    heads_number -= cows
    legs_number -= cows * 4
    
    #Rabbits:
    rabbits = legs_number // 4
    heads_number -= rabbits
    legs_number -= rabbits * 4
    
    #Chickens:
    chickens = legs_number // 2
    heads_number -= chickens
    legs_number -= chickens * 2
    
    if (heads_number > 0):
        rabbits -= heads_number
        heads_number += heads_number
        legs_number += heads_number * 2
        
        chickens += legs_number // 2
        
            
    return {"rabbits" : rabbits, "chickens" : chickens, "cows" : cows}
        