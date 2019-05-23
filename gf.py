# import turtle
# import time
# Name=['H','Y','H']
# def draw_circle():
#     for i in range (200):
#         turtle.right(1)
#         turtle.forward(1)
# def draw_love():
#     turtle.color('red','pink')
#     turtle.pensize(2)
#     turtle.speed(1000)
#     turtle.goto(0,0)
#     turtle.begin_fill()
#     turtle.left(140)
#     turtle.forward(112)
#     draw_circle()
#     turtle.left(120)
#     draw_circle()
#     turtle.forward(112)
#     turtle.end_fill()
# def draw_name():
#     turtle.pensize(4)
#     turtle.up()
#     turtle.goto(-50,142.7)
#     if Name[0]=='L':
#         turtle.left(50)
#         turtle.down()
#         turtle.forward(60)
#         turtle.left(90)
#         turtle.forward(25)
#     turtle.up()
#     turtle.goto(37.5,142.7)
#     if Name[1]=='J':
#         turtle.down()
#         turtle.forward(25)
#         turtle.up()
#         turtle.goto(50,142.7)
#         turtle.right(90)
#         turtle.down()
#         turtle.forward(60)
#         for i in range (20):
#             turtle.right(7.8)
#             turtle.forward(0.3)
#         turtle.forward(8)
#         turtle.up()
#     turtle.goto(100,-10)
#     turtle.write("I Love you")
#
#
# draw_love()
# draw_name()


import turtle
import time

def liujia():
    for i in range (200):
        turtle.right(1)
        turtle.forward(1)
turtle.color('red','white')
turtle.pensize(2)
turtle.speed(10)
turtle.goto(0,0)

turtle.begin_fill()
turtle.left(140)
turtle.forward(112)
liujia()
turtle.left(120)
liujia()
turtle.forward(112)
turtle.end_fill()


turtle.pensize(2)
turtle.speed(1)
turtle.up()
turtle.goto(-65,137.7)
turtle.left(50)
turtle.down()
turtle.forward(60)
turtle.up()
turtle.goto(-65,107.7)
turtle.left(90)
turtle.down()
turtle.forward(30)
turtle.up()
turtle.goto(-35,137.7)
turtle.right(90)
turtle.down()
turtle.forward(60)

turtle.up()
turtle.goto(-18.3,137.7)
turtle.left(45)
turtle.down()
turtle.forward(30)
turtle.up()
turtle.goto(24.1,137.7)
turtle.down()
turtle.right(90)
turtle.forward(30)
turtle.left(45)
turtle.forward(40)

turtle.up()
turtle.goto(40,137.7)
turtle.down()
turtle.forward(60)
turtle.up()
turtle.goto(40,107.7)
turtle.left(90)
turtle.down()
turtle.forward(30)
turtle.up()
turtle.goto(70,137.7)
turtle.right(90)
turtle.down()
turtle.forward(60)

turtle.up()
turtle.goto(-24,35)
turtle.left(135)
turtle.forward(8)
turtle.write("I Love you")
turtle.mainloop()
