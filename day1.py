# Historian Hysteria
# Part 1
left_number = []
right_number = []
with open('day1_input.txt', 'r') as file:
    lines = file.readlines()

total_distance = 0

for line in lines:
    numbers = line.split()
    left_number.append(int(numbers[0]))
    right_number.append(int(numbers[1]))

left_number.sort()
right_number.sort()

for number, number2 in zip(left_number, right_number):
    distance = abs(number2 - number)
    total_distance += distance

print(total_distance)

# Part 2
total_similarity = 0

unique_left = set(left_number)
for number in unique_left:
    number_count = right_number.count(number)
    similarity =  number * number_count
    total_similarity += similarity

print(total_similarity)

    