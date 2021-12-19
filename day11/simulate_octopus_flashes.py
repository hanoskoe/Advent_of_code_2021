# open the files and load content
input_file = open("/home/eva/Documents/Coding_advent/day11/input.txt", "r")
Lines = input_file.readlines()
table = []
width = len(Lines[0]) - 1
length = len(Lines)
print("width is", width, "length is", length)

# create list of lists of ints (and you can access coordinates x, y of each int)
for line in Lines:
    current_list = []
    for elt in line.strip():
        current_list.append([int(elt), 0])
        #the second value in the table is "flashed this tour", needs to be reset to 0 afterwards
    table.append(current_list)


def get_adjacent(x, y):
    # print("calling get_adjacent on", x, y)
    vector_list = [(0, 1), (1, 0), (-1, 0), (0, -1), (1,1), (1,-1), (-1,-1), (-1,1)]
    adjacent_pts = []
    for vector in vector_list:
        new_point = (x + vector[0], y + vector[1])
        if (
            new_point[0] >= 0
            and new_point[1] >= 0
            and new_point[0] < length
            and new_point[1] < width
        ):
            adjacent_pts.append(new_point)
    # print("Returning adjacent points", adjacent_pts)
    return adjacent_pts


#need the recursivity again
def update_val(x,y):
    num_flashes = 0
    cur_value = table[x][y][0]
    if(table[x][y][1] == 0): #enters the following only if this did not flash this round
        if (cur_value < 9):
            table[x][y][0] = cur_value+1
        else:#here comes the flash
            num_flashes = num_flashes+1
            # print("saw flash")
            table[x][y][0] = 0 #reset this value to 0
            table[x][y][1] = 1 #mark is as counted so cannot be updated more this round
            adjacent_pts = get_adjacent(x,y)
            for pt in adjacent_pts:
                num_flashes = num_flashes+update_val(pt[0],pt[1])
    return num_flashes
            

#first part
# flashes = 0
# for i in range(100):
#     for x in range (length):
#         for y in range(width):
#             if(table[x][y][1] == 0): #enters the following only if this did not flash this round
#                 flashes = flashes + update_val(x,y)
#     for x in range (length):
#         for y in range(width):
#             table[x][y][1] = 0 #mreset the counted flag

# print("result is", flashes)

#second part
for i in range(300):
    flashes = 0
    for x in range (length):
        for y in range(width):
            if(table[x][y][1] == 0): #enters the following only if this did not flash this round
                flashes = flashes + update_val(x,y)
    for x in range (length):
        for y in range(width):
            table[x][y][1] = 0 #mreset the counted flag
    if(flashes == 100):
        print("all octopuses flashed at iteration", i+1, "this is your result")
        


