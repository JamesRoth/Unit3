#James Roth
#3/1/18
#dotsDemo.py - how to use loops with graphics

from ggame import *

RADIUS = 25  #this is a constant - always capitalized at the top - so i dont have to go back and change all the 25s

red=Color(0xff0000,1)

dot=CircleAsset(RADIUS, LineStyle(1, red), red)

for i in range (15): #putting a row of dots
    for j in range (9):
        Sprite(dot, (10+i*(RADIUS*2+10),10+(RADIUS*2+10)*j))

App().run()
