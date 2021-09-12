names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for name in names:
    name = name.lower().replace(" ", "_")
    # replace methods is really important in processing string
    usernames.append(name)
print(usernames)
