from utils import load_input, time_solution, InputType
from typing import List

ADD = '+'
MULTI = '*'
CONCAT = '|'

P1_OPERANDS = [ADD, MULTI]
P2_OPERANDS = [CONCAT, MULTI, ADD]

value_found = False

def parse_input(line: str) -> dict:
    sum, numbers = line.split(':')
    return (int(sum), [int(num) for num in numbers.strip().split(" ")])

def recursive_operation(current_sum: int, operand: str, value_searched: int, number_array: List[int], operand_array: List[str], level: int = 1):
    global value_found
    if current_sum == value_searched and level == len(number_array):
        value_found = True
        return
    
    if value_found or len(number_array) <= level: return
    
    current_number = number_array[level]
    if operand == ADD:
        new_sum = current_sum + current_number
    elif operand == MULTI:
        new_sum = current_sum * current_number
    elif operand == CONCAT:
        new_sum = int(str(current_sum) + str(current_number))
    
    level += 1
    for op in operand_array:
        recursive_operation(new_sum, op, value_searched, number_array, operand_array, level)

def solve(input_data: str) -> str:
    equation_list = list(map(parse_input, input_data.splitlines()))

    global value_found
    p1_sum = 0
    p2_sum = 0
    for sum, number_array in equation_list:
        for op in P1_OPERANDS:
            recursive_operation(number_array[0], op, sum, number_array, P1_OPERANDS)
            if value_found:
                p1_sum += sum
                break

        if not value_found:
            for op in P2_OPERANDS:
                recursive_operation(number_array[0], op, sum, number_array, P2_OPERANDS)
                if value_found:
                    p2_sum += sum
                    break
        
        value_found = False

    return f'\nPart1: {p1_sum}\nPart2: {p1_sum + p2_sum}'

# Solves both part1 and part2 combined, because the performance is actually better this way (assuming every input is like this)     
if __name__ == "__main__":
    input_data = load_input(7, InputType.MAIN)
    result = time_solution(solve, input_data)
    print(f"Result: {result}")