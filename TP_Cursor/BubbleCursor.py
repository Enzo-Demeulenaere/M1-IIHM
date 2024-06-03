from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import math

class BubbleCursor:
    defaultCol = Qt.green

    def __init__(self,targets):
        self.x = 0
        self.y = 0
        self.size = 100
        self.targets = targets
        self.closest = None

    def paint(self,painter):
        painter.setBrush(BubbleCursor.defaultCol)
        painter.drawEllipse(self.x-(self.size),self.y-(self.size),self.size*2,self.size*2)

    def move(self,x,y):
        self.x = x
        self.y = y
        if (self.closest != None):
            self.closest.highlighted=False 
        self.closest = self.findClosest()
        self.closest.highlighted=True


    def findClosest(self):
        closest = None
        closestRange = 1000
        cursorCenter = [self.x,self.y]
        for target in self.targets:
            targetCenter = [target.x,target.y]
            distance = math.dist(cursorCenter,targetCenter)
            distance = distance-target.size//2
            if (distance < closestRange):
                closestRange = distance
                closest = target
        self.size = int(closestRange)
        return closest
