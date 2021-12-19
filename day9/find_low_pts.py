
#open the files and load content
input_file = open('/home/eva/Documents/Coding_advent/day9/input.txt', 'r')
Lines = input_file.readlines()

result = 0

for line in range(len(Lines)):
    if(line == 0):
        #first line: only check the below line(2-3 neighbors)
        if(Lines[line][0] < Lines[line][1]):
            #elt 0
            if (Lines[line][0] < Lines[(line+1)][0]):
                print("found local minima:", int(Lines[line][0]))
                result = result+ int(Lines[line][0])+1
        for elt in range(1, len(Lines[line])-2):
            # print("looking at string", Lines[line][elt])
            #testing for elements that are not in the corner
            if(Lines[line][elt] < Lines[line][elt+1]):
                if(Lines[line][elt] < Lines[line][elt-1]):
                    if (Lines[line][elt] < Lines[(line+1)][elt]):
                        print("found local minima:", int(Lines[line][elt]))
                        result = result+ int(Lines[line][elt])+1
        if(Lines[line][len(Lines[line])-2] < Lines[line][len(Lines[line])-3]):
            # print("looking at string", Lines[line][len(Lines[line])-2])
            #elt len(Lines[line])
            if (Lines[line][len(Lines[line])-2] < Lines[(line+1)][len(Lines[line])-2]):
                print("found local minima:", int(Lines[line][len(Lines[line])-2]))
                result = result+ int(Lines[line][len(Lines[line])-2])+1
    elif(line == len(Lines)-1):
        #last line: only check above line
        if(Lines[line][0] < Lines[line][1]):
            #elt 0
            if (Lines[line][0] < Lines[(line-1)][0]):
                print("found local minima:", int(Lines[line][0]))
                result = result+ int(Lines[line][0])+1
        for elt in range(1, len(Lines[line])-2):
            #testing for elements that are not in the corner
            if(Lines[line][elt] < Lines[line][elt+1]):
                if(Lines[line][elt] < Lines[line][elt-1]):
                    if (Lines[line][elt] < Lines[(line-1)][elt]):
                        print("found local minima:", int(Lines[line][elt]))
                        result = result+ int(Lines[line][elt])+1
        if(Lines[line][len(Lines[line])-2] < Lines[line][len(Lines[line])-3]):
            #elt len(Lines[line])
            if (Lines[line][len(Lines[line])-1] < Lines[(line-1)][len(Lines[line])-2]):
                print("found local minima:", int(Lines[line][len(Lines[line])-2]))
                result = result+ int(Lines[line][len(Lines[line])-2])+1
    else:
        #normal line
        if(Lines[line][0] < Lines[line][1]):
            #elt 0
            if (Lines[line][0] < Lines[(line-1)][0]):
                if (Lines[line][0] < Lines[(line+1)][0]):
                    print("found local minima:", int(Lines[line][0]))
                    result = result+ int(Lines[line][0])+1
        for elt in range(1, len(Lines[line])-1):
            #testing for elements that are not in the corner
            if(Lines[line][elt] < Lines[line][elt+1]):
                if(Lines[line][elt] < Lines[line][elt-1]):
                    if (Lines[line][elt] < Lines[(line-1)][elt]):
                        if (Lines[line][elt] < Lines[(line+1)][elt]):
                            print("found local minima:", int(Lines[line][elt]))
                            result = result+ int(Lines[line][elt])+1
        if(Lines[line][len(Lines[line])-2] < Lines[line][len(Lines[line])-3]):
            #elt len(Lines[line])
            if (Lines[line][len(Lines[line])-2] < Lines[(line-1)][len(Lines[line])-2]):
                if (Lines[line][len(Lines[line])-2] < Lines[(line+1)][len(Lines[line])-2]):
                    print("found local minima:", int(Lines[line][len(Lines[line])-2]))
                    result = result+ int(Lines[line][len(Lines[line])-2])+1

print("result is", result)
        
        



