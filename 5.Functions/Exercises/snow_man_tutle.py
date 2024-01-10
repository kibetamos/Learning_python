import turtle

def draw_circle(x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_snowman():
    # Draw snowman body
    draw_circle(0, -150, 40, 'white')
    draw_circle(0, -80, 30, 'white')
    draw_circle(0, -10, 20, 'white')

    # Draw snowman eyes
    draw_circle(-10, 10, 2, 'black')
    draw_circle(10, 10, 2, 'black')

    # Draw snowman nose
    turtle.penup()
    turtle.goto(0, 5)
    turtle.pendown()
    turtle.color('orange')
    turtle.begin_fill()
    turtle.left(60)
    turtle.forward(15)
    turtle.right(120)
    turtle.forward(15)
    turtle.end_fill()

def main():
    turtle.hideturtle()
    turtle.speed(2)
    
    draw_snowman()

    turtle.done()

if __name__ == "__main__":
    main()
