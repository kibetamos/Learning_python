import turtle

def main():
    turtle.hideturtle()
    circle(0, 0, 100, 'red')
    circle(−150, −75, 50, 'blue')
    circle(−200, 150, 75, 'green')




# The circle function draws a circle. The x and y parameters
# are the coordinates of the center point. The radius
# parameter is the circle's radius. The color parameter
# is the fill color, as a string.

def circle(x, y, radius, color):
    turtle.penup() # Raise the pen
    turtle.goto(x, y - radius) # Position the turtle
    turtle.fillcolor(color) # Set the fill color
    turtle.pendown() # Lower the pen
    turtle.begin_fill() # Start filling
    turtle.circle(radius) # Draw a circ


