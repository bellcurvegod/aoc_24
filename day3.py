import re

# Day 3: Mull it over 
with open('day3_input.txt', 'r') as file:
    input = file.read()

pattern = r'\bmul\(\d{1,3},\d{1,3}\)'
results = re.findall(pattern, input)

total_sum = 0
for result in results:
    number_pattern = r'\d{1,3}'
    numbers = re.findall(number_pattern, result)
    int_numbers = list(map(int, numbers))

    multiplied_value = int_numbers[0] * int_numbers[1]
    total_sum += multiplied_value

print(total_sum)

# Part 2 
enabled_pattern = r'(mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\))'

enabled_sum = 0
enabled = True

for match in re.finditer(enabled_pattern, input):
    current = match.group(0)
    
    if current == 'do()':
        enabled = True
    elif current == 'don\'t()':
        enabled = False
    elif current.startswith('mul') and enabled:
        numbers = re.findall(r'\d+', current)
        multiplied_value = int(numbers[0]) * int(numbers[1])
        enabled_sum += multiplied_value

print(enabled_sum)