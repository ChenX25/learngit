#!/usr/bin/env python
#coding: utf-8

from turtle import *

def nose(x, y):
    penup()      # 提笔
    goto(x, y)   # 定位
    pendown()    # 下笔
    seth(-30)    # 定向
    begin_fill()
    a = 0.4
    for i in range(120):  # 每次左转3度，一周转120次
        if 0<=i<30 or 60<=i<90:
            a += 0.08     # 步长增大1/5
            lt(3)         # 左转
            fd(a)         # 前进
        else:
            a -= 0.08     # 步长减小1/5
            lt(3)
            fd(a)
    end_fill()

    penup()
    seth(90)
    fd(25)        # 向上前进25
    seth(0)
    fd(10)        # 向右前进10
    pendown()
    pencolor(255, 155, 192)
    seth(10)
    begin_fill()
    circle(5)     # 画左鼻孔
    color(160, 82, 45)
    end_fill()

    penup()
    seth(0)
    fd(20)        # 向右前进20
    pendown()
    pencolor(255, 155, 192)
    seth(10)
    begin_fill()
    circle(5)     # 画右鼻孔
    color(160, 82, 45)
    end_fill()

def head(x, y):
    color((255, 155, 192), "pink")
    penup()
    goto(x, y)
    seth(0)
    pendown()
    begin_fill()
    seth(180)           # 向左
    circle(300, -30)    # 顺时针画弧30度
    circle(100, -60)
    circle(80, -100)
    circle(150, -20)
    circle(60, -95)
    seth(161)
    circle(-300, 15)
    penup()
    goto(-100, 100)
    pendown()
    seth(-30)
    a = 0.4
    for i in range(60):
        if 0<=i<30 or 60<=i<90:
            a += 0.08
            lt(3)
            fd(a)
        else:
            a -= 0.08
            lt(3)
            fd(a)
    end_fill()

def ears(x, y):
    color((255, 155, 192), "pink")
    penup()
    goto(x, y)
    pendown()
    begin_fill()
    seth(100)
    circle(-50, 50)    # 逆时针画弧
    circle(-10, 120)
    circle(-50, 54)
    end_fill()

    penup()
    seth(90)
    fd(-12)
    seth(0)
    fd(30)             # 向下前进12，向右前进30
    pendown()
    begin_fill()
    seth(100)
    circle(-50, 50)
    circle(-10, 120)
    circle(-50, 56)
    end_fill()


def eyes(x, y):
    color((255, 155, 192),"white")
    penup()
    seth(90)
    fd(-20)
    seth(0)
    fd(-95)    # 下20，左95
    pendown()
    begin_fill()
    circle(15)   # 画左眼眶
    end_fill()

    color("black")
    penup()
    seth(90)
    fd(12)
    seth(0)
    fd(-3)       # 上12，左3
    pendown()
    begin_fill()
    circle(3)    # 画瞳孔
    end_fill()

    color((255, 155, 192), "white")
    penup()
    seth(90)
    fd(-25)
    seth(0)
    fd(40)        # 下25，右40
    pendown()
    begin_fill()
    circle(15)    # 画右眼眶
    end_fill()

    color("black")
    penup()
    seth(90)
    fd(12)
    seth(0)
    fd(-3)        # 上12，左3
    pendown()
    begin_fill()
    circle(3)     # 画瞳孔
    end_fill()

def cheek(x, y):
    color((255, 155, 192))
    penup()
    goto(x, y)
    pendown()
    seth(0)
    begin_fill()
    circle(30)     # 粉红脸颊
    end_fill()

def mouth(x, y):
    color(239, 69, 19)
    penup()
    goto(x, y)
    pendown()
    seth(-80)
    circle(30, 40)   # 逆时针画弧
    circle(40, 80)

def body(x, y):
    color("red", (255, 99, 71))
    penup()
    goto(x, y)
    pendown()
    begin_fill()
    seth(-130)
    circle(100, 10)
    circle(300, 30)
    seth(0)
    fd(230)    # 向右前进
    seth(90)
    circle(300, 30)
    circle(100, 3)
    color((255, 155, 192),(255, 100, 100))
    seth(-135)
    circle(-80, 63)
    circle(-150, 24)
    end_fill()

def hands(x, y):
    color((255, 155, 192))
    penup()
    goto(x, y)
    pendown()
    seth(-160)
    circle(300, 15)
    penup()
    seth(90)
    fd(15)
    seth(0)
    fd(0)      # 向上前进15
    pendown()
    seth(-10)
    circle(-20, 90)

    penup()
    seth(90)
    fd(30)
    seth(0)
    fd(237)    # 上30，右237
    pendown()
    seth(-20)
    circle(-300, 15)
    penup()
    seth(90)
    fd(20)
    pendown()
    seth(-170)
    circle(20, 90)

def foot(x, y):
    pensize(10)
    color((240, 128, 128))
    penup()
    goto(x, y)   # 定位左脚
    pendown()
    seth(-90)
    fd(40)      # 下40
    seth(-180)
    color("black")  # 画鞋
    pensize(15)
    fd(20)      # 左20

    pensize(10)
    color((240, 128, 128))
    penup()
    seth(90)
    fd(40)
    seth(0)
    fd(90)      # 上40，右90，定位右脚
    pendown()
    seth(-90)
    fd(40)      # 下40
    seth(-180)
    color("black")   # 画鞋
    pensize(15)
    fd(20)      # 左20

def tail(x, y):
    pensize(4)
    color((255, 155, 192))
    penup()
    goto(x, y)
    pendown()
    seth(0)
    circle(70, 20)
    circle(10, 330)
    circle(70, 30)

def setting():
    pensize(4)
    hideturtle()
    colormode(255)
    color((255, 155, 192), "pink")
    setup(840, 500)
    speed(10)

def main():
    setting()
    
    nose(-100, 100)
    head(-69, 167)
    ears(0, 160)
    eyes(0, 140)
    cheek(80, 10)
    mouth(-20, 30)
    
    body(-32, -8)
    hands(-56, -45)
    foot(2, -177)
    tail(148, -155)
    
    done()   


if __name__ == '__main__':
    main()
