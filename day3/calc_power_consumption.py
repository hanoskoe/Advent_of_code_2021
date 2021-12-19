# open and parse the file
with open("bin_values.txt", "r") as bin_file:
    bin_values = [value.strip() for value in bin_file]


def calculate_gamma_epsilon(bin_values):
    gamma = ""
    epsilon = ""
    for i in range(0, len(bin_values[0])):
        num_0s = 0
        for bin_value in bin_values:
            if bin_value[i] == "0":
                num_0s = num_0s + 1
        if num_0s > 500:
            gamma = gamma + "0"
            epsilon = epsilon + "1"
        else:
            gamma = gamma + "1"
            epsilon = epsilon + "0"
    return gamma, epsilon


gamma, epsilon = calculate_gamma_epsilon(bin_values)
print("result of the first part is:", int(gamma, 2) * int(epsilon, 2))


oxygen_list = bin_values
new_oxygen_list = []
co2_list = bin_values
new_co2_list = []
gamma, epsilon = calculate_gamma_epsilon(bin_values)
i = 0
num_0s = 0
num_1s = 0

while len(oxygen_list) > 1:
    for elt in oxygen_list:
        if elt[i] == gamma[i]:
            new_oxygen_list.append(elt)
    i = i + 1
    oxygen_list = new_oxygen_list
    new_oxygen_list = []
    gamma = ""
    for index in range(0, 12):
        num_0s = 0
        num_1s = 0
        for line in oxygen_list:
            if line[index] == "0":
                num_0s = num_0s + 1
            else:
                num_1s = num_1s + 1
        if num_0s > num_1s:
            gamma = gamma + "0"
        else:
            gamma = gamma + "1"
print(
    "the only element in oxygen list is",
    oxygen_list,
    "which is",
    int(oxygen_list[0], 2),
    "in decimal",
)

i = 0
while len(co2_list) > 1:
    for elt in co2_list:
        if elt[i] == epsilon[i]:
            new_co2_list.append(elt)
    i = i + 1
    co2_list = new_co2_list
    new_co2_list = []
    epsilon = ""
    for index in range(0, 12):
        num_0s = 0
        num_1s = 0
        for line in co2_list:
            if line[index] == "0":
                num_0s = num_0s + 1
            else:
                num_1s = num_1s + 1
        if num_0s > num_1s:
            epsilon = epsilon + "1"
        else:
            epsilon = epsilon + "0"
print(
    "the only element in co2 list is",
    co2_list,
    "which is",
    int(co2_list[0], 2),
    "in decimal",
)

print(
    "the life support index (result of the 2nd part) is",
    int(co2_list[0], 2) * int(oxygen_list[0], 2),
)
