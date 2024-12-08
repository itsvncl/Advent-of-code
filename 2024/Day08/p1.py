from utils import load_input, time_solution, InputType
from collections import defaultdict
from typing import Tuple, List

def get_antinode_pair(a1: Tuple[int], a2: Tuple[int]) -> List[Tuple[int]]:
    dist = (a1[0]-a2[0], a1[1]-a2[1])
    return [
        (a1[0] + dist[0], a1[1] + dist[1]),
        (a2[0] - dist[0], a2[1] - dist[1])
    ]

def solve(input_data: str) -> str:
    antenna_map = defaultdict(list)
    
    grid = input_data.splitlines()
    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            if char != '.':
                antenna_map[char].append((i,j))

    bound_i = len(grid)
    bound_j = len(grid[0])
    anti_node_set = set()
    for locations in antenna_map.values():
        for i in range(0, len(locations)-1):
            for j in range(i+1, len(locations)):
                anti_node_pair = get_antinode_pair(locations[i], locations[j])
                for node_i, node_j in anti_node_pair:
                    if 0 <= node_i < bound_i and 0 <= node_j < bound_j:
                        anti_node_set.add((node_i, node_j))
    
    return len(anti_node_set)
             
if __name__ == "__main__":
    input_data = load_input(8, InputType.MAIN)
    result = time_solution(solve, input_data)
    print(f"Result: {result}")