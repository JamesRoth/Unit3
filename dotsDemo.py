#James Roth
#3/1/18
#dotsDemo.py - how to use loops with graphics

from ggame import *

red=Color(0xff0000,1)

dot=CircleAsset(25, LineStyle(1, red), red)

Sprite(dot, (200,200))

App().run()
