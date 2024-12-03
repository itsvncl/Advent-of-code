from utils import load_input, time_solution, InputType
import re

DO = "do()"
MUL_SIG = "m"

def prod(list) -> int:
    return int(list[0]) * int(list[1])

def solve(input_data: str) -> str:
    valid_ops = re.findall(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)', input_data)
    
    sum = 0
    execute_enabled = True
    for op in valid_ops:
        if op[0] == MUL_SIG and execute_enabled:
            sum += prod(re.findall(r'\d+', op))
            continue  
        execute_enabled = op == DO
    return sum

if __name__ == "__main__":
    input_data = load_input(3, InputType.MAIN)
    result = time_solution(solve, input_data)
    print(f"Result: {result}")