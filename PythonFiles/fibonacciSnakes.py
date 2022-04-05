def charmSnakes(charm_ratings, time_for_charming):
    #set up fibonacci sequence
    #create list to store generated nth terms
    x = list(range(len(charm_ratings)))
    
    if len(x) > 0:
        for i in range(len(charm_ratings)):
            count = 0
            n1,n2 = 0, 1
            n = charm_ratings[i]
            # generate fibonacci sequence
            while count < n:
                nth = n1 + n2
                ## updating values
                n1 = n2
                n2 = nth
                count += 1
            x[i] = (n2) #add the nth term to a list

        #find biggest nth number
        max_time = max(x)
    else:
        max_time = 0
    
    if time_for_charming > max_time:
        message = print("Successfully charmed the snakes!")
    else:
        message = print("Failed to charm the snakes...")
        
    return message

charmSnakes([], 1)