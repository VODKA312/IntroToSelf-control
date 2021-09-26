weight = ['65', '60', '55']
height = ['172', '165', '180']
persons = list(zip(weight, height))
print(persons)  # [('65', '172'), ('60', '165'), ('55', '180')] else return zip obj

# ergodic it
for letter, num in zip(weight, height):
    print("{}: {}".format(weight, height))

# unzip
some_list = [('a', 1), ('b', 2), ('c', 3)]
letters, nums = zip(*some_list)
print(letters)
print(nums)

letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)
