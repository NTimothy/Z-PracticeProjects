
def readFile():
    try:
        f = open(r"02.txt", "r")
        line = f.readline()
        dir = []
        val = []
        count = 0
        while line:
            dir.append(line[:(len(line)-3)])
            val.append(int(line[(len(line)-2):]))
            line = f.readline()
            count +=1
    finally:
        f.close()
        return dir,val, count

def move_sub(a,b,c,x,z):
    i = 0
    while i < c:
        if a[i] == "forward":
            x += b[i]
        elif a[i] == "up":
            z += b[i]
        elif a[i] == "down":
            z -= b[i]
        else:
            return x,z
        # print(i, "|", x, z)
        i += 1
    return x,z

def move_sub_2(a,b,c):
    i, aim, x, z = 0,0,0,0
    while i < c:
        if a[i] == "forward":
            x += b[i]
            z += aim * b[i]
        elif a[i] == "up":
            aim += b[i]
        elif a[i] == "down":
            aim -= b[i]
        else:
            return x,z
        i += 1
    return x,z


#Part 1
a,b,c = readFile()
x,z = move_sub(a,b,c,0,0)
ans = abs(x*z)
print(f"Part 1: {ans}")

#Part 2
i,j = move_sub_2(a,b,c)
ans_2 = (-1)*i*j
print(f"Part 2: {ans_2}")
