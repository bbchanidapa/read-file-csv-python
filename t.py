x = [1, 2, 3, 4]
y = [4, 5, 6]
zipped = zip(x, y)
print list(zipped)

x2, y2 = zip(*zip(x, y))
x == list(x2) and y == list(y2)

