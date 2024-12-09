from utils import load_input, time_solution, InputType
from typing import Tuple
from collections import deque

#This solution is highly unoptimised :(

def read_disk(input_data:str) -> Tuple[deque[str], deque[str], deque[int]]:
    free_space_groups = deque()
    file_blocks = deque()
    file_groups = deque()

    file_id = 0
    space_index = 0
    is_file = True
    for char in input_data:
        block_size = int(char)
        if is_file:
            file_block = block_size * [str(file_id)]
            file_blocks.extend(file_block)
            file_groups.append(file_block)
            file_id += 1
        else:
            free_space_groups.append(range(space_index, space_index + block_size))

        is_file = not is_file
        space_index += block_size
    
    return (file_blocks, file_groups, free_space_groups)

def solve(input_data: str) -> str:
    file_blocks, file_groups, free_space_groups = read_disk(input_data)
    allocated_space_size = len(file_blocks)
    disk = []

    is_file = True
    while len(disk) < allocated_space_size:
        if is_file:
            disk.extend(file_groups.popleft())
        else:
            for i in free_space_groups.popleft():
                disk.append(file_blocks.pop())
        
        is_file = not is_file
    
    disk = disk[:allocated_space_size]
    
    return sum(i * int(disk[i]) for i in range(allocated_space_size))
             
if __name__ == "__main__":
    input_data = load_input(9, InputType.MAIN)
    result = time_solution(solve, input_data)
    print(f"Result: {result}")