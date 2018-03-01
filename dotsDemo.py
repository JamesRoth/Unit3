#James Roth
#3/1/18
#dotsDemo.py - how to use loops with graphics

from ggame import *

red=Color(0xff0000,1)

dot=CircleAsset(25, LineStyle(1, red), red)

for i in range (15): #putting a row of dots
    for j in range (9):
        Sprite(dot, (10+i*60,10+60*j))

App().run()
