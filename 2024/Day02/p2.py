from utils import load_input, time_solution, InputType

def has_problem_at_index(number_str_array) -> int:
    prev_num = int(number_str_array[0])
    is_descending = prev_num > int(number_str_array[1])
    
    ind = 0
    if is_descending:
        for number_str in number_str_array[1:]:
            curr_num = int(number_str)
            if not 0 < prev_num - curr_num <= 3:
                return ind
            prev_num = curr_num
            ind += 1
    else:
        for number_str in number_str_array[1:]:
            curr_num = int(number_str)
            if not -3 <= prev_num - curr_num < 0:
                return ind
            prev_num = curr_num
            ind += 1
        
    return -1

def get_sub_arrays_in_bounds(arr, ind, max_ind):
    return [
        arr[max(ind - 1, 0):ind+1] + arr[min(ind + 2, max_ind):],
        arr[max(ind - 2, 0):ind] + arr[min(ind + 1, max_ind):],
        arr[max(ind - 3, 0):ind-1] + arr[min(ind, max_ind):],
    ]


def solve(input_data: str) -> str:
    safe_count = 0
    for line in input_data.splitlines():
        number_str_array = line.split(" ")
        problem_index = has_problem_at_index(number_str_array)
        
        #If there is no problem, or the problem is at the very end. Since if the problem is at the very end, it's dampened by the problem dampener
        if problem_index == -1 or problem_index == len(number_str_array) - 2:
            safe_count += 1
        else:
            sub_arrays = get_sub_arrays_in_bounds(number_str_array, problem_index, len(number_str_array))
            for sub_array in sub_arrays:
                if has_problem_at_index(sub_array) == -1:
                    safe_count += 1
                    break

    return safe_count

if __name__ == "__main__":
    input_data = load_input(2, InputType.MAIN)
    result = time_solution(solve, input_data)

    print(f"Result: {result}")