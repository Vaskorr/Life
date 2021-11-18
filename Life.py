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
# game process
def game():
    gfield[0][0].draw(win)
    msg = Text(Point(170, 10), '<- draw figure and click here to start')
    msg.draw(win)
    for i in range(1000):
        a = win.getMouse()
        x = int(a.x//10)
        y = int(a.y//10)
        if x == 0 and y == 0:
            break;
        if field[x][y] == 0:
            field[x][y] = 1
            gfield[int(a.x//10)][int(a.y//10)].draw(win)
        else:
            field[x][y] = 0
            gfield[int(a.x//10)][int(a.y//10)].undraw()
    # 1000-steps game
    for i in range(1000):
        drawField()
        a = step()
        if not(a):
            break;
    # the end
    m = Text(Point(170, 30), 'press any cell to restart')
    m.draw(win)
    win.getMouse()
    m.undraw()
    return 0
#restart and clear 
while(1):
    game()
    for i in range(100):
        for j in range(100):
            field[i][j] = 0
            gfield[i][j].undraw()
            

