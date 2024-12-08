from utils import load_input, time_solution, InputType
from collections import defaultdict
from typing import Tuple, List

def get_antinodes_in_bound(a1: Tuple[int], a2: Tuple[int], bound_i: int, bound_j: int) -> List[Tuple[int]]:
    dist = (a1[0]-a2[0], a1[1]-a2[1])
    anti_nodes = [a1, a2]

    anit_node_i, anit_node_j = a1[0] + dist[0], a1[1] + dist[1]
    while 0 <= anit_node_i < bound_i and 0 <= anit_node_j < bound_j:
        anti_nodes.append((anit_node_i, anit_node_j))
        anit_node_i, anit_node_j = anit_node_i + dist[0], anit_node_j + dist[1]
    
    anit_node_i, anit_node_j = a1[0] - dist[0], a1[1] - dist[1]
    while 0 <= anit_node_i < bound_i and 0 <= anit_node_j < bound_j:
        anti_nodes.append((anit_node_i, anit_node_j))
        anit_node_i, anit_node_j = anit_node_i - dist[0], anit_node_j - dist[1]
    
    return anti_nodes

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
                anti_node_set.update(get_antinodes_in_bound(locations[i], locations[j], bound_i, bound_j))
    
    return len(anti_node_set)
             
if __name__ == "__main__":
    input_data = load_input(8, InputType.MAIN)
    result = time_solution(solve, input_data)
    print(f"Result: {result}")