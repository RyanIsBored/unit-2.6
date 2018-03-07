#Ryan Jones
#2/8/18

from ggame import *

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)
yellow = Color(0xFFFF00,1)

noOutline = LineStyle(0,black)


greenRectangle = RectangleAsset(300,300,noOutline,green)
redTriangle = PolygonAsset([(200,200), (350,100), (500,200)],noOutline,red)
blackRectangle = RectangleAsset(100,100,noOutline,black)
text = TextAsset('house',fill=blue, style='bold 40pt wingdings')
yellowCircle = CircleAsset(10,noOutline,yellow)


Sprite(greenRectangle,(200,200))
Sprite(redTriangle,(200,100))
Sprite(blackRectangle,(300,400))
Sprite(text,(250,300))
Sprite(yellowCircle,(305,440))
App().run()