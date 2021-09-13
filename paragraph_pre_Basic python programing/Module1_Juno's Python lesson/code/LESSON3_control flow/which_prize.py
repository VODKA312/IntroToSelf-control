points = 174  # use this input to make your submission

# write your if statement here
if points <=0 or points > 200:
    print("Invalid variable!")
else:
    if 1 <= points <= 50:
        prize_name = "wooden rabbit"
    elif 51 <= points <= 150:
        prize_name = "no prize"
    elif 151 <= points <= 180:
        prize_name = "wafer-thin mint"
    elif 181 <= points <= 200:
        prize_name = "penguin"
    result = "Congratulations! You won a "+prize_name+"!"
    print(result)

# another solution
# points = 174

# if points <= 50:
#    result = "Congratulations! You won a wooden rabbit!"
# elif points <= 150:
#    result = "Oh dear, no prize this time."
# elif points <= 180:
#    result = "Congratulations! You won a wafer-thin mint!"
# else:
#    result = "Congratulations! You won a penguin!"

# print(result)