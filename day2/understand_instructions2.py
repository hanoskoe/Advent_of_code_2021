# open and parse the file
with open("instructions.txt", "r") as instructions_file:
    instructions = []
    for instruction in instructions_file:
        keyword, value = instruction.strip().split()
        instructions.append((keyword, int(value)))

depth = 0
position = 0
aim = 0

# Strips the newline character
for keyword, value in instructions:
    if keyword == "forward":
        position = position + value
        depth = depth + aim * value
    elif keyword == "up":
        aim = aim - value
    elif keyword == "down":
        aim = aim + value


print("Final position is", position)
print("Final depth is", depth)
print("Final aim is", aim)
print("result is", depth * position)
