import collections
import functools
import operator
import string

# open and parse the file
with open("input.txt", "r") as input_file:
    rules_dict = {}
    for rule in input_file:
        key, item = rule.strip().split(" -> ")
        rules_dict[key] = item

print("rules dict is", rules_dict)

# initial polymer
# initial_polymer = "NNCB" #test polymer
initial_polymer = "OFSVVSFOCBNONHKFHNPK"


def insert_new(polymer):
    new_polymer = ""
    for i in range(len(polymer) - 1):
        pair = polymer[i : i + 2]
        new_polymer = new_polymer + pair[0] + rules_dict[pair]
    new_polymer = new_polymer + pair[1]
    return new_polymer


def merge_dicts(list_dicts):
    return dict(functools.reduce(operator.add, map(collections.Counter, list_dicts)))


memo = {}


def insert_new_rec(pair, n):
    # insert the new proteins into the polymer pair and return the polymer this creates
    # what about creating the pairs from the first one and then letting them go through recursivity, then getting them back and just eliminate the
    if (pair, n) in memo:
        return memo[(pair, n)]
    else:
        if n == 0:
            return {}
        else:
            count_dict = {}
            count_dict[rules_dict[pair]] = 1
            new_polymer = pair[0] + rules_dict[pair] + pair[1]
            new_count_dict1 = insert_new_rec(new_polymer[0:2], n - 1)
            new_count_dict2 = insert_new_rec(new_polymer[1:3], n - 1)
            count_dict = merge_dicts([new_count_dict1, new_count_dict2, count_dict])
            memo[(pair, n)] = count_dict
            return count_dict


count_dict = {}
for i in range(len(initial_polymer) - 1):
    pair = initial_polymer[i : i + 2]
    new_dict = insert_new_rec(pair, 40)
    count_dict = merge_dicts([count_dict, new_dict])
for str in initial_polymer:
    count_dict[str] = count_dict[str] + 1

print("count_dict is", count_dict)
max_occurences = 0
min_occurences = count_dict["N"]
for (letter, count) in count_dict.items():
    if count > max_occurences:
        max_occurences = count
    elif (count < min_occurences) and count > 1:
        min_occurences = count

print("result is", max_occurences - min_occurences)
