import sys
import random

# helps determine if selected woman prefers m over current partner or not
def prefers_over_m(preference, m, partner, w):

    for i in range(len(preference[0])):
        if (preference[w][i] == m):
            # w prefers m over partner
            return True
        if (preference[w][i] == partner):
            # w prefers partner over m
            return False
    
    print("Error")
    sys.exit(1)

# generates random preference_list list given a size from user
def gen_random_preference_list(n):
    rows, num = 2*n, n 
    preference_list =[]

    for i in range(rows):
        
        if i < n:
            # then we are adding men's preference_lists of women (n -> 2*n -1)
            preference_list.append(random.sample(range(n, 2*n), num))
        else:
            # then we are adding women's preference_lists of men (0 -> n-1)
            preference_list.append(random.sample(range(0, n), num))
    
    return preference_list