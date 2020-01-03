from turtle import Turtle
from random import randint

laura = Turtle()
laura.color('red')
laura.shape('circle')
laura.penup()
laura.goto(-160, 100)
laura.pendown()
laura.circle(200)

brian = Turtle()
brian.color('blue')
brian.shape('turtle')
brian.penup()
brian.goto(-160,40)
brian.pendown()
brian.circle(200)

for movement in range(100):
    laura.forward(randint(1,5))
    brian.forward(randint(1,5))

# way to stop window closing on its own
input("Press Enter to close")
