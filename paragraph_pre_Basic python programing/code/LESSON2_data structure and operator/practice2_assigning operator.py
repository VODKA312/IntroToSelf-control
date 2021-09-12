# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8 # 4.45e8 = 4.45 * 10 ** 8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff
rainfall =  rainfall * 0.9
# add the rainfall variable to the reservoir_volume variable
reservoir_volume = rainfall + reservoir_volume
# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm
reservoir_volume = reservoir_volume * 1.05
# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume = reservoir_volume * 0.95
# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume = reservoir_volume - 2.5e5
# print the new value of the reservoir_volume variable
print(reservoir_volume)