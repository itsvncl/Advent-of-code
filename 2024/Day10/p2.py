from utils import load_input, time_solution, InputType

DIRECTIONS = {
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
}

def trail_walk(grid, i, j, level, i_max, j_max) -> int:
    try: #I still hate this, but it still performs better
        if(i < 0 or j < 0): return 0
        height = grid[i][j]
    except:
        return 0

    if height != level: return 0
    if level == 9: return 1 if height == level else 0
    
    level += 1
    return sum([trail_walk(grid, i+d[0], j+d[1], level, i_max, j_max) for d in DIRECTIONS])


def solve(input_data: str) -> str:
    grid = list(map(lambda list: [int(digit) for digit in list], input_data.splitlines()))

    i_max = len(grid)
    j_max = len(grid[0])
    trails = 0
    for i in range(i_max):
        for j in range(j_max):
            if grid[i][j] == 0:
                trails += trail_walk(grid, i, j, 0, i_max, j_max)

    return trails
             
if __name__ == "__main__":
    input_data = load_input(10, InputType.MAIN)
    result = time_solution(solve, input_data)
    print(f"Result: {result}")