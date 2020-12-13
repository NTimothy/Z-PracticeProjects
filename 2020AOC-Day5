# Advent of Code 2020
# --- Day 5: Binary Boarding ---

# Constants:
# Max rows = 128, numbered 0-127
# Max columns = 8, numbered 0-7

with open(r"2020_day5") as file:
    passes = []
    line = file.readline()
    while line:
        min_row = 0
        max_row = 127
        min_col = 0
        max_col = 7
        i = 0
        while i < 7:
            x = ((max_row+1-min_row)/2)
            if line[i] == "F":
                max_row -= x
            elif line[i] == "B":
                min_row += x
            i += 1
        while 6 < i < 10:
            x = ((max_col + 1 - min_col) / 2)
            if line[i] == "L":
                max_col -= x
            elif line[i] == "R":
                min_col += x
            i += 1
        row = min_row
        col = min_col
        seat_id = (row * 8) + col           # Calculate Seat ID
        passes.append(int(seat_id))         # Add Seat ID to list
        line = file.readline()

def find_seat(passes):
    end = passes[0] + len(passes)
    step = 0
    seat = 0
    while passes[step] < end:
        if (passes[step]+1) != passes[step+1]:
            seat = passes[step]+1
        step += 1
    return seat


passes.sort()
print("Highest Seat ID:", max(passes))  # Part 1 Ans: 818

my_seat = find_seat(passes)
print("My Seat ID:", my_seat)              # Part 2 Ans: 559

