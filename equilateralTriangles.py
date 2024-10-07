from turtle import *
import time

shape('turtle')

def triangle(sideLength=100):
    for i in range(3):
        right(120)
        forward(sideLength)
        right(120)


triangle(200)
time.sleep(3)