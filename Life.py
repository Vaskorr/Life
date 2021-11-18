'''
Created by Vaskorr 18.11.2021

Some description to understand my code:

field - 2D list with cell's condition
gfield - 2D list with squares to easy one-command draw and erasing


#0 dead
#1 alive
#2 dead -> alive
#3 alive -> dead

e.g:

000
111
000

020
313
020

010
010
010

TODO: optimize code to run faster
      add buttons/some different input
      make field boundless (?)
'''

from graphics import*
from time import*

win = GraphWin("Game of Life", 1000, 1000)
field = []
gfield = []

# init graphics field
for i in range(100):
    gf = []
    for j in range(100):
        gf.append(Rectangle(Point(i*10+1, j*10+1), Point(i*10+10, j*10+10)))
    gfield.append(gf)
    
# init conditions field
for i in range(100):
    a = []
    for j in range(100):
        gfield[i][j].setFill('black')
        a.append(0)
    field.append(a)
    
# function for check cell's neighbors
def chkcell(x, y):
    k = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not(i == 0 and j == 0):
                if field[x+i][y+j] == 1 or field[x+i][y+j] == 3:
                    k += 1
    return k

# function for make one step
def step():
    f = 0
    for i in range(1,99):
        for j in range(1,99):
            k = chkcell(i, j)
            if field[i][j] == 0:
                if k == 3:
                    field[i][j] = 2
                    f += 1
            else:
                if k < 2 or k > 3:
                    field[i][j] = 3
                    f += 1
    return f
# print and refresh the field
def drawField():
    for i in range(100):
        for j in range(100):
            if field[i][j] == 2:
                field[i][j] = 1
                gfield[i][j].draw(win)
            elif field[i][j] == 3:
                field[i][j] = 0
                gfield[i][j].undraw()

# glider moving model
field[50][50] = 1
field[51][51] = 1
field[52][51] = 1
field[52][50] = 1
field[52][49] = 1

# 1000-steps game
for i in range(1000):
    drawField()
    a = step()
    if not(a):
        break;
# the end
win.getMouse() 
win.close()
