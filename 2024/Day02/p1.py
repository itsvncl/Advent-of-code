from utils import load_input, time_solution, InputType

def is_safe(number_str_array):
    prev_num = int(number_str_array[0])
    is_descending = prev_num > int(number_str_array[1])
        
    if is_descending:
        for number_str in number_str_array[1:]:
            curr_num = int(number_str)
            if not 0 < prev_num - curr_num <= 3:
                return False
            prev_num = curr_num
    else:
        for number_str in number_str_array[1:]:
            curr_num = int(number_str)
            if not -3 <= prev_num - curr_num < 0:
                return False
            prev_num = curr_num
        
    return True

def solve(input_data: str) -> str:
    safe_count = 0
    
    for line in input_data.splitlines():
        number_str_array = line.split(" ")
        if is_safe(number_str_array):
            safe_count += 1
        
    return safe_count

if __name__ == "__main__":
    input_data = load_input(2, InputType.MAIN)
    result = time_solution(solve, input_data)
    print(f"Result: {result}")