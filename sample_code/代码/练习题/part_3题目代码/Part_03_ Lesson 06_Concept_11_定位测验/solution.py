import numpy as np

# A 4x5 robot world of characters 'o' and 'b'
world = np.array([ ['o', 'b', 'o', 'o', 'b'],
                   ['o', 'o', 'b', 'o', 'o'],
                   ['b', 'o', 'o', 'b', 'o'],
                   ['b', 'o', 'o', 'o', 'o'] ])

# Sensor measurement
measurement = ['b', 'o']

# This function takes in the world and the sensor measurement.
# Complete this function so that it returns the indices of the 
# likely robot locations, based on matching the measurement 
# with the color patterns in the world

def find_match(world, measurement):
    
    # Empty possible_locations list
    possible_locations = []
    
    # Store the number of columns and rows in the 2D array
    col = world.shape[1]
    row = world.shape[0]
    
    # Iterate through the entire array
    for i in range(0, row):
        for j in range (0, col):
            # Check that we are within the bounds of the world,
            # since we have to check two values, this means we're at
            # a row index < the number of columns (5) - 1
            # In other words j < 4
            if j < col - 1:
                # Check if a match is found by comparing array contents
                # and checking for equality at world[i][j] and 
                # one row to the right at world[i][j+1]
                
                # Values under and in front of the robot 
                under = world[i][j]
                in_front = world[i][j+1]
                
                if((measurement[0] == under) and (measurement[1] == in_front)):
                    # A match is found!
                    # Append the index that the robot is on
                    possible_locations.append([i,j])
    
    # Return the completed list
    return possible_locations
   

# This line runs the function and stores the output - do not delete 
locations = find_match(world, measurement)
