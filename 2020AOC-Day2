# Advent of Code 2020
# --- Day 2: Password Philosophy ---

def readFile():
    try:
        f = open(r"2020_day2", "r")
        line = f.readline()
        p_input = []
        count = 0
        while line:
            p_input.append(str(line))
            line = f.readline()
            count +=1
    finally:
        f.close()
        return p_input, count


# Function to evaluate if password meets "corporate policy"
# if password has the allowed number of occurrences of a character
def validatePass(min,max,char,password):
    count = 0
    c = str(char)
    p = str(password)

    # Counts occurrences of a given character in a password
    for i in p:
        if i == c:
            count += 1
    if (count >= min) and (count <= max):
        return True
    else:
        return False


def countValidated1(_input, _total):
    ele = 0
    validated = 0
    try:
        while ele < _total:
            x = _input[ele].split()
            min = int(x[0].split("-")[0])
            max = int(x[0].split("-")[1])
            char = str(x[1].split(":")[0])
            password = str(x[2])
            check = validatePass(min,max,char,password)
            if check:
                validated +=1
            ele+=1
    finally:
        return validated


input,total = readFile()
print("Part 1 Answer:", countValidated1(input,total))


## Part 2

# Checks if given char is present in only one of the positions
# within the given password
def validatePass2(pos1, pos2, char, password):
    if password[pos1-1] == char and password[pos2-1] != char:
        return True
    elif password[pos1-1] != char and password[pos2-1] == char:
        return True
    else:
        return False


# Counts number of validated passwords
def countValidated2(_input, _total):
    ele = 0
    validated = 0
    try:
        while ele < _total:
            x = _input[ele].split()
            pos1 = int(x[0].split("-")[0])
            pos2 = int(x[0].split("-")[1])
            char = str(x[1].split(":")[0])
            password = str(x[2])
            check = validatePass2(pos1,pos2,char,password)
            if check:
                validated +=1
            ele+=1
    finally:
        return validated


print("Part 2 Answer:", countValidated2(input,total))
