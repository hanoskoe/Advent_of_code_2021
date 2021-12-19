import sys


def calculate_new_value(value, shift):
    if value + shift < 10:
        return value + shift
    else:
        return (value + shift) - 9


def increase_graph_size(graph, factor):
    new_graph = [[0] * (factor * len(graph[0])) for _ in range(factor * len(graph))]
    new_stripe = [[0] * (factor * len(graph[0])) for _ in range(len(graph))]
    # other tiles than 0 have increasing risk factor
    for k in range(factor):
        for i in range(len(graph)):
            for j in range(len(graph[0])):
                new_stripe[i][len(graph[0]) * k + j] = calculate_new_value(
                    graph[i][j], k
                )
    # at this stage I have a graph of 5 tiles in length and 1 tile in width
    # print("new stripe is:")
    # for line in new_stripe:
    #     print(line)

    for k in range(factor):
        for i in range(len(new_stripe)):
            for j in range(len(new_stripe[0])):
                new_graph[k * len(new_stripe) + i][j] = calculate_new_value(
                    new_stripe[i][j], k
                )
    # at this stage I have a graph of 5 tiles in length and 5 tiles in width
    # print("new graph is:")
    # for line in new_graph:
    #     print(line)
    return new_graph


def get_adjacent(x, y, graph):
    vector_list = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    adjacent_pts = []
    for vector in vector_list:
        new_point = (x + vector[0], y + vector[1])
        if (
            new_point[0] >= 0
            and new_point[1] >= 0
            and new_point[0] < len(graph)
            and new_point[1] < len(graph[0])
        ):
            adjacent_pts.append(new_point)
    return adjacent_pts


def order_by_min_dist(list_points, dist_dict):
    ordered_list_points = []
    # takes the points in the list and orders them according to the shortest distance in dist
    while len(list_points) > 0:
        min_dist = dist_dict[list_points[0]]
        min_point = list_points[0]
        for point in list_points:
            if dist_dict[point] <= min_dist:
                min_dist = dist_dict[point]
                min_point = point
        ordered_list_points.append(min_point)
        list_points.remove(min_point)
    return ordered_list_points


def dijkstra(graph, init_point_coord, end_point_coord):
    visited_nodes_dict = {}
    # this dictionary will contain the distances to reach each node(coordinate)
    distances_dict = {}
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            distances_dict[(i, j)] = sys.maxsize
            visited_nodes_dict[(i, j)] = False
    distances_dict[init_point_coord] = 0

    # for all points in the graph:
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if visited_nodes_dict[(i, j)] == False:
                adjacent_nodes = get_adjacent(i, j, graph)
                # print("adjacent nodes are", adjacent_nodes)
                # updating adjacent nodes
                for node in adjacent_nodes:
                    if (
                        distances_dict[node]
                        > distances_dict[(i, j)] + graph[node[0]][node[1]]
                    ):
                        distances_dict[node] = (
                            distances_dict[(i, j)] + graph[node[0]][node[1]]
                        )
                visited_nodes_dict[(i, j)] = True
                # order adjacent nodes by smallest distance
                ordered_adjacent_nodes = order_by_min_dist(
                    adjacent_nodes, distances_dict
                )
                # go through all neighbors from smallest distance to biggest distance
                for neighbor_node in ordered_adjacent_nodes:
                    if visited_nodes_dict[neighbor_node] == False:
                        neighbor_adjacent_nodes = get_adjacent(
                            neighbor_node[0], neighbor_node[1], graph
                        )
                        for node in neighbor_adjacent_nodes:
                            if (
                                distances_dict[node]
                                > distances_dict[neighbor_node]
                                + graph[node[0]][node[1]]
                            ):
                                distances_dict[node] = (
                                    distances_dict[neighbor_node]
                                    + graph[node[0]][node[1]]
                                )
                        # visited_nodes_dict[neighbor_node] = True
    # print("visited nodes are", visited_nodes)
    return distances_dict[end_point_coord]


# open and parse the file
with open("input.txt", "r") as input_file:
    risk_graph = []
    for line in input_file:
        current_risk_line = []
        for risk_factor in line.strip().split():
            for digit in risk_factor:
                current_risk_line.append(int(digit))
        risk_graph.append(current_risk_line)
# for line in risk_graph:
#     print(line)


print(
    "length and width of risk_graph are respectively",
    len(risk_graph),
    len(risk_graph[0]),
)


result1 = dijkstra(risk_graph, (0, 0), (len(risk_graph) - 1, len(risk_graph[0]) - 1))
print("result of the first part is", result1)

print("increasing graph size")
risk_graph2 = increase_graph_size(risk_graph, 5)
print(
    "Now, length and width of risk_graph are respectively",
    len(risk_graph2),
    len(risk_graph2[0]),
)


result2 = dijkstra(risk_graph2, (0, 0), (len(risk_graph2) - 1, len(risk_graph2[0]) - 1))
print("result of the second part is", result2)
print("2930 is too high")

# to optimize this: heap for ensemble (point, distance)
# probably still doing sth wrong: I think what I do here is not exactly Dijstra's algorithm
