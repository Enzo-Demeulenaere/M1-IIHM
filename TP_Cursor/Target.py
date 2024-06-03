from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Target:
    defaultCol = Qt.blue
    highlightCol = Qt.green
    toSelectCol = Qt.red

    def __init__(self,x,y,size):
        self.x = x
        self.y = y
        self.size = size
        self.toSelect = False
        self.highlighted = False

    def paint(self,painter):
        if (self.highlighted):
            painter.setBrush(Target.highlightCol)
        elif (self.toSelect):
            painter.setBrush(Target.toSelectCol)
        else: 
            painter.setBrush(Target.defaultCol) 
        painter.drawEllipse(self.x-(self.size//2),self.y-(self.size//2),self.size,self.size)