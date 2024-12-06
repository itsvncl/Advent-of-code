from utils import load_input, time_solution, InputType
from typing import List

def look_ahead(lab_map, pos): # I hate it, but it literally runs faster then regular bound checking
    try:
        return lab_map[pos[0]][pos[1]]
    except:
        return None

def rotate_right(direction: List[int]):
    direction.reverse()
    direction[1] *= -1

def simulate_guard(lab_map, start_pos,  direction = [-1 , 0], obstacle = '#', step_marker = 'X') -> int:
    bound_i, bound_j = len(lab_map), len(lab_map[0]) 
    loc_i, loc_j = start_pos
    unique_pos_count = 0

    while 0 <= loc_i < bound_i and 0 <= loc_j < bound_j:
        lab_field = lab_map[loc_i][loc_j]
        if lab_field != step_marker:
            unique_pos_count += 1
            lab_map[loc_i][loc_j] = step_marker

        if look_ahead(lab_map, [loc_i + direction[0], loc_j + direction[1]]) == obstacle:
            rotate_right(direction)

        loc_i += direction[0]        
        loc_j += direction[1]

    return unique_pos_count        

def find_start(lab_map, guard_marker = '^'):
    for i in range(len(lab_map)):
        for j in range(len(lab_map[i])):
            if lab_map[i][j] == guard_marker:
                return [i, j]

def solve(input_data: str) -> str: 
    lab_map = [list(line) for line in input_data.splitlines()]
    start_pos = find_start(lab_map)
    return simulate_guard(lab_map, start_pos)
             
if __name__ == "__main__":
    input_data = load_input(6, InputType.MAIN)
    result = time_solution(solve, input_data)
    print(f"Result: {result}")