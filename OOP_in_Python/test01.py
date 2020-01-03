import json
from turtle import Turtle

class Turtle_plus(Turtle):
    def __init__(self):
        super().__init__()
        self.name = None
        self.wins = 0

red = Turtle_plus()
red.name = "Red"
blue = Turtle_plus()
blue.name = "Blue"

racers = [red, blue]

# read json file, if exists
try:
    with open("test_data.json", "r") as f:
        gamedata = json.load(f)
except:
    f = open("test_data.json",'w')
    gamedata = {}
    for racer in racers:
        gamedata[racer.name] = racer.wins

print(red.wins, "mcvicar")

red.wins += 5
print(red.wins)
# gamedata = {}
for racer in racers:
    gamedata[racer.name] = racer.wins
with open("test_data.json", "w") as f:
    json.dump(gamedata, f)
    print("eddie")
