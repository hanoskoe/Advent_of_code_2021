# open the files and load content
input_file = open("/home/eva/Documents/Coding_advent/day10/input.txt", "r")
Lines = input_file.readlines()

opening_elts = ['(', '[', '{', '<']
closing_elts = [')', ']', '}', '>']

incomplete_price = [1,2,3,4]
failed_elts = []
closing_queue = []
incomplete_scores = []

for line in Lines:
    ignore_line = 0
    for elt in line.strip():
        # print("looking at elt", elt)
        if elt in closing_elts:
            # print("it's a closing element, testing it against the first element of the closing queue", closing_queue[-1])
            # print("closing queue state is", closing_queue)
            if(closing_queue[-1] == elt):
                closing_queue.pop((-1))
                # print("closing queue state is", closing_queue)
            else:
                failed_elts.append(elt)
                ignore_line = 1
                break
        else:#it's an opening element
            closing_queue.append(closing_elts[opening_elts.index(elt)])
    #at the end of the queue check if there are any missing elements in the queue
    #if yes, calculate the corresponding score and add append it to the incomplete_scores list
    if ignore_line == 0 and len(closing_queue) != 0:
        score = 0
        while(len(closing_queue) != 0):
            print("closing queue not empty. contains", closing_queue)
            score = 5*score+incomplete_price[closing_elts.index(closing_queue[-1])]
            closing_queue.pop((-1))
        incomplete_scores.append(score)
    closing_queue = []


#first part

# print("failed elts are", failed_elts)
# count0 = failed_elts.count(')')
# count1 = failed_elts.count(']')
# count2 = failed_elts.count('}')
# count3 = failed_elts.count('>')
# print("count0=", count0)
# print("count1=", count1)
# print("count2=", count2)
# print("count3=", count3)

# result = 3*count0+57*count1+1197*count2+25137*count3
# print("result is", result)

#second part
print("incomplete scores are", incomplete_scores)
incomplete_scores.sort()
while len(incomplete_scores) > 1:
    incomplete_scores.pop(-1)
    incomplete_scores.pop(0)
    
result = incomplete_scores[0]
print("result is", result)
print("already tried 1110756183 but was too high")
            
            
    
    


