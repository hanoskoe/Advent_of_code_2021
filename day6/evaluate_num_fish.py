#create a class for each line segment
class Shrimp:
    
    def __init__(self,init_counter):
        self.decounter = init_counter
    
    def __str__(self):
        return f"{self.decounter}"
    
    def next_day(self, shrimps):
        if (self.decounter == 0):
            #reset and create new shrimp
            self.decounter = 6
            shrimps.append(Shrimp(9))
        else:
            self.decounter = self.decounter-1
    

#open the files and load content
input_file = open('/home/eva/Documents/Coding_advent/day6/test.txt', 'r')
Lines = input_file.readlines()
init_shrimps = Lines[0].split(",")

shrimps = []
for init_shrimp in init_shrimps:
    shrimps.append(Shrimp(int(init_shrimp)))
    #print("added to list shrimp with decounter", init_shrimp)

memo = {}

def calculate_num_children(shrimp, days):
    if (shrimp.decounter, days) in memo:
        return memo[(shrimp.decounter, days)]
    else:
        decounter = shrimp.decounter
        if days == 0:
            return 1
        else:
            if (shrimp.decounter == 0):
                shrimp.decounter = 6
                baby_shrimp = Shrimp(8)
                count = calculate_num_children(shrimp, days-1) + calculate_num_children(baby_shrimp, days-1)
            else:
                shrimp.decounter = shrimp.decounter -1
                count =  calculate_num_children(shrimp, days-1)
            memo[(decounter, days)] = count
    return count
    
# for i in range (1, 257):
#     for shrimp in shrimps:
#         shrimp.next_day(shrimps)
#     #print("on day", i, "there are", len(shrimps),"shrimps:", *shrimps)
#     print("on day", i, "there are", len(shrimps))
# count0 = 0
# for shrimp in shrimps:
#     count0 = count0+calculate_num_children(shrimp, 256)

# print(count0)
# print(memo)

shrimp1=Shrimp(1)
count1 = calculate_num_children(shrimp1, 256)
print("initial value 1 results in", count1, "shrimps")

shrimp2=Shrimp(2)
count2 = calculate_num_children(shrimp2, 256)
print("initial value 2 results in", count2, "shrimps")

shrimp3=Shrimp(3)
count3 = calculate_num_children(shrimp3, 256)
print("initial value 3 results in", count3, "shrimps")

shrimp4=Shrimp(4)
count4 = calculate_num_children(shrimp4, 256)
print("initial value 4 results in", count4, "shrimps")

shrimp5=Shrimp(5)
count5 = calculate_num_children(shrimp5, 256)
print("initial value 5 results in", count5, "shrimps")

print("result is", count1*83+count2*51+count3*58+count4*54+count5*54)

print(len(memo))