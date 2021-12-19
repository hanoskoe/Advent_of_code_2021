
import re

#create a class for each line segment
class Segment:
    
    def __init__(self,x0,y0,x1,y1):
        self.beginning = (x0,y0)
        self.end = (x1,y1)
        self.used_points=[]
    
    def recalculate_used_points(self):
        if((self.beginning[0] == self.end[0]) | (self.beginning[1] == self.end[1])): #only needed for the first part
            for i in range (min(self.beginning[0], self.end[0]), max(self.beginning[0], self.end[0])+1):
                for j in range (min(self.beginning[1], self.end[1]), max(self.beginning[1], self.end[1])+1):
                    self.used_points.append((i,j))
        else: #in this case it's a diagonal
            i= self.beginning[0]
            j= self.beginning[1]
            while True:
                self.used_points.append((i,j))
                if (i == self.end[0]):
                    break
                else:
                    if (i <= self.end[0]):
                        i= i+1
                    else:
                        i = i-1
                    if (j <= self.end[1]):
                        j = j+1
                    else:
                        j = j-1
            print("the segment starts at point", self.beginning, "and ends at point", self.end)
            print("the current list of used points for this segment is", self.used_points)

#open the files and load content
input_coordinates_file = open('/home/eva/Documents/Coding_advent/day5/input_coordinates.txt', 'r')
Lines = input_coordinates_file.readlines()

segments = []

#read the file and populate my table of segments
for line in Lines:
    current_line = re.findall(r"[\d']+", line)
    print("current_line is", current_line)
    x0 = int(current_line[0])
    y0 = int(current_line[1])
    x1 = int(current_line[2])
    y1 = int(current_line[3])
    segments.append(Segment(x0, y0, x1, y1))

# for current_segment in segments:
#     current_segment.recalculate_used_points()

#print("segments contains", segments)

#now create a dict of all coordinates and calculate which ones are hit how many times
coord_dict = {}
for i in range(1000):
    for j in range(1000): 
        coord_dict[(i,j)] = 0
print("created dictionary")

local_max = 0
#populate the coord_dict according to all segments
for seg in segments:
    print("looking at segment starting at", seg.beginning)
    seg.recalculate_used_points()
    for coord in seg.used_points:
        coord_dict[coord] = coord_dict[coord] +1
        #print("added 1 to coordinate", coord)
        if (coord_dict[coord] > local_max):
            local_max = coord_dict[coord] 
    del seg

print("maximum value reached is", local_max)

#now count the number of values that hit this
count = 0
for i in range(1000):
    for j in range(1000): 
        if(coord_dict[(i,j)] > 1):
            count = count+1

print("result is that", count, "segments are hitting most dangerous points with value bigger than", 1)
        
