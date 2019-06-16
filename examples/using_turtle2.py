from guizero import App, Box, Text, Turtle, Slider, PushButton

a = App()

def draw():
    turtle.clear()
    for i in range(sides.value):
        turtle.forward(length.value)
        turtle.right(int(360 / sides.value))

Text(a, text="this is a guizero turtle")

buttons_box = Box(a)

Text(buttons_box, text="no. of sides: ", align="left")
sides = Slider(buttons_box, start=3, end=10, align="left")

Text(buttons_box, text="length: ", align="left")
length = Slider(buttons_box, start=10, end=100, align="left")
length.value = 100

draw_button = PushButton(buttons_box, text="Draw", align="left", command=draw)

turtle = Turtle(a, width="fill", height="fill")

a.display()