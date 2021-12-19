
import re
import random
import itertools

# open the files and load content
input_file = open("/home/eva/Documents/Coding_advent/day12/input.txt", "r")
Lines = input_file.readlines()

upper_dict = {}
lower_dict = {'start': [],
              'end' : []}

# create list of lists of ints (and you can access coordinates x, y of each int)
for line in Lines:
    clean_line = re.findall(r"[\w+']+", line)
    print("clean line is", clean_line)
    if(clean_line[0].isupper()):
        if(clean_line[0] not in upper_dict):
            upper_dict[clean_line[0]] = list()
        upper_dict[clean_line[0]].append(clean_line[1])
    else:
        if(clean_line[0] not in lower_dict):
            lower_dict[clean_line[0]] = list()
        lower_dict[clean_line[0]].append(clean_line[1])
    if(clean_line[1].isupper()):
        if(clean_line[1] not in upper_dict):
            upper_dict[clean_line[1]] = list()
        upper_dict[clean_line[1]].append(clean_line[0])
    else:
        if(clean_line[1] not in lower_dict):
            lower_dict[clean_line[1]] = list()
        lower_dict[clean_line[1]].append(clean_line[0])

print("content of upper_dict is", upper_dict)
print("content of lower dict is", lower_dict)
#create one dictionary of the small caves: who are they connected to?
#create one dictionary of big caves: who are they connected to?
#attention the paths are in both directionr(ae-start and start-ae)

#how to find a way that has not been found by anyone else?
#create struct way that will contain the steps of the way in a list
#when creating a new way, it could well start exactly the same as the previous one

#my idea here is to randomly find a way 100 times and hoping that this will find all the possibilities

#how to make sure that this will avoid to go into the small caves only once? Marked
def find_a_way_through():
    path = ['start']
    next_step = ''
    illegal_opts = ['start'] #this will contain all the small caves that have been visited once already
    while (next_step != 'end'):
        previous_step = path[-1]
        # print("previous step is", previous_step)
        if (previous_step.isupper()):
            choice_list = [x for x in upper_dict[previous_step] if x not in illegal_opts]
            # print("choice list is", choice_list)
            if (len(choice_list) == 0):
                return ['error']
            next_step = random.choice(choice_list)
        else:
            choice_list = [x for x in lower_dict[previous_step] if x not in illegal_opts]
            # print("choice list is", choice_list)
            if (len(choice_list) == 0):
                return ['error']
            next_step = random.choice(choice_list)
        if(next_step.isupper() == 0):
            illegal_opts.append(next_step)
            # print("adding", next_step, "to illegal opts")
            
        # print("next step is", next_step)
        path.append(next_step)
    return path
    
table_paths = []
for i in range(11000000):
    path = find_a_way_through()
    if (path != ['error']):
        # print("found a possible way through:", path)
        table_paths.append(path)

#go through the table of paths and only keep the unique ones
table_paths.sort()
final_ways = list(table_paths for table_paths,_ in itertools.groupby(table_paths))
print("Found paths are as follows")
for way in final_ways:
    print(way)
print("result is", len(final_ways))