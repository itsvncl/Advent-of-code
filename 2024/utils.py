import time
import math
from enum import Enum
from pathlib import Path

class InputType(Enum):
    EXAMPLE = "example"
    MAIN = "main"

def load_input(day: int, input_type: InputType = InputType.MAIN) -> str:
    if(input_type == InputType.MAIN):
        input_file = Path(f"./Day{day:02}/input.txt")
    else:
        input_file = Path(f"./Day{day:02}/example.txt")

    if input_file.exists():
        with open(input_file, "r") as f:
            return f.read().strip()
    else:
        raise FileNotFoundError(f"Input file for day {day:02} not found!")

def time_solution(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()

    execution_time_sec = (end_time - start_time)
    execution_time_ms = execution_time_sec * 1_000
    execution_time_us = execution_time_sec * 1_000_000
    
    print(f"Execution time:")
    print(f"  - {execution_time_sec:.3f} sec")
    print(f"  - {execution_time_ms:.2f} ms")
    print(f"  - {math.ceil(execution_time_us)} µs")
    return result
