from utils import load_input, time_solution, InputType
from typing import List

WORD = "XMAS"

def is_word_in_direction(grid: List[str], grid_i: int, grid_j: int, incr_i: int, incr_j: int, word: str, letter_ind: int = 0) -> bool:    
    if(grid_i >= len(grid) or grid_i < 0 or grid_j >= len(grid[grid_i]) or grid_j < 0):
        return False
    
    if grid[grid_i][grid_j] == word[letter_ind]:
        return True if letter_ind + 1 >= len(word) else is_word_in_direction(grid, grid_i + incr_i, grid_j + incr_j, incr_i, incr_j, word, letter_ind + 1)

    return False
    
def find_words_in_grid(grid: List[str], word: str) -> int:
    word_count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == word[0]:
                word_count += is_word_in_direction(grid, i + 1, j, 1, 0, word, 1)
                word_count += is_word_in_direction(grid, i - 1, j, -1, 0, word, 1)
                word_count += is_word_in_direction(grid, i, j - 1, 0, -1, word, 1)
                word_count += is_word_in_direction(grid, i, j + 1, 0, 1, word, 1)
                word_count += is_word_in_direction(grid, i + 1, j + 1, 1, 1, word, 1)
                word_count += is_word_in_direction(grid, i - 1, j - 1, -1, -1, word, 1)
                word_count += is_word_in_direction(grid, i - 1, j + 1, -1, 1, word, 1)
                word_count += is_word_in_direction(grid, i + 1, j - 1, 1, -1, word, 1)
    return word_count

def solve(input_data: str) -> str:
    return find_words_in_grid(input_data.splitlines(), WORD)

if __name__ == "__main__":
    input_data = load_input(4, InputType.MAIN)
    result = time_solution(solve, input_data)
    print(f"Result: {result}")