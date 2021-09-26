x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]
points = []
points = list(zip(x_coord, y_coord, z_coord))
# write your for loop here


for label, point in zip(labels, points):
    print("{}: {}".format(label, point))

# for point in zip(labels, x_coord, y_coord, z_coord):
#     points.append("{}: {}, {}, {}".format(*point))
# for point in points:
#     print(point)
