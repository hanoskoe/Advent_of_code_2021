# open and parse the file
with open("depths.txt", "r") as depths_file:
    depths = [int(depth.strip()) for depth in depths_file]


count = 0
previous_value = depths[0]
current_value = previous_value

# Strips the newline character
for current_value in depths:
    if current_value > previous_value:
        count += 1
    previous_value = current_value

print("Final count is", count)
