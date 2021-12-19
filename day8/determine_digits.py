
import re

#open the files and load content
input_file = open('/home/eva/Documents/Coding_advent/day8/input.txt', 'r')
Lines = input_file.readlines()

# count = 0
# for line in Lines:
#     current_line = re.findall(r"[\w']+", line)
#     print("current line is", current_line)
#     #separate last 4 elements in the current line
#     for i in range(10,14):
#         length = len(current_line[i])
#         print("length of", current_line[i], "is", length)
#         if ((length == 2) | (length == 3) |(length == 4) | (length == 7)):
#             count = count+1
#             print("adding +1 to count")

# print("result for the first part is is", count)

#second part: need to decode really now

#sol 1 : does not work because I don't know which one is which
#1and7 gives the top value
#6 and 0 when differentiating gives the top right and middle
#3 and 4 when differentiating gives the bottom right and top left

#sol 2: 
#kind of a statistical analysis
#1 gives the right side
#a bar is present 8 times, in all values except 1 and 4 (which are recognizable)
#b bar is present 6 times, not present in 1 and 7 (recognizable)
#c bar is present 8 times, including all recognizable
#d bar is present 7 times
#e bar is present 4 times
#f bar is present 9 times
#g bar is present 7 times, not in 1, 4, 7

dict = {}

result = 0

#identify the 2 bars in 1
for line in Lines:
    dict['a'] = 0
    dict['b'] = 0
    dict['c'] = 0
    dict['d'] = 0
    dict['e'] = 0
    dict['f'] = 0
    dict['g'] = 0
    a_bar = ''
    b_bar = ''
    c_bar = ''
    d_bar = ''
    e_bar = ''
    f_bar = ''
    g_bar = ''
    string_4=''
    digits = ''
    current_line = re.findall(r"[\w']+", line)
    print("current line is", current_line)
    #the elements that I will use firstly are 0-9
    #and I need to know which values are in 1
    for i in range(10):
        elt = current_line[i]
        if ('a' in elt):
            dict['a']  = dict['a'] +1
        if('b' in elt):
            dict['b']  = dict['b'] +1
        if('c' in elt):
            dict['c']  = dict['c'] +1
        if('d' in elt):
            dict['d']  = dict['d'] +1
        if('e' in elt):
            dict['e']  = dict['e'] +1
        if('f' in elt):
            dict['f']  = dict['f'] +1
        if('g' in elt):
            dict['g']  = dict['g'] +1
        if(len(elt) == 4):
            string_4 = elt
    #print("my dictionary:", dict)
    for dict_elt in dict:
        if(dict[dict_elt] == 4):
            #dict_elt corresponds to e bar
            e_bar = dict_elt
        elif(dict[dict_elt] == 6):
            b_bar = dict_elt
        elif(dict[dict_elt] == 9):
            f_bar = dict_elt
        elif(dict[dict_elt] == 7):
            if(dict_elt in string_4):#'a' in 'abcd'
                d_bar = dict_elt
            else:
                g_bar = dict_elt #g_bar= 'a'
        elif(dict[dict_elt] == 8):
            if(dict_elt in string_4):
                c_bar = dict_elt
            else:
                a_bar = dict_elt
    for i in range(10,14):
        elt = current_line[i] 
        if (len(elt)== 2):
            digits = digits+'1'
        elif(len(elt) == 3):
            digits = digits+'7'
        elif(len(elt) == 4):
            digits = digits+'4'
        elif(len(elt) == 7):
            digits = digits+'8'
        elif(len(elt) == 5):
            if (e_bar in elt):
                digits = digits+'2'
            elif (b_bar in elt):
                digits = digits+'5'
            else:
                digits = digits+'3'
        elif(len(elt) == 6):
            if (e_bar in elt):
                if(d_bar in elt):
                    digits = digits+'6'
                else:
                    digits = digits+'0'
            else:
                digits = digits+'9'
    # print("line result is", int(digits))
    result = result + int(digits)

print("result is", result)
            



