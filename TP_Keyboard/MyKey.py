from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Key:

    def __init__(self,keyboard,position,size,symbol):
        self.keyboard = keyboard
        self.position = position
        self.size = size
        self.symbol = symbol
        self.over = False

    def paint(self,painter):
        painter.setPen(QPen(Qt.black,1,Qt.SolidLine))
        if self.over:
            painter.setBrush(QBrush(QColor(200,200,200)))
        else:
            painter.setBrush(QBrush(QColor(220,220,220)))

        painter.drawRoundedRect(self.position,5,5)
        painter.drawText(self.position,Qt.AlignCenter,self.symbol)

    def isOver(self,cursorPos):
        self.over = self.position.contains(cursorPos)