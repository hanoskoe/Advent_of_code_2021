# open the files and load content
input_file = open("/home/eva/Documents/Coding_advent/day9/input.txt", "r")
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
    table.append(current_list)


def get_adjacent(x, y):
    # print("calling get_adjacent on", x, y)
    vector_list = [(0, 1), (1, 0), (-1, 0), (0, -1)]
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
    print("Returning adjacent points", adjacent_pts)
    return adjacent_pts


def is_minimal(x, y):
    adjacent_pts = get_adjacent(x, y)
    current_val = table[x][y][0]
    for point in adjacent_pts:
        # print("checking point", point, "in adjacent points")
        if table[point[0]][point[1]][0] <= current_val:
            return 0
    return 1


def is_bassin_pt(x, y):
    if x < 0 or y < 0 or x >= length or y >= width:
        return 0
    elif table[x][y][0] == 9:
        return 0
    else:
        return 1


def calculate_bassin_size(x, y):
    # for calculating the bassin size around the local minima x,y
    # for each direction go until you hit table boundary or 9
    ret_value = 1
    table[x][y][1] = 1  # marking this point as counted
    if is_bassin_pt(x, y):
        adjacent_pts = get_adjacent(x, y)
        for point in adjacent_pts:
            if table[point[0]][point[1]][1] == 0:
                ret_value = ret_value + calculate_bassin_size(point[0], point[1])
                table[point[0]][point[1]][1] = 1
        return ret_value
    else:
        return 0


result = 0
table_sizes = []
for x_coord in range(length):
    for y_coord in range(width):
        print("testing coords x", x_coord, "y", y_coord)
        if is_minimal(x_coord, y_coord):
            current_val = table[x_coord][y_coord][0]
            print("found local minima:", current_val)
            # result = result+ current_val+1
            table_sizes.append(calculate_bassin_size(x_coord, y_coord))

table_sizes.sort()
table_sizes.reverse()
print("table sizes are as follow:", table_sizes)
result = table_sizes[0] * table_sizes[1] * table_sizes[2]
print("result is", result)


# fonction get_adjacent(x,y) - returns list of x,y coords around this one (can return 2,3, or 4)
# fonction is_minimal(x,y) to know if that point is a local minima


# itere sur tous les x,y et regarde si c'est minimal ou pas
