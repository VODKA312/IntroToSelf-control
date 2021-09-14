import numpy as np

# A 4x5 robot world of characters 'o' and 'b'
world = np.array([ ['o', 'b', 'o', 'o', 'b'],
                   ['o', 'o', 'b', 'o', 'o'],
                   ['b', 'o', 'o', 'b', 'o'],
                   ['b', 'o', 'o', 'o', 'o'] ])

# Sensor measurement
measurement = ['b', 'o']

def find_match(world, measurement):
    
    # Empty possible_locations list
    possible_locations = []
    for y in range(world.shape[0]):
        for x in range(world.shape[1]):
            # if we are at the edge then we can't
            # look ahead. Use the "continue" statement
            # to proceed to the next step in the loop.
            if x == (world.shape[1]-1):
                continue
            
            m_under = world[y,x]   # get measurement UNDER robot
            m_front = world[y,x+1] # measurement in front of robot
            if [m_under, m_front] == measurement:
                possible_locations.append([y,x])
    
    return possible_locations
   

# This line runs the function and stores the output - do not delete 
locations = find_match(world, measurement)

