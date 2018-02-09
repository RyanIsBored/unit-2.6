#Ryan Jones
#2/8/18

from ggame import *

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)
yellow = Color(0xFFFF00,1)

noOutline = LineStyle(0,black)


yellowRectangle = RectangleAsset(300,300,noOutline,yellow)
redTriangle = PolygonAsset([(200,100), (450,50), (600,100)],noOutline,red)

Sprite(yellowRectangle,(200,200))
Sprite(redTriangle,(200,100))
App().run()