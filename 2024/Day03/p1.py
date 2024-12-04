from utils import load_input, time_solution, InputType
import re

def solve(input_data: str) -> str:
    return sum(map(lambda op : int(op[0]) * int(op[1]), re.findall(r'mul\((\d+),(\d+)\)', input_data)))

if __name__ == "__main__":
    input_data = load_input(3, InputType.MAIN)
    result = time_solution(solve, input_data)
    print(f"Result: {result}")