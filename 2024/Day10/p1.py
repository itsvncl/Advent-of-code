from utils import load_input, time_solution, InputType

DIRECTIONS = {
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
}

def trail_walk(grid, i, j, level, reached: set) -> int:
    try: #I still hate this, but it still performs better
        if(i < 0 or j < 0): return 0
        height = grid[i][j]
    except:
        return 0

    if height != level: return 0
    if level == 9 and (i,j) not in reached:
        reached.add((i,j))
        return 1 if height == level else 0
    
    level += 1
    return sum([trail_walk(grid, i+d[0], j+d[1], level, reached) for d in DIRECTIONS])


def solve(input_data: str) -> str:
    grid = list(map(lambda list: [int(digit) for digit in list], input_data.splitlines()))

    trails = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                reached_set = set()
                trails += trail_walk(grid, i, j, 0, reached_set)

    return trails
             
if __name__ == "__main__":
    input_data = load_input(10, InputType.MAIN)
    result = time_solution(solve, input_data)
    print(f"Result: {result}")