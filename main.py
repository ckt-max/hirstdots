from turtle import Turtle, Screen,colormode
from random import *
# import colorgram
#
# colors = colorgram.extract('hdmmdc-02_a19.jpg',30)
# rgb_colors = []
#
# for c in colors:
#     r = c.rgb.r
#     g = c.rgb.g
#     b = c.rgb.b
#
#     rgb_colors.append((r,g,b))
# print (rgb_colors)

color_list = [(7, 38, 55), (47, 101, 120), (16, 80, 100), (115, 171, 184), (185, 61, 33), (49, 16, 22), (40, 13, 10), (235, 141, 60), (233, 73, 40), (202, 228, 236), (81, 147, 161), (147, 27, 19), (249, 242, 210), (140, 25, 31), (14, 25, 23), (247, 216, 73), (223, 241, 239), (144, 55, 62), (156, 207, 214), (222, 140, 19), (82, 95, 92), (140, 174, 171), (45, 64, 85), (247, 242, 245), (227, 40, 45), (159, 210, 208), (243, 209, 4), (42, 75, 71), (169, 144, 149), (72, 68, 46)]
colormode(255)

point = Turtle()
point.speed(0)
#point.color((7, 38, 55))
row_len = 10
screen_w = 1980
screen_h = 1080
point.penup()
point.goto(point.position() - (50 * row_len/2, 50 * row_len/2))

for i in range(row_len):
    for j in range(row_len):
        point.dot(20, choice(color_list))
        point.forward(50)

    point.goto(point.position() - (50 * row_len, 0) + (0, 50))


screen = Screen()
screen.screensize(screen_w, screen_h)
screen.exitonclick()