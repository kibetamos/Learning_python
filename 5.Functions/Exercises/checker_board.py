import turtle

def draw_square(x, y, size, color):
    turtle.penup()
    turtle.goto(x - size / 2, y - size / 2)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)
    
    turtle.end_fill()

def draw_checkerboard(rows, cols, square_size):
    colors = ['black', 'white']
    
    # Draw outer border
    draw_square(0, 0, cols * square_size, 'black')
    
    for row in range(rows):
        for col in range(cols):
            color_index = (row + col) % 2
            color = colors[color_index]
            draw_square(col * square_size, row * square_size, square_size, color)

def main():
    turtle.hideturtle()
    turtle.speed(0)  # 0 is the fastest speed
    
    rows = 8
    cols = 8
    square_size = 30
    
    draw_checkerboard(rows, cols, square_size)

    turtle.done()

if __name__ == "__main__":
    main()
