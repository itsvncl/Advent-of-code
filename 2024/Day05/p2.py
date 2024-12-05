from utils import load_input, time_solution, InputType
from typing import List
import math

def sorted_update_collection(update_collection: List[str], rule_table: dict) -> List[str]:
    invalid_count_by_rule = {key: 0 for key in update_collection}

    for update in update_collection:
        rule_set = rule_table.get(update, []) #This is required if the graph does not have a circle (like the example input...)
        for invalids in rule_set:
            if invalids in invalid_count_by_rule:
                invalid_count_by_rule[invalids] = invalid_count_by_rule[invalids] + 1

    return sorted(invalid_count_by_rule.items(), key = lambda item: int(item[1]), reverse=True)

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
        for update in update_collection:
            if update in invalid_updates:
                update_collection = sorted_update_collection(update_collection, rule_table) #This is now a tuple btw
                sum += int(update_collection[math.floor((len(update_collection)-1)/2)][0])
                break
            invalid_updates.update(rule_table.get(update, []))
    
    return sum
             
if __name__ == "__main__":
    input_data = load_input(5, InputType.MAIN)
    result = time_solution(solve, input_data)
    print(f"Result: {result}")