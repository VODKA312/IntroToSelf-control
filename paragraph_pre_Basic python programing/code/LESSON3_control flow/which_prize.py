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