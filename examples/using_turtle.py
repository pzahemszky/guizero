from guizero import App, Text, Turtle

a = App()
Text(a, text="this is a guizero app")

painter = Turtle(a, width="fill", height="fill")

painter.pencolor("blue")

for i in range(50):
    painter.forward(50)
    painter.left(123)  
    
painter.pencolor("red")
for i in range(50):
    painter.forward(100)
    painter.left(123)

a.display()