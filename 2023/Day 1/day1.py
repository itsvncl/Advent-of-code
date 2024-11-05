import re

input_string = open('input.txt', 'r').read()

#Part 1
string_array = re.sub(r'[^\d\n]', '', input_string).splitlines()
number_array = [int(num[0] + num[len(num)-1]) for num in string_array]
print('Part 1: ' + str(sum(number_array)))

#Part 2
number_dictionary = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def get_first_number(line: str) -> str:
    loop_barrier = len(line)
    curr_ind = 0

    while curr_ind != loop_barrier:
        if(line[curr_ind].isnumeric()):
            return line[curr_ind]
        
        subword = line[0:curr_ind+1]
        for key in number_dictionary.keys():
            if key in subword:
                return number_dictionary[key]

        curr_ind += 1

    return ''

def get_last_number(line: str) -> str:
    last_ind = len(line)
    curr_ind = last_ind - 1

    while curr_ind != -1:
        if(line[curr_ind].isnumeric()):
            return line[curr_ind]
        
        subword = line[curr_ind:last_ind]
        for key in number_dictionary.keys():
            if key in subword:
                return number_dictionary[key]

        curr_ind -= 1

    return ''

def get_number(line: str) -> int:
    return int(get_first_number(line) + get_last_number(line))

number_array_2 = map(get_number, input_string.splitlines())
print('Part 2: ' + str(sum(number_array_2)))