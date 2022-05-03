#spirograph tool

import math as m 
import turtle 

# may use euclidean algorithm which is more efficient log(n) rather than n
def gcd(num1, num2):
    gcd = 0

    for divisor in range(1, min(num1, num2) + 1):
        if num1 % divisor == 0 and num2 % divisor == 0:
            gcd = divisor
            
    return gcd

def lcm(num1, num2):
    return (num1 * num2) // gcd(num1, num2)


# order measures the smootheness of the generated curve (higher order = more smooth but takes longer to draw)
def draw_hypotrochoid(r, R, d, order = 50, color = 'red'):
    t = turtle.Turtle()
    t.speed(10)
    t.color(color)
    
    upperbound = m.ceil((m.pi * 2 * (lcm(r, R) / R) * order))
    t.penup()
    
    for theta in [x * (1/order) for x in range(upperbound + 1)]:
        x = (R - r) * m.cos(theta) + d * m.cos(((R - r) * theta) / r)
        y = (R - r) * m.sin(theta) - d * m.sin(((R - r) * theta) / r)
        t.goto(x, y)
        t.pendown()
    

def draw_epitrochoid(r, R, d, order = 50, color = 'red'):
    t = turtle.Turtle()
    t.speed(10)
    t.color(color)
    
    upperbound = m.ceil((m.pi * 2 * (lcm(r, R) / R) * order))
    t.penup()
    for theta in [x * (1/order) for x in range(upperbound + 1)]:
        x = (R + r) * m.cos(theta) - d * m.cos(((R + r) * theta) / r)
        y = (R + r) * m.sin(theta) - d * m.sin(((R + r) * theta) / r)
        t.goto(x, y)
        t.pendown()
    
# use the functions here above turtle.mainloop()
draw_epitrochoid(50, 150, 100)
draw_hypotrochoid(50, 150, 100)

turtle.mainloop()