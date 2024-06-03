from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from BubbleCursor import *
import math

class RopeCursor(BubbleCursor):

    def paint(self,painter):
        painter.setPen(QPen(Qt.black,3))
        if (self.closest != None):
            painter.drawLine(self.x,self.y,self.closest.x,self.closest.y)
            painter.setPen(QPen(1))
            self.closest.paint(painter)
