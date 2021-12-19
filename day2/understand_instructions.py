# open and parse the file
with open("instructions.txt", "r") as instructions_file:
    instructions = []
    for instruction in instructions_file:
        keyword, value = instruction.strip().split()
        instructions.append((keyword, int(value)))


position = 0
depth = 0

for keyword, value in instructions:
    if keyword == "forward":
        position = position + value
    elif keyword == "up":
        depth = depth - value
    elif keyword == "down":
        depth = depth + value


print("Final position is", position)
print("Final depth is", depth)
print("result is", depth * position)
