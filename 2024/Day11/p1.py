from utils import load_input, time_solution, InputType

class MagicStone:
    value: int
    level: int
    left: 'MagicStone'
    right: 'MagicStone'

stone_cache = {}

def blink(stones: list[int]) -> list[int]:
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
            continue
        stone_str = str(stone)
        
        if len(stone_str) % 2 == 0:
            half = len(stone_str) // 2
            new_stones.extend([int(stone_str[:half]), int(stone_str[half:])])
        else:
            new_stones.append(stone * 2024)
    
    return new_stones

def solve(input_data: str) -> str:
    stones = list(map(int, input_data.split()))
    
    for i in range(25):
        stones = blink(stones)
    return len(stones)
             
if __name__ == "__main__":
    input_data = load_input(11, InputType.MAIN)
    result = time_solution(solve, input_data)
    print(f"Result: {result}")