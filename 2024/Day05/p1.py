from utils import load_input, time_solution, InputType

def solve(input_data: str) -> str:
    rules, update_strs = input_data.split('\n\n')

    rule_table = {}
    for rule in rules.splitlines():
        before, after = rule.split('|')
        rule_table.setdefault(after, []).append(before)

    sum = 0
    for update_collection_string in update_strs.splitlines():
        update_collection = update_collection_string.split(',')

        invalid_updates = set()
        is_valid_update_collection = True
        for update in update_collection:
            if update in invalid_updates:
                is_valid_update_collection = False
                break
            invalid_updates.update(rule_table.get(update, []))
        
        if is_valid_update_collection:
            sum += int(update_collection[int((len(update_collection)-1)/2)])
    
    return sum
             
if __name__ == "__main__":
    input_data = load_input(5, InputType.MAIN)
    result = time_solution(solve, input_data)
    print(f"Result: {result}")