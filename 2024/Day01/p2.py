from utils import load_input, time_solution, InputType

def solve(input_data: str) -> str:
    leftColList = []
    rightColList = []

    for line in input_data.splitlines():
        splittedLine = line.split("   ")
        leftColList.append(int(splittedLine[0]))
        rightColList.append(int(splittedLine[1]))
    
    cache = {}
    sum = 0

    for leftId in leftColList:
        if leftId in cache:
            sum = sum + cache[leftId]
        else:
            partialSum = 0
            for rightId in rightColList:
                if rightId == leftId:
                    partialSum = partialSum + leftId
            
            cache[leftId] = partialSum
            sum = sum + partialSum
    
    return sum 

if __name__ == "__main__":
    input_data = load_input(1, InputType.MAIN)
    result = time_solution(solve, input_data)

    print(f"Result: {result}")