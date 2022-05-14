import turtle

window = turtle.Screen()
window.bgcolor("red")

brad = turtle.Turtle()
brad.shape("turtle") #2-step
brad.color("yellow") #2-step
brad.speed(2)        #2-step

brad.forward(100)
brad.right(90)
brad.forward(100)
brad.right(90)
brad.forward(100)
brad.right(90)
brad.forward(100)
brad.right(90)

angie = turtle.Turtle() #3-step
angie.shape("arrow") #3-step
angie.color("blue") #3-step
angie.circle(100) #3-step

window.exitonclick()