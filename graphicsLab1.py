from graphics import *
from time import sleep
    
def main():
    
    Y_INCREMENT = 5
    X_INCREMENT = 5
    
    win = GraphWin("Draw Circles", 400, 400)
    win.setBackground('orange')
 
    circ1 = Circle(Point(50, 50), 40)
    circ1.setFill('yellow')
    #circ1.setOutline('black')
    circ1.draw(win)
 
    text = Text(Point(200, 300), "Click mouse on new location for circle")
    text.draw(win)
    
    for i in xrange(3):
        
        curr_x_increment = X_INCREMENT
        curr_y_increment = Y_INCREMENT
        moveTo = win.getMouse()
        current = circ1.getCenter()
        dx = moveTo.getX()
        dy = moveTo.getY()
        x = current.getX()
        y = current.getY()
    
        print "I am in the for loop"
        
        while circ1.getCenter().getX() < dx - X_INCREMENT or circ1.getCenter().getY() < dy - Y_INCREMENT:
            print " X_INCREMENT : " + str(X_INCREMENT) + " x : " + str(circ1.getCenter().getX()) + " dx : " + str(dx)
            print " Y_INCREMENT : " + str(Y_INCREMENT) + " y : " + str(circ1.getCenter().getY()) + " dy : " + str(dy)
            if circ1.getCenter().getX() >= dx - X_INCREMENT:
                curr_x_increment = 0
            if circ1.getCenter().getY() >= dy - Y_INCREMENT:
                curr_y_increment = 0
            circ1.move(curr_x_increment,curr_y_increment)
        
        print "I am doing the steps after the while loop"
        X_INCREMENT = (dx - circ1.getCenter().getX())
        Y_INCREMENT = (dy - circ1.getCenter().getY())
        circ1.move(X_INCREMENT,Y_INCREMENT)
        
        
 
    # circ2 = Circle(Point(200, 200), 50)
#     circ2.setFill('blue')
#     circ2.setOutline('red')
#     circ2.draw(win)
#
    # line1 = Line(Point(350, 50), Point(350, 350))
    # line1.setWidth(4)
    # line1.draw(win)
    #
    
    win.close()
    
main()