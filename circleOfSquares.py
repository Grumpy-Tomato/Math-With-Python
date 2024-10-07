from turtle import *
import time

shape('turtle')

def square(sideLength=100):
    for i in range(4):
        forward(sideLength)
        right(90)

def circleOfSquares(squareSize=100):
    speed(0)
    for i in range(72):
        square(squareSize)
        right(5)

sideLengthSizes = [65, 100, 150, 225]
for i in sideLengthSizes:
    circleOfSquares(i)

time.sleep(5)