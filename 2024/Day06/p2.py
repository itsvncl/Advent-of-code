from utils import load_input, time_solution, InputType
from typing import List

def look_ahead(lab_map, pos): # I hate it, but it literally runs faster then regular bound checking
    try:
        if(pos[0] < 0 or pos[1] < 0): return None
        return lab_map[pos[0]][pos[1]]
    except:
        return None

def rotate_right(direction: List[int]):
    direction.reverse()
    direction[1] *= -1
    return direction

def is_loop(lab_map, loc_i, loc_j, bound_i, bound_j, direction, obstacle = '#'):
    loc_rotation_path = set()
    while 0 <= loc_i < bound_i and 0 <= loc_j < bound_j:        
        while look_ahead(lab_map, [loc_i + direction[0], loc_j + direction[1]]) == obstacle:
            loc_rotation_hash_key = f"{loc_i},{loc_j};{direction[0]},{direction[1]}"
            if loc_rotation_hash_key in loc_rotation_path: return True
            
            loc_rotation_path.add(loc_rotation_hash_key)
            rotate_right(direction)

        loc_i += direction[0]        
        loc_j += direction[1]

    return False

def loop_guard(lab_map, start_pos,  direction = [-1 , 0], obstacle = '#', free_space = '.') -> int:
    bound_i, bound_j = len(lab_map), len(lab_map[0]) 
    loc_i, loc_j = start_pos

    loop_count = 0
    while 0 <= loc_i < bound_i and 0 <= loc_j < bound_j:
        while look_ahead(lab_map, [loc_i + direction[0], loc_j + direction[1]]) == obstacle:
            rotate_right(direction)

        ahead_i, ahead_j = loc_i + direction[0], loc_j + direction[1]
        if look_ahead(lab_map, [ahead_i, ahead_j]) == None: break
        
        if lab_map[ahead_i][ahead_j] == free_space:
            lab_map[ahead_i][ahead_j] = obstacle
            loop_count += is_loop(lab_map, loc_i, loc_j, bound_i, bound_j, [*direction])
            lab_map[ahead_i][ahead_j] = ''

        loc_i += direction[0]        
        loc_j += direction[1]

    return loop_count        

def find_start(lab_map, guard_marker = '^'):
    for i in range(len(lab_map)):
        for j in range(len(lab_map[i])):
            if lab_map[i][j] == guard_marker:
                return [i, j]

def solve(input_data: str) -> str: 
    lab_map = [list(line) for line in input_data.splitlines()]
    start_pos = find_start(lab_map)
    return loop_guard(lab_map, start_pos)
             
if __name__ == "__main__":
    input_data = load_input(6, InputType.MAIN)
    result = time_solution(solve, input_data)
    print(f"Result: {result}")