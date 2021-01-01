# with open("/workspace/aoc2020/input/day03_input") as file:
f = open("/workspace/aoc2020/input/day03_input", "r")
field = [line.strip() for line in f.readlines()]

trees = 0
squares = 0

for row in field:
    if row[squares] == "#":
        trees += 1
    squares = (squares + 3) % len(row)

print(trees)

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
result = 1
for slope, (right, down) in enumerate(slopes):
    trees = 0
    row = 0
    column = 0
    while row < len(field):
        if field[row][column] == "#":
            trees += 1
        row += down
        column = (column + right) % len(field[0])
    result *= trees
print(result)

