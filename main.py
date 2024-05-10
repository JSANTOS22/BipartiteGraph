import sys
from helperFunctions import gen_random_preference_list
from galeShapley import algo
from animation import initialize_Animation

if __name__ == '__main__':
    # get user input for however many nodes they want
    n = int(input('How many nodes on each side? '))
    
    # make sure n > 0
    if n <= 0:
        print('Error: number of nodes must be greater than 0')
        sys.exit(1)

    # generate random preference list given user's desired n size
    preference_list = gen_random_preference_list(n)

    # this gets the count of however many iterations the algorithm does
    # so we know how many frames we need in the visualization
    result, count = algo(preference_list)

    # call the function that initializes the animation by creating a graph of all the nodes
    # the function then calls the actual animation function after doing so
    initialize_Animation(count, preference_list)



    



    