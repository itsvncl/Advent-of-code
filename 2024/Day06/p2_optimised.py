from utils import load_input, time_solution, InputType
import bisect
ROW_MAP = {}
COLUMN_MAP = {}

def look_ahead(lab_map, pos): # I hate it, but it literally runs faster then regular bound checking
    try:
        if(pos[0] < 0 or pos[1] < 0): return None
        return lab_map[pos[0]][pos[1]]
    except:
        return None


def get_guard_path(lab_map, start_pos,  direction = (-1 , 0), obstacle = '#') -> set:
    bound_i, bound_j = len(lab_map), len(lab_map[0]) 
    loc_i, loc_j = start_pos
    dir_i, dir_j = direction
    
    pos_set = set()
    while 0 <= loc_i < bound_i and 0 <= loc_j < bound_j:
        pos_set.add((loc_i, loc_j))

        while look_ahead(lab_map, [loc_i + dir_i, loc_j + dir_j]) == obstacle:
            dir_i, dir_j = dir_j, -dir_i

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

def is_loop(loc_pair, loc_set) -> bool:
    if loc_pair in loc_set: return True
    loc_set.add(loc_pair)

def find_loop(start_pos):
    loc_i, loc_j = start_pos
    
    loc_set = set()
    while True:
        #UP
        up_list = COLUMN_MAP[loc_j]
        bisect_ind = bisect.bisect_left(up_list, loc_i) - 1
        if bisect_ind < 0: return False
        loc_i = up_list[bisect_ind] + 1
        if is_loop((loc_i, loc_j, 'U'), loc_set): return True

        #RIGHT
        right_list = ROW_MAP[loc_i]
        bisect_ind = bisect.bisect_left(right_list, loc_j)
        if bisect_ind == len(right_list): return False
        loc_j = right_list[bisect_ind] - 1
        if is_loop((loc_i, loc_j, 'R'), loc_set): return True

        #DOWN
        down_list = COLUMN_MAP[loc_j]
        bisect_ind = bisect.bisect_left(down_list, loc_i)
        if bisect_ind == len(down_list): return False
        loc_i = down_list[bisect_ind] - 1
        if is_loop((loc_i, loc_j, 'D'), loc_set): return True

        #LEFT
        right_list = ROW_MAP[loc_i]
        bisect_ind = bisect.bisect_left(right_list, loc_j) - 1
        if bisect_ind < 0: return False
        loc_j = right_list[bisect_ind] + 1
        if is_loop((loc_i, loc_j, 'L'), loc_set): return True


def solve(input_data: str) -> str: 
    lab_map = list(map(list, input_data.splitlines()))
    start_pos = find_start_and_build_dicts(lab_map)
    guard_paths = get_guard_path(lab_map, start_pos)
    guard_paths.remove(start_pos)
    
    loops = 0
    for path in guard_paths:
        old_row_list = [*ROW_MAP[path[0]]]
        bisect.insort_left(ROW_MAP[path[0]], path[1])
        old_col_list = [*COLUMN_MAP[path[1]]]
        bisect.insort_left(COLUMN_MAP[path[1]], path[0])
        
        loops += find_loop(start_pos)
        
        ROW_MAP[path[0]] = old_row_list
        COLUMN_MAP[path[1]] = old_col_list

    return loops
             
if __name__ == "__main__":
    input_data = load_input(6, InputType.MAIN)
    result = time_solution(solve, input_data)
    print(f"Result: {result}")