from utils import load_input, time_solution, InputType
import bisect
from collections import defaultdict

def is_loop(loc_pair, loc_set) -> bool:
    if loc_pair in loc_set: return True
    loc_set.add(loc_pair)

def move_up(loc_i, loc_j, loc_set):
    up_list = COLUMN_MAP[loc_j]
    bisect_ind = bisect.bisect_left(up_list, loc_i) - 1
    if bisect_ind < 0: return False
    loc_i = up_list[bisect_ind] + 1
    if is_loop((loc_i, loc_j, 'U'), loc_set): return True

    return move_right(loc_i, loc_j, loc_set)

def move_right(loc_i, loc_j, loc_set):
    right_list = ROW_MAP[loc_i]
    bisect_ind = bisect.bisect_left(right_list, loc_j)
    if bisect_ind == len(right_list): return False
    loc_j = right_list[bisect_ind] - 1
    if is_loop((loc_i, loc_j, 'R'), loc_set): return True

    return move_down(loc_i, loc_j, loc_set)

def move_down(loc_i, loc_j, loc_set):
    down_list = COLUMN_MAP[loc_j]
    bisect_ind = bisect.bisect_left(down_list, loc_i)
    if bisect_ind == len(down_list): return False
    loc_i = down_list[bisect_ind] - 1
    if is_loop((loc_i, loc_j, 'D'), loc_set): return True

    return move_left(loc_i, loc_j, loc_set)

def move_left(loc_i, loc_j, loc_set):
    right_list = ROW_MAP[loc_i]
    bisect_ind = bisect.bisect_left(right_list, loc_j) - 1
    if bisect_ind < 0: return False
    loc_j = right_list[bisect_ind] + 1
    if is_loop((loc_i, loc_j, 'L'), loc_set): return True

    return move_up(loc_i, loc_j, loc_set)

def find_loop(start_pos, start_dir):
    loc_i, loc_j = start_pos
    
    loc_set = set()
    while True:
        if start_dir == (-1, 0):
            return move_up(loc_i, loc_j, loc_set)
        elif start_dir == (0, 1):
            return move_right(loc_i, loc_j, loc_set)
        elif start_dir == (1, 0):
            return move_down(loc_i, loc_j, loc_set)
        elif start_dir == (0, -1):
            return move_left(loc_i, loc_j, loc_set)
        
def look_ahead(lab_map, pos): # I hate it, but it literally runs faster then regular bound checking
    try:
        if(pos[0] < 0 or pos[1] < 0): return None
        return lab_map[pos[0]][pos[1]]
    except:
        return None

def get_guard_path(lab_map, start_pos,  direction = (-1 , 0), obstacle = '#') -> dict:
    bound_i, bound_j = len(lab_map), len(lab_map[0]) 
    loc_i, loc_j = start_pos
    dir_i, dir_j = direction
    
    pos_set = {}
    last_turn = start_pos
    ind = 0
    while 0 <= loc_i < bound_i and 0 <= loc_j < bound_j:
        loc_tuple = (loc_i, loc_j)  
        if loc_tuple not in pos_set:
            pos_set[loc_tuple] = (loc_i, loc_j, last_turn, ind, (dir_i, dir_j))
            ind += 1

        while look_ahead(lab_map, [loc_i + dir_i, loc_j + dir_j]) == obstacle:
            dir_i, dir_j = dir_j, -dir_i
            last_turn = (loc_i, loc_j)

        loc_i += dir_i      
        loc_j += dir_j

    return pos_set  

def find_start_and_build_dicts(lab_map, guard_marker = '^'):
    for i in range(len(lab_map)):
        row_turns = []
        for j in range(len(lab_map[i])):
            field = lab_map[i][j]
            if field == '#':
                COLUMN_MAP.setdefault(j, []).append(i)
                row_turns.append(j)
            elif field == guard_marker:
                start = (i, j)
        
        row_turns.sort()
        ROW_MAP[i] = row_turns

    for key, values in COLUMN_MAP.items():
        COLUMN_MAP[key] = sorted(values)
    
    return start

def solve(input_data: str) -> str: 
    lab_map = list(map(list, input_data.splitlines()))
    start_pos = find_start_and_build_dicts(lab_map)
    guard_paths = get_guard_path(lab_map, start_pos)
    del guard_paths[start_pos]

    sorted_paths = sorted(guard_paths.values(), key=lambda x: x[3])
    loops = 0
    for path in sorted_paths:
        old_row_list = [*ROW_MAP[path[0]]]
        bisect.insort_left(ROW_MAP[path[0]], path[1])
        old_col_list = [*COLUMN_MAP[path[1]]]
        bisect.insort_left(COLUMN_MAP[path[1]], path[0])
        
        loops += find_loop(path[2], path[4])
        
        ROW_MAP[path[0]] = old_row_list
        COLUMN_MAP[path[1]] = old_col_list

    return (f'Part1: {len(sorted_paths) + 1}, Part2: {loops}')

ROW_MAP = defaultdict(list)
COLUMN_MAP = defaultdict(list)

if __name__ == "__main__":
    input_data = load_input(6, InputType.MAIN)
    result = time_solution(solve, input_data)
    print(f"Result: {result}")