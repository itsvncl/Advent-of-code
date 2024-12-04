from utils import load_input, time_solution, InputType

VALID_CHARS = "MS"

def is_valid_mas(letter1, letter2):
    return letter1 != letter2 and letter1 in VALID_CHARS and letter2 in VALID_CHARS

def solve(input_data: str) -> str:
    x_count = 0
    grid = input_data.splitlines()
    for i in range(1,len(grid)-1):
        for j in range(1,len(grid[i])-1):
            x_count += grid[i][j] == 'A' and is_valid_mas(grid[i-1][j-1], grid[i+1][j+1]) and is_valid_mas(grid[i+1][j-1], grid[i-1][j+1])
    return x_count

if __name__ == "__main__":
    input_data = load_input(4, InputType.MAIN)
    result = time_solution(solve, input_data)
    print(f"Result: {result}")