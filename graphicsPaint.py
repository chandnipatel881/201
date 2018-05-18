from graphics import *
import math
import string
 
def calculateRadius(x1,x2,y1,y2):
    return math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))

def main():
    radius = 0
    win = GraphWin("Paint", 400, 400)
    win.setBackground('orange')
    
    inputBox = Entry(Point(150,10), 50)
    inputBox.draw(win)
    inputBox.setText("Enter the color for your circles :")
    
    
    firstClick = win.getMouse()
    secondClick = win.getMouse()
    
    while firstClick.getX() != secondClick.getX() and firstClick.getY() != secondClick.getY():
    
    
        print "First Click X : " + str(firstClick.getX())
        print "First Click Y : " + str(firstClick.getY())
        print "Second Click X : " + str(secondClick.getX())
        print "Second Click Y : " + str(secondClick.getY())
    
        radius = calculateRadius(firstClick.getX(),secondClick.getX(),firstClick.getY(),secondClick.getY())
    
        print "Radius : " + str(radius)
    
        circ1 = Circle(Point(firstClick.getX(), secondClick.getY()),radius)
        circ1.draw(win)
        circ1.setFill(string.strip(inputBox.getText()))
        
        firstClick = win.getMouse()
        secondClick = win.getMouse()
    

    
    win.close()
    
    
    
main()