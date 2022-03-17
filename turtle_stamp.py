import turtle
import random

def screenLeft(x,y):

    r = random.random()
    g = random.random()
    b = random.random()
    tsize = random.randrange(1, 10)
    turtle.shapesize(tsize)
    turtle.color(r, g, b)

    turtle.goto(x,y)#마우스 위치로 이동
    turtle.left(random.random() * 360)#거북이 각도 랜덤으로 찍기
    turtle.stamp()

turtle.title('거북이로 찍기')
turtle.shape('turtle')
turtle.up()#선을 그리지 않게 거들기 위로 올리기
turtle.speed(10)#속도 최대
turtle.onscreenclick(screenLeft,1)

turtle.done()#창 종료하지 않게