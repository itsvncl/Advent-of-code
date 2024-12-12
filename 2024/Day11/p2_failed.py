from utils import load_input, time_solution, InputType

#This is my failed attempt before looking at reddit. I got it working until 60 blinks (runs in 8 minutes),
# but over that it wont ever finish the calculation :(

stone_cache = {}

def get_path_to(stone: int) -> tuple[int, dict[int]]:
    stones = [stone]
    level_cache = {}
    for i in range(1,32):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
                continue
            stone_str = str(stone)
            
            if len(stone_str) % 2 == 0:
                half_point = len(stone_str) // 2
                new_stones.extend([int(stone_str[:half_point]), int(stone_str[half_point:])])
            else:
                new_stones.append(stone * 2024)
        level_cache[i] = ([*new_stones], len(new_stones))
        stones = [*new_stones]
    return (31, level_cache)

master = 0
def blink(stone: int, level: int, max_level: int):
    global master    
    if level >= max_level:
        master += 1
        return

    if stone in stone_cache:
        path_cache = stone_cache[stone][1]
        steps_remain = max_level-level
        step = min(steps_remain, path_cache[0])

        if step == steps_remain:
            master += path_cache[1][step][1]
            return

        next_level = level + step
        for cache in path_cache[1][step][0]:
            blink(cache, next_level, max_level)
        return

    next_level = level + 1
    if stone == 0:
        stone_cache[stone] = ([1], get_path_to(stone))
        blink(1, next_level, max_level)
        return
    if len(str(stone)) % 2 == 0:
        value_str = str(stone)
        half_point = len(value_str) // 2
        current_cache = [int(value_str[:half_point]), int(value_str[half_point:])]
        stone_cache[stone] = (current_cache, get_path_to(stone))
        for cache in current_cache:
            blink(cache, next_level, max_level)
    else:
        new_stone = stone * 2024
        stone_cache[stone] = ([new_stone], get_path_to(stone))
        blink(new_stone, next_level, max_level)


def solve(input_data: str) -> str:
    stones = list(map(int, input_data.split()))
    
    for stone in stones:
        blink(stone, 0, 62)

    return master
             
if __name__ == "__main__":
    input_data = load_input(11, InputType.MAIN)
    result = time_solution(solve, input_data)
    print(f"Result: {result}")