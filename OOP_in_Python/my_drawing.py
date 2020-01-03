from shapes import Triangle, Rectangle, Oval, Paper

rect1 = Rectangle()
rect1.set_width(200)
rect1.set_height(100)
rect1.set_color("blue")
rect1.draw()


rect2 = Rectangle()
rect2.set_width(50)
rect2.set_height(150)
rect2.set_color("yellow")
rect2.set_x(100)
rect2.set_y (100)
rect2.draw()

ov1 = Oval()
ov1.randomize()
ov1.draw()

Paper.display()