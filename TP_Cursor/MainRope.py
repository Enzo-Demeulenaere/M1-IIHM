from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from RopeWidget import *
import sys

def main(app,args):
    window = QMainWindow()
    window.resize(1024,800)
    window.setCentralWidget(RopeWidget(app,args))
    window.show()

if __name__ == "__main__":
    main()
