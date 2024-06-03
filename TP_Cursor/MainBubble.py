from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from BubbleWidget import *
import sys

def main(app,args):
    window = QMainWindow()
    window.resize(1024,800)
    window.setCentralWidget(BubbleWidget(app,args))
    window.show() 

if __name__ == "__main__":
    main()
