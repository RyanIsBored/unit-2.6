#Ryan Jones
#2/7/18
#graphicsdemo.py - intro to ggame

from ggame import *

red = Color(0xFF0000,1) #this is the color red
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black)

redRectangle = RectangleAsset(200,100,blackOutline,red) #width, height, outline, fill)
blueCircle = CircleAsset(50,blackOutline,blue) #radius, outline, fill
greenEllipse = EllipseAsset(100,50,blackOutline,green) #width, height, outliine, fill
blackLine = LineAsset(50,160,blackOutline) #x_enpoint, y_enpoint, lineStyle
redTriangle = PolygonAsset([(0,0), (120,180), (60,300)],blackOutline,red) #enpoint, outline, fill
text = TextAsset('h',fill=blue, style='bold 40pt Times') #test, other options

Sprite(redRectangle)
Sprite(blueCircle,(50,50))
Sprite(greenEllipse,(200,200))
Sprite(blackLine)
Sprite(redTriangle)
Sprite(text,(300,200))

App().run()