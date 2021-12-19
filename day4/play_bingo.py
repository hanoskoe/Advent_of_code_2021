# open and parse the files
with open("bingo_values.txt", "r") as bingo_values_file:
    for line in bingo_values_file:
        bingo_values = [int(value) for value in line.strip().split(",")]
# bingo_values contains the respective values in the order in which they will be drawn

with open("bingo_tables.txt", "r") as bingo_tables_file:
    bingo_tables = []
    current_table = []
    for line in bingo_tables_file:
        if line.strip() != "":
            current_table.append([[int(value), 0] for value in line.split()])
        else:
            bingo_tables.append(current_table)
            current_table = []
    # adding one last table that would be forgotten otherwise
    bingo_tables.append(current_table)

# each value in bingo is a "struct" value+state(marked = 1, unmarked=0)


# now play
bingo = 0
i = 0
sum = 0
new_bingo_tables = bingo_tables

# going through all the bingo tables to get bingo.
# to get the response to part 1, just take the first bingo that shows up.
while len(bingo_tables) > 1:
    # first 4 values are harmless, there can be no bingo
    for table in bingo_tables:
        for line in table:
            for elt in line:
                if elt[0] == bingo_values[i]:
                    elt[1] = 1  # marked
    if i > 4:
        # start checking if there is bingo
        for table in bingo_tables:
            bingo = 0
            for line in table:
                # checking ofr horizontal bingo
                if (
                    (line[0][1] == 1)
                    & (line[1][1] == 1)
                    & (line[2][1] == 1)
                    & (line[3][1] == 1)
                    & (line[4][1] == 1)
                ):
                    bingo = 1
                    print("found bingo on line", line, "in table", table)
                    print("removing this table from all bingos")
                    new_bingo_tables.remove(table)
                    for line in table:
                        for elt in line:
                            if elt[1] == 0:
                                sum = sum + elt[0]
                    print("result is", sum * bingo_values[i])
            if (
                bingo == 0
            ):  # only if bingo not found yet in this table, check for vertical bingo
                for k in range(0, 5):
                    if (
                        table[0][k][1]
                        == 1 & table[1][k][1]
                        == 1 & table[2][k][1]
                        == 1 & table[3][k][1]
                        == 1 & table[4][k][1]
                        == 1
                    ):
                        bingo = 1
                        print("found bingo on a column,in table", table)
                        print("removing this table from all bingos")
                        new_bingo_tables.remove(table)
                        for line in table:
                            for elt in line:
                                if elt[1] == 0:
                                    sum = sum + elt[0]
                        print("result is", sum * bingo_values[i])
        bingo_tables = new_bingo_tables
    i = i + 1
print("there is only one table that did not have bingo:", bingo_tables)

# now call as many values as necessary until this table eventually gets a bingo as well
bingo = 0
while bingo == 0:
    for i2 in bingo_tables[0]:
        for i3 in i2:
            if i3[0] == bingo_values[i]:
                i3[1] = 1  # marked
    for i2 in bingo_tables[0]:
        if (
            (i2[0][1] == 1)
            & (i2[1][1] == 1)
            & (i2[2][1] == 1)
            & (i2[3][1] == 1)
            & (i2[4][1] == 1)
        ):
            bingo = 1
            print("Final bingo found on line")
    if bingo == 0:  # only if bingo not found yet in this table
        i1 = bingo_tables[0]
        for k in range(0, 5):
            if (
                i1[0][k][1]
                == 1 & i1[1][k][1]
                == 1 & i1[2][k][1]
                == 1 & i1[3][k][1]
                == 1 & i1[4][k][1]
                == 1
            ):
                bingo = 1
                print("Final bingo found on column")
    i = i + 1

sum = 0
for line in bingo_tables[0]:
    for elt in line:
        if elt[1] == 0:
            sum = sum + elt[0]
print("result of the 2nd part is", sum * bingo_values[i - 1])
