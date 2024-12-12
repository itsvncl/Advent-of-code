from utils import load_input, time_solution, InputType
from functools import cache

#Not my idea either. I just wanted to have some fun with this new cache annotation I learned about, very useful!

@cache
def blink(stone, blinks_left) -> int:
    if blinks_left == 0:
        return 1
    elif stone == 0:
        return blink(1, blinks_left - 1)
    elif len( stone_str:= str(stone)) % 2 == 0:
        half_point = len(stone_str) // 2
        return blink(int(stone_str[:half_point]), blinks_left - 1) + blink(int(stone_str[half_point:]), blinks_left - 1)
    else:
        return blink(stone * 2024, blinks_left - 1)

def solve(input_data: str) -> str:
    stones = list(map(int, input_data.split()))
    
    return sum([blink(stone, 75) for stone in stones])
             
if __name__ == "__main__":
    input_data = load_input(11, InputType.MAIN)
    result = time_solution(solve, input_data)
    print(f"Result: {result}")