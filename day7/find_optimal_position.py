

#open the files and load content
input_file = open('/home/eva/Documents/Coding_advent/day7/crabs_init_positions.txt', 'r')
Lines = input_file.readlines()
init_crab_positions = Lines[0].split(",")
#convert them to int
init_crab_positions = list(map(int, init_crab_positions))

#find the most optimal solution
#sol 1:
# for each position, for each crab calculate the number of fuels they need to get there
# you can optimize by checking if that's bigger than sth already found

max_position = max(init_crab_positions)
min_position = min(init_crab_positions)
dict_of_fuels = {}
current_min = 0

#initialize dict
for i in range( min_position, max_position+1):
    dict_of_fuels[i] = 0

for i in range( min_position, max_position+1):
    for crab in init_crab_positions:
        dict_of_fuels[i] = dict_of_fuels[i] + ((abs(i - crab))*(abs(i-crab)+1))/2 #sum of numbers from 1 to n = (n*(n+1))/2
    if (i== min_position):
        current_min = dict_of_fuels[i]
        result = i
    else:
        if (dict_of_fuels[i] <current_min):
            current_min = dict_of_fuels[i]
            result = i

print("result is position", result, "and used", dict_of_fuels[result], "units of fuel" )