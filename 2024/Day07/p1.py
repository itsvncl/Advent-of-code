from utils import load_input, time_solution, InputType
from typing import List

ADD = '+'
MULTI = '*'

value_found = False

def parse_input(line: str) -> dict:
    sum, numbers = line.split(':')
    return (int(sum), [int(num) for num in numbers.strip().split(" ")])

def add_or_multiply(current_sum: int, operand: str, value_searched: int, number_array: List[int], level: int = 1):
    global value_found
    if current_sum == value_searched and level == len(number_array):
        value_found = True
        return
    
    if value_found or len(number_array) <= level: return
    
    new_level = level + 1
    current_number = number_array[level]
    if operand == ADD:
        new_sum = current_sum + current_number
        add_or_multiply(new_sum, ADD, value_searched, number_array, new_level)
        add_or_multiply(new_sum, MULTI, value_searched, number_array, new_level)
    elif operand == MULTI:
        new_sum = current_sum * current_number
        add_or_multiply(new_sum, ADD, value_searched, number_array, new_level)
        add_or_multiply(new_sum, MULTI, value_searched, number_array, new_level)

def solve(input_data: str) -> str:
    equation_list = list(map(parse_input, input_data.splitlines()))

    global value_found
    valid_sum = 0
    for sum, number_array in equation_list:
        add_or_multiply(number_array[0], ADD, sum, number_array)
        add_or_multiply(number_array[0], MULTI, sum, number_array)

        if value_found:
            valid_sum += sum
            value_found = False


    return valid_sum
             
if __name__ == "__main__":
    input_data = load_input(7, InputType.MAIN)
    result = time_solution(solve, input_data)
    print(f"Result: {result}")