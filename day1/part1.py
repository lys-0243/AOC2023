import re

def read_file(file_path):
    with open(file_path, "r") as file:
        return file.readlines()

def extract_numbers(lines):
    return [re.sub(r'[^0-9]', '', line) for line in lines]

def get_first_and_last(numbers):
    return [num[0] + num[-1] for num in numbers if num]

def calculate_sum(numbers):
    return sum(int(num) for num in numbers)

def main():
    lines = read_file("../input.txt")
    only_numeric = extract_numbers(lines)
    first_and_last = get_first_and_last(only_numeric)
    total = calculate_sum(first_and_last)
    print(total)

main()



