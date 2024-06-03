from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from NormalWidget import *
import sys

def main(app,targetsFile,callback):
    window = QMainWindow()
    window.resize(1024,800)
    window.setCentralWidget(NormalWidget(targetsFile,callback))
    window.show()

if __name__ == "__main__":
    pass
