from utils import load_input, time_solution, InputType
from typing import Tuple

def read_disk(input_data:str) -> Tuple[list[list], list[dict], dict]:
    free_space_groups = list()
    file_groups = list()

    file_id = 0
    is_file = True
    for char in input_data:
        block_size = int(char)
        if is_file:
            file_groups.append(block_size * [str(file_id)])
            file_id += 1
        else:
            free_block = {
                "space": block_size * ['0'],
                "original_size": block_size,
                "size": block_size,
            }
            free_space_groups.append(free_block)

        is_file = not is_file    

    return (file_groups, free_space_groups)

def solve(input_data: str) -> str:
    file_groups, free_space_groups = read_disk(input_data)
    file_groups.reverse()
    
    space_size = len(free_space_groups)
    for i, file_group in enumerate(file_groups):
        group_size = len(file_group)
        file_id = file_group[0]
        for j, free_space_group in enumerate(free_space_groups):
            free_size = free_space_group["size"]
            if j + 1 > space_size - i: break
            if free_size < group_size: continue

            offset = free_space_group["original_size"] - free_size
            free_space = free_space_group["space"]
            for j in range(offset, offset + group_size):
                free_space[j] = file_id

            free_space_group["size"] = free_size - group_size
            file_groups[i] = group_size * ['0']
            break

    file_groups.reverse()
    disk = []
    for i in range(space_size):
        disk.extend(file_groups[i])
        disk.extend(free_space_groups[i]["space"])
    disk.extend(file_groups[-1])

    return sum(i * int(disk[i]) for i in range(len(disk)))
             
if __name__ == "__main__":
    input_data = load_input(9, InputType.MAIN)
    result = time_solution(solve, input_data)
    print(f"Result: {result}")