from typing import List

#I miss interpreted the task from the beggining and made the data strucutre way more sophisticated than i should have.
#Well, a bit of OOP practice never hurts, am I right? :')

RED_LIMIT = 12
GREEN_LIMIT = 13
BLUE_LIMIT = 14

class Round:
    def __init__(self, red: int = 0, green: int = 0, blue: int = 0):
        self.red = red
        self.green = green
        self.blue = blue

class Game:
    def __init__(self, id: int, rounds: List[Round]):
        self.id = id
        self.rounds = rounds

input_string = open('input.txt', 'r').read()

def parse_round(round_str: str) -> Round:
    details = round_str.split(",")
    round = Round()

    for detail in details:
        [count, color] = detail.strip().split(" ")
        if color == "red":
            round.red = int(count)
        elif color == "green":
            round.green = int(count)
        elif color == "blue":
            round.blue = int(count)
    
    return round

def parse_game(details: str) -> Game:
    [game_id, rounds] = details.split(":")
    
    game_id = game_id.split(" ")[1]
    rounds = list(map(parse_round, rounds.split(";")))

    return Game(game_id, rounds)

games = list(map(parse_game, input_string.splitlines()))

#Part 1
in_limit_ids = []
for game in games:
    possible = True
    for round in game.rounds:
        if(round.red > RED_LIMIT or round.green > GREEN_LIMIT or round.blue > BLUE_LIMIT):
            possible = False
            break
    
    if possible:
        in_limit_ids.append(int(game.id))

print("Part 1: " + str(sum(in_limit_ids)))

#Part 2
powers_of_set_of_cubes = []
for game in games:
    max_red = 0
    max_green = 0
    max_blue = 0

    for round in game.rounds:
        if(round.red > max_red):
            max_red = round.red
        if(round.green > max_green):
            max_green = round.green
        if(round.blue > max_blue):
            max_blue = round.blue
    
    powers_of_set_of_cubes.append(max_red * max_green * max_blue)

print("Part 2: " + str(sum(powers_of_set_of_cubes)))