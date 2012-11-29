#Useful functions
def do_twice(f):
    f()
    f()
def do_four(f):
    do_twice(f)
    do_twice(f)

import turtle   
from turtle import *
from Tkinter import *
import math

def polygon(t, n, length):
    angle = 360.0 / n
    for i in range(n):
        turtle.forward(t)
        turtle.left(t)
        
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    for i in range(n):
        turtle.forward(step_length)
        turtle.left(step_angle)

# Menu Grid
def main_menu():
    def menu_1(s):
        print '|',
        print ' '*(14)+s+14*' ',
        print '|'
    def sid(s):
        print '|',
        print ' '*(12)+s+12*' ',
        print '|'
    def m(s):    
        print '|',
        print ' '*(14)+s+14*' ',
        print '|'
    def line_1():
        print '+ - - - -',
    def line_2():
        print '        ',
    def full_line_1():
        do_four(line_1)
        print '+'
    def full_line_2():
        print '| ',
        do_four(line_2)
        print ' |'
    def grid():
        full_line_1()
        do_twice(full_line_2)
        menu_1('Main Menu')
        full_line_2()
        sid('Gustavo Costa')
        m('M00272117')
        full_line_2()
        full_line_1()  
    grid()

    
    
# Menu
def menu():
    print ' '
    print ' '
    print 'Shapes and Forms'
    print ' '
    print '1) Triangle'
    print '2) Square'
    print '3) Rectangle'
    print '4) Circle'
    print '5) Pentagon'
    print '6) Hexagon'
    print '7) Spiral'
    print '8) Squared Spiral'
    print '9) Triangular Spiral'
    print '10) Smiley Face'
    print '11) Flowers'
    print '12) Quit program'


def program():
    menu();
    print ' '
    user = input('Type here a number from 1 to 12: ')
    
# Commands
    if (user == 1):
        triangle();
    elif (user == 2):
        square();
    elif (user == 3):
        rectangle();
    elif (user == 4):
        circle();
    elif (user == 5):
        pentagon();
    elif (user == 6):
        hexagon();
    elif (user == 7):
        spiral();
    elif (user == 8):
        squaredspiral();
    elif (user == 9):
        trianglespiral();
    elif (user == 10):
        face();
    elif (user == 11):
        flowers_3();
    elif (user == 12):    
        exit();
        
    else:
        print 'Sorry, try again!';
    print ' '    
    print '**********************************************************'    
    print '          Try another number or type 12 to exit.          '
    print '**********************************************************'
    print ' '
    program()

    
    
                        


# Shapes

# Triangle 1
def triangle():
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    raw_input('Press Enter')
    clear()
    turtle.reset()

# Square 2
def square():
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
    raw_input('Press Enter')    
    clear()
    turtle.reset()


# Rectangle 3
def rectangle():
    for i in range(2):
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)
    raw_input('Press Enter')    
    clear()
    turtle.reset()


# Circle 4
def circle():
    import math
    circunference = 2 * math.pi * 10
    n = int(circunference / 3) + 1
    length = circunference / n
    polygon(18, n, length)
    raw_input('Press Enter')
    clear()
    turtle.reset()

# Pentagon 5
def pentagon():
    turtle.forward(50)
    turtle.left(72)
    turtle.forward(50)
    turtle.left(72)
    turtle.forward(50)
    turtle.left(72)
    turtle.forward(50)
    turtle.left(72)
    turtle.forward(50)
    raw_input('Press Enter')
    clear()
    turtle.reset()

# Hexagon 6
def hexagon():
    turtle.forward(50)
    turtle.left(60)
    turtle.forward(50)
    turtle.left(60)
    turtle.forward(50)
    turtle.left(60)
    turtle.forward(50)
    turtle.left(60)
    turtle.forward(50)
    turtle.left(60)
    turtle.forward(50)
    raw_input('Press Enter')
    clear()
    turtle.reset()
    

# Spiral 7

def spiral():
    n=5
    while n<100:
        turtle.circle(n, 180)
        n +=5
    raw_input('Press Enter')    
    clear()
    turtle.reset()
 
# SquaredSpiral 8
def squaredspiral():
    n=10
    while n<100:
        turtle.forward(n)
        turtle.left(90)
        turtle.forward(n)
        turtle.left(90)
        n +=10
    raw_input('Press Enter')    
    clear()    
    turtle.reset()
    

# TriangledSpiral 9
def trianglespiral():
    n=10
    while n<100:
        turtle.forward(n)
        turtle.left(120)
        n +=10
    raw_input('Press Enter')    
    clear()
    turtle.reset()

# Smily Face 10
def face():
    turtle.color('blue')
    turtle.circle(50)
    turtle.up()
    turtle.goto(-20, 60)
    turtle.down()
    turtle.color('green')
    turtle.circle(8)
    turtle.up()
    turtle.goto(20, 60)
    turtle.down()
    turtle.color('green')
    turtle.circle(8)
    turtle.up()
    turtle.goto(0, 10)
    turtle.circle(40, 270)
    turtle.down()
    turtle.color('red')
    turtle.circle(40,180)
    turtle.up()
    turtle.forward(1000)
    raw_input('Press Enter')
    clear()
    turtle.reset()
    
# Flower 11
def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        turtle.left(180-angle)

def flowers(t, n, r, angle):
    for i in range(n):
        petal(t, r, angle)
        turtle.left(360.0/n)

def move_turtle(t, length):
    turtle.up()
    turtle.forward(length)
    turtle.down()

def flowers_3():
    turtle.speed (150)
    # Flower 1
    move_turtle(turtle, -100)
    flowers(turtle, 7, 60.0, 60.0)
    # Flower 2
    move_turtle(turtle, 100)
    flowers(turtle, 10, 40.0, 80.0)
    # Flower 3
    move_turtle(turtle, 100)
    flowers(turtle, 20, 140.0, 20.0)
    raw_input('Press Enter')
    clear()
    turtle.reset()


# Exit 12
def bye():
    #B
    turtle.color('red')
    turtle.up()
    turtle.goto(-60, 0)
    turtle.down()
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(180)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(20)
    turtle.backward(20)
    #Y
    turtle.color('blue')
    turtle.up()
    turtle.backward(20)
    turtle.down()
    turtle.right(90)
    turtle.forward(30)
    turtle.left(45)
    turtle.forward(25)
    turtle.backward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.backward(25)
    turtle.right(135)
    turtle.forward(30)
    #E
    turtle.color('green')
    turtle.up()
    turtle.left(90)
    turtle.forward(30)
    turtle.down()
    turtle.forward(20)
    turtle.backward(20)
    turtle.left(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(15)
    turtle.backward(15)
    turtle.left(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(20)
    #!
    turtle.color('purple')
    turtle.up()
    turtle.forward(20)
    turtle.right(90)
    turtle.down()
    turtle.forward(30)
    turtle.up()
    turtle.forward(10)
    turtle.right(90)
    turtle.down()
    turtle.circle(5)
    #Move arrow away
    turtle.up()
    turtle.forward(1000)

    
def exit():
    bye()
    import sys
    sys.exit()
    exit = quit = quit()
    del quit





def tkinter():
    root=Tk()
    widget=Label(root,text='Welcome! Choose a number from 1 to 11 and see what happens or type 12 to exit.')
    widget.pack()
    main_menu()
    program()

tkinter()

    


    
    


    

