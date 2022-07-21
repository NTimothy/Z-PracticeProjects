import numpy as np
np.set_printoptions(linewidth=300)

f = open(r"C:\Users\ntimo\PycharmProjects\Testing\Z-PracticeProjects\day8", "r")
data = []
while True:
    byte = f.read(1)
    if not byte:
        break
    data.append(int(byte))  # list data contains raw integer input
   
# should return 100 layers, 150 pixels pixels; included in case input data amount is different lengths
def layerCount(data,length,width):
    total_area = len(data)
    area = length*width
    count = int(total_area/(area))
    return count,area                   
    
def newArr(type, area, row,col):
    if type == 0:
        arr = np.zeros(area).reshape(row, col)
    return arr

row = h = 6   # height aka rows
col = w = 25   # width aka columns
layers,area = layerCount(data,w,h)

allDict = {}
zeroDict = {}
_i=0

for lay in range(layers):
    x = newArr(0, area, 6, 25)              # loops to create temporary 2D numpy array from data
    for row in range(h):
        for col in range(w):
            x[row][col] = data[_i]
            key_lay = f'L{lay}|{data[_i]}'
            if key_lay in allDict:
                allDict[key_lay] += 1          # counts frequency of the data value
                if data[_i] ==0:               
                    zeroDict[key_lay]+=1      # separate dictionary for zeros only
            else:
                allDict[key_lay] = 1
                if data[_i] ==0:
                    zeroDict[key_lay]=1
            _i += 1

# for key, value in allDict.items():
#     print(f"{key} : {value}")

# for key,value in zeroDict.items():
#     print(f"{key} : {value}")

print(min(zeroDict, key=allDict.get))       # prints lowest key value in dictionary containing only zero digit values
# Part 1 Answer: 19 * 125 = 2375


### Part 2 ###
_i=0
z = np.full((6,26),-1)                      # Base Image layer
x = newArr(0, area, 6, 25)                  # temporary x array
for lay in range(layers):
    for row in range(h):
        for col in range(w):                
            x[row][col] = data[_i]          # populates temporary x array with data
            _i += 1
    for row in range(h):
        for col in range(w):
            if z[row][col] == -1 and x[row][col] != 2:              # Populates base image layer if pixel is not defined
                z[row][col] = x[row][col]
    x = newArr(0, area, 6, 25)                                      # Refresh array for nexy=t layer

print(z)
# Output:
# [[ 1  1  1  0  0  1  0  0  1  0  1  0  0  1  0  1  1  1  0  0  1  0  0  0  1 -1]
#  [ 1  0  0  1  0  1  0  1  0  0  1  0  0  1  0  1  0  0  1  0  1  0  0  0  1 -1]
#  [ 1  0  0  1  0  1  1  0  0  0  1  1  1  1  0  1  0  0  1  0  0  1  0  1  0 -1]
#  [ 1  1  1  0  0  1  0  1  0  0  1  0  0  1  0  1  1  1  0  0  0  0  1  0  0 -1]
#  [ 1  0  1  0  0  1  0  1  0  0  1  0  0  1  0  1  0  1  0  0  0  0  1  0  0 -1]
#  [ 1  0  0  1  0  1  0  0  1  0  1  0  0  1  0  1  0  0  1  0  0  0  1  0  0 -1]]
