import turtle


def main():
    window = turtle.Screen()
    dave = turtle.Turtle()
    make_square(dave)
    window.mainloop()


def make_square(dave):
    length = int(input('size of the flower : '))

    for i in range(12):
        make_line_and_turn(dave, length)


def make_line_and_turn(dave, length):
    dave.forward(length)
    dave.left(30)
    dave.forward(length)
    dave.left(120)
    dave.forward(length)
    dave.left(30)
    dave.forward(length)
    dave.left(30)
    dave.forward(length)
    dave.left(120)
    dave.forward(length)
    dave.left(180)
    dave.forward(length)
    dave.left(30)
    dave.forward(length)
    dave.left(30)
    dave.forward(length)
    dave.left(120)
    dave.forward(length)
    dave.left(180)




if __name__ == '__main__':
    main()
