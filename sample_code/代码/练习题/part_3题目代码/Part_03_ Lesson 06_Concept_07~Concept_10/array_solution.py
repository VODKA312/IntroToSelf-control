test_road = ['r', 'r', 's', 'r']

def stop_test(road):
    # Iterate through the road array
    for i in range(0, len(road)):
        # find where the stop sign is and return the index right before
        if(road[i] == 's'):
            stop_index = i -1
            break
    return stop_index