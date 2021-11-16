
from turtle import*
import turtle

def fleur():
    for i in range(300):
        circle(190-i,90)
        left(90)
        circle(190-i,90)
        left(18)
turtle.speed(100)
fleur()
mainloop()        
