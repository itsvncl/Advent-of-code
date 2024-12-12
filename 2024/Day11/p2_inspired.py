from utils import load_input, time_solution, InputType

#Sadly after thinking on this problem for about 24 hours straight, I couldn't come up 
#with a solution on my own. My best attempt vagy 64 iterations with an overengineerd bruteforce
#This solution is highly inspired by some reddit folks. Not my idea, but my implementation
#and a great opportunity to learn something new :)

cache = {}

def blink(stone, blinks_left) -> int:
    if blinks_left == 0:
        return 1
    elif (stone, blinks_left) in cache:
        return cache[(stone, blinks_left)]
    elif stone == 0:
        stone_count = blink(1, blinks_left - 1)
    elif len( stone_str:= str(stone)) % 2 == 0:
        half_point = len(stone_str) // 2
        stone_count = blink(int(stone_str[:half_point]), blinks_left - 1) + blink(int(stone_str[half_point:]), blinks_left - 1)
    else:
        stone_count = blink(stone * 2024, blinks_left - 1)
    
    cache[(stone, blinks_left)] = stone_count 
    return stone_count

def solve(input_data: str) -> str:
    stones = list(map(int, input_data.split()))
    
    return sum([blink(stone, 75) for stone in stones])
             
if __name__ == "__main__":
    input_data = load_input(11, InputType.MAIN)
    result = time_solution(solve, input_data)
    print(f"Result: {result}")