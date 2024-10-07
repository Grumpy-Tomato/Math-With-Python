from turtle import *
import time

shape('turtle')

def square(size=100):
    for i in range(4):
        forward(size)
        right(90)

def circleOfSquares():
    speed(0)
    for i in range(72):
        square()
        right(5)

circleOfSquares()
time.sleep(5)