from utils import load_input, time_solution, InputType
import re

def prod(list) -> int:
    return int(list[0]) * int(list[1])

def solve(input_data: str) -> str:
    valid_ops = re.findall(r'mul\(\d+,\d+\)', input_data)
    return sum(map(lambda op : prod(re.findall(r'\d+', op)), valid_ops))

if __name__ == "__main__":
    input_data = load_input(3, InputType.MAIN)
    result = time_solution(solve, input_data)
    print(f"Result: {result}")