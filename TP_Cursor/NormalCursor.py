from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import math

class NormalCursor:
    defaultCol = Qt.green

    def __init__(self,targets):
        self.x = 0
        self.y = 0
        self.targets = targets
        self.targeted = None

    def paint(self,painter):
        return 

    def move(self,x,y):
        self.x = x
        self.y = y
        if (self.targeted != None):
            self.targeted.highlighted=False 
        self.targeted = self.findTarget()
        if (self.targeted != None):
            self.targeted.highlighted=True 

    def findTarget(self):
        targeted = None
        cursorCenter = [self.x,self.y]
        for target in self.targets:
            targetCenter = [target.x,target.y]
            distance = math.dist(cursorCenter,targetCenter)
            if (distance < target.size//2):
                targeted = target
        return targeted
