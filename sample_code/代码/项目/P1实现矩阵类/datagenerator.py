# You don't need to do anything with this file!

import math
import numpy as np

def generate_data(initial_distance, initial_velocity, final_velocity, acceleration,
	stopped_time, reverse_time, measurement_time_interval):
	# Data Generator

	# set time between measurements in milliseconds
	dt = measurement_time_interval

	# set initial distance, velocity, acceleration, final velocity
	initial_distance = initial_distance # m
	initial_velocity = initial_velocity # km/h
	final_velocity = final_velocity # km/h
	acceleration = acceleration # m/s^2

	# set how long the vehicle idles and then how long it moves backwards
	stopped_time = stopped_time # milliseconds
	reverse_time = reverse_time # milliseconds

	# convert acceleration to km/h^2
	acceleration_kmh = acceleration * 1e-3 * math.pow(60 * 60, 2)

	# set up variable to keep track of the current velocity and current_time
	current_velocity = initial_velocity
	current_time = 0

	# variables to hold the time, velocity, and acceleration results
	acceleration_groundtruth = []
	velocity_groundtruth = []
	time_groundtruth = []


	# Simulated data has 3 phases
	# Phase one: Object moves forward but is decelerating until velocity = 0
	# Phase two: Object is idle with velocity = 0 for amount of time in 
	#              stopped_time variable
	# Phase three: Object accelerates in reverse until reaching 
	#              final_velocity 
	# Phase four:  Object continues in reverse at constant veloctity 

	while(current_velocity > 0):
	    
	    acceleration_groundtruth.append(acceleration_kmh)
	    velocity_groundtruth.append(current_velocity)
	    time_groundtruth.append(current_time)
	    current_velocity += acceleration_kmh * (dt / (1000 * 60 * 60))
	    current_time += dt
	    

	# Phase two
	idle_time = dt
	current_velocity = 0
	while (idle_time < stopped_time):
	    
	    acceleration_groundtruth.append(0)
	    velocity_groundtruth.append(current_velocity)
	    time_groundtruth.append(current_time)

	    current_time += dt
	    idle_time += dt
	    
	# Phase three: accelerating in reverse
	while(current_velocity > final_velocity):
	    
	    acceleration_groundtruth.append(acceleration_kmh)
	    velocity_groundtruth.append(current_velocity)
	    time_groundtruth.append(current_time)

	    current_velocity += acceleration_kmh * (dt / (1000 * 60 * 60))
	    current_time += dt

	# Phase four: constant velocity in reverse 
	noaccel_time = dt
	current_velocity = velocity_groundtruth[-1]

	while (noaccel_time < reverse_time):

	    acceleration_groundtruth.append(0)
	    velocity_groundtruth.append(current_velocity)
	    time_groundtruth.append(current_time)

	    current_time += dt
	    noaccel_time += dt


	# Calculate distance ground truth
	x = initial_distance
	distance_groundtruth = [initial_distance]

	for i in range(len(time_groundtruth) - 1):
		# calculate delta_t and convert to seconds
	    time_difference = (time_groundtruth[i+1] - time_groundtruth[i]) / 1000

	    # convert velocity from km/h to m/s
	    velocity = 1000 * velocity_groundtruth[i] / (60 * 60)

	    # convert acceleration from km/h^2 to m/s^2
	    acceleration = 1000 * acceleration_groundtruth[i] / math.pow(60 * 60, 2)

	    # calculate distance traveled within the interval based on the velocity at [i] and the acceleration
	    x = x + velocity * time_difference + 0.5 * acceleration * math.pow(time_difference, 2)
	    
	    distance_groundtruth.append(x)

	return time_groundtruth, distance_groundtruth, velocity_groundtruth, acceleration_groundtruth

def generate_lidar(distance_groundtruth, standard_deviation):
	return distance_groundtruth + np.random.normal(0, standard_deviation, len(distance_groundtruth))