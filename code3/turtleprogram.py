import turtle


wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Hello, Tess!")    # Set the window title to "Hello, Tess!"    
tess = turtle.Turtle()
tess.color("hotpink")          # Tell tess to change her color
tess.pensize(3)             # Tell tess to set her pen width        
tess.forward(150)
tess.left(90)
tess.forward(75)
tess.left(90)
tess.forward(150)
tess.left(90)
tess.forward(75)
alex = turtle.Turtle()
alex.color("blue")
alex.pensize(5)
alex.forward(50)
alex.left(120)
alex.forward(50)
alex.left(120)
alex.forward(50)
wn.mainloop()