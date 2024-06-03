from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Target import *
from BubbleWidget import *
from RopeCursor import *

class RopeWidget(BubbleWidget):
    def __init__(self,app,args):
        super().__init__(app,args)
        self.cursor = RopeCursor(self.targets)