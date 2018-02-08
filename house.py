#Ryan Jones
#2/8/18

from ggame import *

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)
yellow = Color(0xFFFF00,1)


yellowRectangle = RectangleAsset(200,200,yellow)

Sprite(yellowRectangle)

App().run()