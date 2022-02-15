#spirograph tool


import math as m 
import turtle 

def largest(num1, num2):
    if num1 >= num2:
        return num1
    elif num2 > num1:
        return num2
    
def gcf(num1, num2):
    gcf = 0
    
    for divisor in range(1, largest(num1, num2) + 1):
        if num1 % divisor == 0 and num2 % divisor == 0:
            gcf = divisor
            
    return gcf
            

def lcm(num1, num2):
    return (num1 * num2) // gcf(num1, num2)

def draw_hypotrochoid(r, R, d):
    # could have used a while loop
    # while theta < upperbound:
    # x, y = parametric eqns
    # t.goto(x, y)
    # theta += step value (smaller = smoother)
    
    t = turtle.Turtle()
    t.speed(10)
    t.color('red')
    
    upperbound = m.ceil((m.pi * 2 * (lcm(r, R) / R) * 50))
    t.penup()
    
    # u can change the 0.02 parameter the smaller the value the smoother the curve but it will takek longer to draw
    for theta in [x * 0.02 for x in range(upperbound + 1)]:
        x = (R - r) * m.cos(theta) + d * m.cos(((R - r) * theta) / r)
        y = (R - r) * m.sin(theta) - d * m.sin(((R - r) * theta) / r)
        t.goto(x, y)
        t.pendown()
    

def draw_epitrochoid(r, R, d):
    t = turtle.Turtle()
    t.speed(10)
    t.color('red')
    
    upperbound = m.ceil((m.pi * 2 * (lcm(r, R) / R) * 50))
    t.penup()
    for theta in [x * 0.02 for x in range(upperbound + 1)]:
        x = (R + r) * m.cos(theta) - d * m.cos(((R + r) * theta) / r)
        y = (R + r) * m.sin(theta) - d * m.sin(((R + r) * theta) / r)
        t.goto(x, y)
        t.pendown()
    


draw_epitrochoid(75, 250, 150)

turtle.mainloop()
