from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ExpSetup import *
import sys

def main():
    app = QApplication([])
    window = QMainWindow()
    window.resize(250,250)
    window.setCentralWidget(ExpSetup(app))
    window.show()
    app.exec()

if __name__ == "__main__":
    main()