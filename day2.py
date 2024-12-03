# Red Nosed Reports
# Part 1

with open('day2_input.txt', 'r') as file:
    lines = file.readlines()

# Check if all lines are increasing or decreasing
n_safe = 0
for line in lines:
    numbers = list(map(int, line.split()))

    difference = []
    decreasing = True
    increasing = True
    bad_level = 0
    n_decreasing = 0
    n_increasing = 0

    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]

        if abs(diff) > 3 or abs(diff) < 1:
            increasing = False
            decreasing = False
            bad_level += 1

        if diff > 0:
            decreasing = False
            n_decreasing += 1
        elif diff < 0:
            increasing = False
            n_increasing += 1

        bad_level += min(n_decreasing, n_increasing)
        # print(bad_level)

        difference.append(numbers[i + 1] - numbers[i])
    
    if increasing or decreasing:
        n_safe += 1 
    elif bad_level <= 1:
        n_safe += 1
print(n_safe)

# Part 2
