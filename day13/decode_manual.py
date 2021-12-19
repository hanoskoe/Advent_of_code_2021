# open and parse the file
with open("input.txt", "r") as input_file:
    coordinates = []
    for dot in input_file:
        x_coord, y_coord = dot.strip().split(",")
        coordinates.append((int(x_coord), int(y_coord)))
# print(coordinates)

with open("fold_instructions.txt", "r") as instructions_file:
    fold_instructions = []
    for instruction_line in instructions_file:
        instruction = instruction_line.strip().split()[2]
        fold_axe, fold_value = instruction.split("=")
        fold_instructions.append((fold_axe, int(fold_value)))
print(fold_instructions)

# TODO:get the maximum coordinates of x and y to know how big table I need
x_max = 0
y_max = 0
for dot in coordinates:
    if dot[0] > x_max:
        x_max = dot[0]
    if dot[1] > y_max:
        y_max = dot[1]

# returns new max coordinates
def fold_paper(x_max, y_max, paper, axe, value):
    if axe == "x":  # horizontal fold
        # fold left all values that are above the value
        for x in range(value, x_max + 1):
            for y in range(y_max + 1):
                if paper[y][x] == "#":
                    paper[y][2 * value - x] = "#"
    elif axe == "y":  # vertical fold
        # fold up all vaues below the value
        for x in range(x_max + 1):
            for y in range(value, y_max + 1):
                if paper[y][x] == "#":
                    # print("looking at # at coordinates", x, y)
                    # print("remapping it to coordinates", x, 2 * value - y)
                    paper[2 * value - y][x] = "#"


def count_dots(x_max, y_max, paper):
    count = 0
    for x in range(x_max + 1):
        for y in range(y_max + 1):
            if paper[y][x] == "#":
                count = count + 1
    return count


print("x_max is", x_max, "y_max is", y_max)

# create a structure that will contain all those dots and populate it correctly
transparent_paper = [["."] * (x_max + 1) for _ in range(y_max + 1)]
# print(transparent_paper)
for dot in coordinates:
    # print("adding dot on coordinates", dot[0], dot[1])
    transparent_paper[dot[1]][dot[0]] = "#"
# for line in transparent_paper:
#     print(line)

for instruction in fold_instructions:
    fold_value = instruction[1]
    # fold_value = 7
    fold_axe = instruction[0]
    # fold_axe = "y"
    print(
        "folding paper along the axe",
        fold_axe,
        "with value",
        fold_value,
    )
    fold_paper(x_max, y_max, transparent_paper, fold_axe, fold_value)
    if fold_axe == "x":
        x_max = fold_value
    else:
        y_max = fold_value
    print("new values of x_max and y_max are", x_max, y_max)
    result = count_dots(x_max, y_max, transparent_paper)
    print("result of the first part is", result)
    # create new paper that will be smaller and will still contain the same values as the previous paper
    new_paper = [["."] * (x_max + 1) for _ in range(y_max + 1)]
    for x in range(x_max + 1):
        for y in range(y_max + 1):
            new_paper[y][x] = transparent_paper[y][x]
    transparent_paper = new_paper

for line in transparent_paper:
    # print(line)
    print("".join(str(x) for x in line))

print("Result of the second part is PGHRKLKL")
