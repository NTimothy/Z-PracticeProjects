# Advent of Code 2020
# Day 1: Report Repair

def readFile():
    try:
        f = open(r"2020_day1", "r")
        line = f.readline()
        p_input = []
        count = 0
        while line:
            p_input.append(int(line))
            line = f.readline()
            count +=1
    finally:
        f.close()
        return p_input, count

def testPart1(x,y):
    sum = x + y
    if sum == 2020:
        product = x*y
        return product
    else:
        return -1

p_input, total = readFile()

count1 = 0
count2 = 0
while count1 < total:
    while count2 < total:
       ans = testPart1(p_input[count1],p_input[count2])
       if ans != -1:
           print(ans)
           print(p_input[count1], "|", p_input[count2])
           count1 = total+1
           count2 = total+1
       count2 +=1
    count2 = 0
    count1 +=1


## Part 2
count1 = 0
count2 = 0
count3 = 0

while count1 < total:
    while count2 < total:
        while count3 < total:
            sum = p_input[count1]+p_input[count2]+p_input[count3]
            if sum == 2020:
                product = p_input[count1]*p_input[count2]*p_input[count3]
                print(product)
                print(p_input[count1], "|", p_input[count2], "|", p_input[count3])
                count1, count2, count3 = total+1, total+1, total+1
            else:
                count3 +=1
        count2 +=1
        count3 = 0
    count1 +=1
    count2 = 0

  
