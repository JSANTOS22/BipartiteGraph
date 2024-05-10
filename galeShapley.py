from helperFunctions import prefers_over_m

# this is the original algorithm, returns a count of how many times it iterates to finish
def algo(preference):
    n = len(preference[0])

    # initialize free males and females by setting them to -1
    freeM = [-1] * n
    prefW = [-1] * n

    freeCount = n

    # this stores the amount of frames needed for the animation
    count = 0

    # iterate until there are no more free males
    while (freeCount > 0):

        # start at the first available free male
        m = 0
        for m in range(n):
            if freeM[m] == -1:
                break

        count += 1
        
        # now we iterate through free male's preference list to find first available woman
        i = 0
        while (i < n) and (freeM[m] == -1):

            # first, we set w to the next woman on preference list
            w = preference[m][i]

            # if preffered woman is free, we must engage the two individuals
            if prefW[w - n] == -1:
                # set male to taken
                freeM[m] = 0  
                # decrease available free males count
                freeCount -= 1
                # now engage the two individuals by setting woman's list to m
                prefW[w - n] = m

                #count += 1

            else:
            # this means that woman is engaged already, check if woman prefers m over current partner
                
                partner = prefW[w - n]

                if prefers_over_m(preference, m, partner, w):

                    count +=1

                    # then break up w's engagement and engage with m
                    prefW[w - n] = m
                    freeM[m] = 0
                    freeM[partner] = -1
            i += 1
    return prefW, count

# this is a modified version of the algorithm, it returns after every iteration to get each frame
def animateAlgo(freeM, prefW, preference):
    n = len(preference[0])

    # start at the first available free male
    m = 0
    for m in range(n):
        if freeM[m] == -1:
            break

    # now we iterate through free male's preference list to find first available woman
    i = 0
    while (i < n) and (freeM[m] == -1):

        # first, we set w to the next woman on preference list
        w = preference[m][i]

        # if preffered woman is free, we must engage the two individuals
        if prefW[w - n] == -1:
            # set male to taken
            freeM[m] = 0  
            # now engage the two individuals by setting woman's list to m
            prefW[w - n] = m

            # set up return string
            s = f'M{m} engages with W{w-n}'

            return freeM, prefW, w-n, s

        else:
            # this means that woman is engaged already, check if woman prefers m over current partner     
            partner = prefW[w - n]

            if prefers_over_m(preference, m, partner, w):

                # then break up w's engagement and engage with m
                prefW[w - n] = m
                freeM[m] = 0
                freeM[partner] = -1

                #set up return string 
                s = f'W{w-n} leaves M{partner} for M{m}, M{partner} must find a new partner'

                return freeM, prefW, w-n, s
            
        i += 1
    return freeM, prefW, -1, ''