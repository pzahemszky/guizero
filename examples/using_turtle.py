from guizero import App, Text, Turtle

a = App()
Text(a, text="this is a guizero app")

painter = Turtle(a, width="fill", height="fill")
painter2 = Turtle(painter, width="fill", height="fill")

painter.pencolor("blue")
painter2.pencolor("green")

painter2.setx(20)
painter2.sety(20)

for i in range(50):
    painter.forward(50)
    painter2.forward(50)
    painter.left(123)  
    painter2.left(123)
    
painter.pencolor("red")
painter2.pencolor("yellow")

for i in range(50):
    painter.forward(100)
    painter2.forward(100)
    painter.left(123)
    painter2.left(123)

a.display()