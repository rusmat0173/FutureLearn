# from shapes import Triangle, Rectangle, Oval, Paper
from turtle import Turtle
from random import randint
import json

class Turtle_plus(Turtle):
    def __init__(self):
        super().__init__()
        self.name = None
        self.wins = 0

# create the race track
referee = Turtle()
ref= referee
ref.color('black')
ref.shape('turtle')
ref.penup()
ref.goto(-200,0)

for i in range(2):
    ref.circle(0)
ref.left(90)
ref.speed(5)
ref.pendown()
ref.forward(200)
ref.right(90)
ref.forward(400)
ref.right(90)
ref.forward(380)
ref.right(90)
ref.goto(-200,-180)
ref.right(90)
ref.goto(-200,0)
ref.penup()
ref.ht()

# create signage
ref.goto(0,210)
ref.write("Let's Race!", move = False, align = "center", font = ("Arial", 18, "normal"))

# create racing turtles
red = Turtle_plus()
red.name = ("Red")
red.penup()
red.goto(-220, 160)
red.color('red')
red.shape('turtle')
red.pencolor("red")

yellow = Turtle_plus()
yellow.name = ("Yellow")
yellow.penup()
yellow.goto(-220, 100)
yellow.color('yellow')
yellow.shape('turtle')
yellow.pencolor("yellow")

blue = Turtle_plus()
blue.name = ("Blue")
blue.penup()
blue.goto(-220, 40)
blue.color('blue')
blue.shape('turtle')
blue.pencolor("blue")

green = Turtle_plus()
green.name = ("Green")
green.penup()
green.goto(-220, -20)
green.color('green')
green.shape('turtle')
green.pencolor("green")

pink = Turtle_plus()
pink.name = ("Pink")
pink.penup()
pink.goto(-220, -80)
pink.color('pink')
pink.shape('turtle')
pink.pencolor("pink")

cyan = Turtle_plus()
cyan.name = ("Cyan")
cyan.penup()
cyan.goto(-220, -140)
cyan.color('cyan')
cyan.shape('turtle')
cyan.pencolor("cyan")
print(cyan.xcor())

# set up json file to score number of wins for each turtle
racers = [red, yellow, blue, green, pink, cyan]
try:
    with open("turtleracedata.json", "r") as f:
        gamedata = json.load(f)
except:
    f = open("turtleracedata.json",'w')



race_over = False
winner = None

# = = = = game here = = = =

# allow game to be played over and over
# play_again = True

# create race itself
while not race_over:
    for racer in racers:
        step = randint(0, 3)
        racer.forward(step)
        if racer.xcor() > 190:
            racer.wins += 1
            checker = Turtle()
            checker.penup()
            checker.goto(0,-210)
            checker.ht()
            checker.write("Winner is " + str(racer.color()[0]), move = True, align = "center", font = ("Arial", 12, "normal"))
            race_over = True


# way to stop window closing on its own
input("Press Enter to close")

# relaod json data file
with open("turtleracedata.json", "w") as f:
    json.dump(gamedata, f)



