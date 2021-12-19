# open and parse the file
with open("depths.txt", "r") as depths_file:
    depths = [int(depth.strip()) for depth in depths_file]

count = 0
previous_sum = sum(depths[0:3])
for i in range(1, len(depths) - 2):
    window = depths[i : i + 3]
    current_sum = sum(window)
    if current_sum > previous_sum:
        count += 1
    previous_sum = current_sum
print("Final count is", count)
