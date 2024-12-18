from utils import load_input, time_solution, InputType

def solve(input_data: str) -> str:
    leftColList = []
    rightColList = []

    for line in input_data.splitlines():
        splittedLine = line.split("   ")
        leftColList.append(int(splittedLine[0]))
        rightColList.append(int(splittedLine[1]))
    
    leftColList.sort()
    rightColList.sort()

    diffSum = 0
    for i in range(len(leftColList)):
        diffSum = diffSum + abs(leftColList[i]- rightColList[i])
    
    return diffSum

if __name__ == "__main__":
    input_data = load_input(1, InputType.MAIN)
    result = time_solution(solve, input_data)
    print(f"Result: {result}")