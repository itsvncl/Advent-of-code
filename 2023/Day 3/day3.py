from typing import List

input_string = open('input.txt', 'r').read()
engine_matrix = [list(line) for line in input_string.splitlines()]
i_max = len(engine_matrix) - 1
j_max = len(engine_matrix[0]) - 1

#Part 1
def has_symbol(i: int, j: int) -> bool:
    return i >= 0 and j >= 0 and i <= i_max and j <= j_max and engine_matrix[i][j] != '.' and not engine_matrix[i][j].isdigit()

def is_part(i: int, j: int) -> bool:
    if has_symbol(i-1, j): return True
    if has_symbol(i+1, j): return True
    if has_symbol(i, j+1): return True
    if has_symbol(i, j-1): return True
    if has_symbol(i-1, j+1): return True
    if has_symbol(i-1, j-1): return True
    if has_symbol(i+1, j+1): return True
    if has_symbol(i+1, j-1): return True

    return False

is_part_number = False
number = ''
part_numbers = []
for i in range(i_max+1):
    for j in range(j_max+1):
        if not engine_matrix[i][j].isdigit():
            if is_part_number:
                part_numbers.append(int(number))
            is_part_number = False
            number = ''
            continue
        
        if not is_part_number:
            is_part_number = is_part(i, j)
        
        number += engine_matrix[i][j]

print("Part 1: " + str(sum(part_numbers)))

#Part 2
def is_number(i: int, j: int) -> bool:
    return i >= 0 and j >= 0 and i <= i_max and j <= j_max and engine_matrix[i][j].isdigit()

def reveal_number(i: int, j: int) -> int:
    number = engine_matrix[i][j]
    left_j = j
    right_j = j

    while left_j > 0:
        left_j -= 1
        char = engine_matrix[i][left_j]

        if char.isdigit():
            number = engine_matrix[i][left_j] + number
        else:
            break
    
    while right_j < j_max:
        right_j += 1
        char = engine_matrix[i][right_j]

        if char.isdigit():
            number = number + engine_matrix[i][right_j]
        else:
            break
    
    return int(number)

def get_parts_around(i: int, j: int) -> List[int]:
    part_positions = []
    if is_number(i, j+1): part_positions.append((i, j+1)) # To the right
    if is_number(i, j-1): part_positions.append((i, j-1)) # To the left

    if is_number(i-1, j): # Middle field on the top
        part_positions.append((i-1, j))
    else:
        if is_number(i-1, j+1): part_positions.append((i-1, j+1))
        if is_number(i-1, j-1): part_positions.append((i-1, j-1))
    
    if is_number(i+1, j): # Middle field on the bottom
        part_positions.append((i+1, j))
    else:
        if is_number(i+1, j+1): part_positions.append((i+1, j+1))
        if is_number(i+1, j-1): part_positions.append((i+1, j-1))
    
    part_numbers = []
    for (pp_i, pp_j) in part_positions:
        part_numbers.append(reveal_number(pp_i, pp_j))
    
    return part_numbers

gears = []
for i in range(i_max+1):
    for j in range(j_max+1):
        if engine_matrix[i][j] == "*":
            parts_around = get_parts_around(i, j)
            if len(parts_around) == 2:
                gears.append(parts_around[0] * parts_around[1])

print("Part 2: " + str(sum(gears)))