import re

# Day 3: Mull it over 
with open('day4_input.txt', 'r') as file:
    input = file.read()
    lines = input.splitlines()

horizontal = re.findall(r'(?=(XMAS))', input)
backwards = re.findall(r'(?=(SAMX))', input)

count = 0
for row in range(len(lines)):
    for col in range(len(lines[row])):
        # Check vertical down match
        if (row + 3) < len(lines) and lines[row][col] == 'X' \
            and lines[row + 1][col] == 'M' and lines[row + 2][col] == 'A' and lines[row + 3][col] == 'S':
            count += 1
        # Check diagonal match (down-right)
        if (row + 3) < len(lines) and (col + 3) < len(lines[row]) and lines[row][col] == 'X' \
            and lines[row + 1][col + 1] == 'M' and lines[row + 2][col + 2] == 'A' and lines[row + 3][col + 3] == 'S':
            count += 1
        # Check diagonal match (down-left)
        if col >= 3 and (row + 3) < len(lines) and lines[row][col] == 'X' and lines[row + 1][col - 1] == 'M' \
            and lines[row + 2][col - 2] == 'A' and lines[row + 3][col - 3] == 'S':
            count += 1
        # Check vertical up match
        if row >= 3 and lines[row][col] == 'X' and lines[row - 1][col] == 'M' \
            and lines[row - 2][col] == 'A' and lines[row - 3][col] == 'S':
            count += 1
        # Check diagonal match (up-right)
        if row >= 3 and (col + 3) < len(lines[row]) and lines[row][col] == 'X' and lines[row - 1][col + 1] == 'M' \
            and lines[row - 2][col + 2] == 'A' and lines[row - 3][col + 3] == 'S':
            count += 1
        # Check diagonal match (up-left)
        if col >= 3 and row >= 3 and lines[row][col] == 'X' and lines[row - 1][col - 1] == 'M' \
            and lines[row - 2][col - 2] == 'A' and lines[row - 3][col - 3] == 'S':
            count += 1        

total = len(horizontal) + len(backwards) + count 
print(total)

# Part 2 
new_count = 0
for row in range(len(lines)):
    for col in range(len(lines[row])):
        if lines[row][col] == 'A':
            if row + 1 < len(lines) and col + 1 < len(lines[row]) and row - 1 >= 0 and col - 1 >= 0:
                if lines[row + 1][col - 1] == "S" and lines[row + 1][col + 1] == "M" \
                    and lines[row - 1][col - 1] == "S" and lines[row - 1][col + 1] == "M":
                    new_count += 1
                if lines[row + 1][col - 1] == "M" and lines[row + 1][col + 1] == "S" \
                    and lines[row - 1][col - 1] == "M" and lines[row - 1][col + 1] == "S":
                    new_count += 1
                if lines[row + 1][col - 1] == "M" and lines[row + 1][col + 1] == "M" \
                    and lines[row - 1][col - 1] == "S" and lines[row - 1][col + 1] == "S":
                    new_count += 1
                if lines[row + 1][col - 1] == "S" and lines[row + 1][col + 1] == "S" \
                    and lines[row - 1][col - 1] == "M" and lines[row - 1][col + 1] == "M":
                    new_count += 1
print(new_count)