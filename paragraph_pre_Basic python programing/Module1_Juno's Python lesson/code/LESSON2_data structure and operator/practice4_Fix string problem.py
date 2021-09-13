# TODO: Fix this string!
ford_quote = "Whether you think you can, or you think you can't--you're right."  # change '' to " "
print(ford_quote)

username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

# TODO: print a log message using the variables above.
# The message should have the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."

message = username + " accessed the site " + url + " at " + timestamp + "."
print(message)

# TODO: len.
given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

name_length = len(given_name+middle_names+family_name)+2 # like William*barley*pitt

# Now we check to make sure that the name fits within the driving license character limit
# Nothing you need to do here
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)