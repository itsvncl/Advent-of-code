from utils import load_input, time_solution, InputType

def solve(input_data: str) -> str:
    return input_data

if __name__ == "__main__":
    input_data = load_input(1, InputType.MAIN)
    result = time_solution(solve, input_data)
    print(f"Result: {result}")