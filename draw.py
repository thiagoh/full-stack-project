import turtle

def drawSquare(t):

   for i in range(1, 5):
      t.forward(100)
      t.right(90)

def drawArt():

   window = turtle.Screen()
   window.bgcolor("red")

   t = turtle.Turtle()
   t.shape("turtle")
   t.color("yellow")
   t.speed(20)
   angle = 10

   for i in range(1, 360 / angle):
      drawSquare(t)
      t.right(angle)

   window.exitonclick()

drawArt()
