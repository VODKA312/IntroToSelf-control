points = 174  # use this as input for your submission

# establish the default prize value to None
prize = None

# use the points value to assign prizes to the correct prize names
if points <= 50:
    prize = "a wooden rabbit"
elif 151 <= points <= 180:
    prize = "a wafer-thin mint"
elif points >= 181:
    prize = "a penguin"

# use the truth value of prize to assign result to the correct prize
if prize:
    result = "Congratulations! You won " + prize + "!"
else:
    result = "Oh dear, no prize this time."

print(result)