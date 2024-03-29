def read_file():
    f = open(r"04.txt", "r")
    data = []
    count = 0
    try:
        line = f.readline()
        while line:
            data.append(str(line.split("\n")[0]))
            line = f.readline()
            count +=1
    finally:
        f.close()
        return data, count

def clean_data(p_input,boards):

    # Re-orders puzzle input into a list of integers
    bingo_values = []
    num = ""
    for char in p_input:
        if char == ",":
            bingo_values.append(int(num))
            num = ""
        elif char != ",":
            num += str(char)


    board_values = []
    _count = 0
    num = ""
    # Re-orders data into a single list containing only strings
    for line in boards:
        for char in line:
            _count += 1
            if char == " ":
                board_values.append(num)
                num = ""
            elif _count == 14:
                num = str(num) + str(char)
                board_values.append(num)
                _count = 0
                num = ""
            elif char != " ":
                num = str(num) + str(char)

    # Removes all empty elements in list
    for _element in board_values:
        if _element == "":
            board_values.remove(_element)

    # 1. Create List of Boards
    # 2. Parses through each number and organizes a List of all boards,
    # Each board contains a dict of all its rows as lists & each value as an element
    # within the list
    Boards = []
    _boardnum, _row, _num = 0, 0, 0
    while _num < len(board_values):
        if _row == 0:
            _board = {0:[],1:[],2:[],3:[],4:[]}             # Create dict with 5 keys, 1 for each row of a board
        while _row < 5:                                     # Loops until all 5 rows are completed
            _rem = _num % 5
            if _rem < 4:                                        # Fills values of row 1 by 1
                _board[_row].append(int(board_values[_num]))    
            elif _rem ==4:                                      # At the end of a row
                _board[_row].append(int(board_values[_num]))    
                _row+=1                                         #   move to next row
            if (_row == 4) and (_rem==4):                       # At the end of the 5th row
                Boards.append(_board)                           #   add to list of all bingo boards
            _num +=1

        _row = 0
        _boardnum +=1
    return Boards



def part_one(input,boards):
    for num in boards:
        print(num)                                              # Test output


data, count = read_file()
p_input = data[0]
Boards = clean_data(data[0],data[2:])

# Print Debug
# print(p_input)
# print(Boards)

part_one(p_input,Boards)

