import re


def calculate_multiplications(data):
    total_sum = 0
    multiplication_pattern = re.compile(r'mul\(\d{1,3},\d{1,3}\)')
    matches = multiplication_pattern.finditer(data)

    for match in matches:
        num1, num2 = map(int, re.findall(r'\d+', match.group()))
        total_sum += num1 * num2

    return total_sum


def conditional_multiplications(data):
    total_sum = 0
    pattern = re.compile(r'mul\(\d{1,3},\d{1,3}\)|don\'t\(\)|do\(\)')
    matches = pattern.finditer(data)
    is_enabled = True

    for match in matches:
        match_str = match.group()
        if match_str == "do()":
            is_enabled = True
        elif match_str == "don't()":
            is_enabled = False
        elif is_enabled:
            num1, num2 = map(int, re.findall(r'\d+', match_str))
            total_sum += num1 * num2

    return total_sum


with open('input.input', 'r') as file:
    input_data = file.read()

print(calculate_multiplications(input_data))
print(conditional_multiplications(input_data))
