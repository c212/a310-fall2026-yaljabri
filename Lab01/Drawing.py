from turtle import Turtle


def turtle_command(text):
    command_list = text.split(",")
    command = command_list[0].strip()

    if command == "goto":
        x = float(command_list[1])
        y = float(command_list[2])
        width = float(command_list[3])
        color = command_list[4].strip()
        pen.width(width)
        pen.pencolor(color)
        pen.goto(x, y)

    elif command == "circle":
        radius = float(command_list[1])
        width = float(command_list[2])
        color = command_list[3].strip()
        pen.width(width)
        pen.pencolor(color)
        pen.circle(radius)

    elif command == "beginfill":
        color = command_list[1].strip()
        pen.fillcolor(color)
        pen.begin_fill()

    elif command == "endfill":
        pen.end_fill()

    elif command == "penup":
        pen.penup()

    elif command == "pendown":
        pen.pendown()

    else:
        print("Unknown command:", command)


def main():
    filename = input("Enter the drawing filename (example: Flower.txt): ")

    global pen
    pen = Turtle()
    pen.speed(0)

    screen = pen.getscreen()
    screen.title("Lab 01 - Qatar Flag Drawing")

    with open(filename) as file:
        for line in file:
            text = line.strip()
            if text:
                turtle_command(text)

    pen.hideturtle()
    screen.exitonclick()


if __name__ == "__main__":
    main()
