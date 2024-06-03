from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Editor import *
import sys

def main():
    app = QApplication([])
    window = QMainWindow()
    window.setFixedSize(550,200)
    window.setCentralWidget(EditorWidget())
    window.show()
    app.exec()

if __name__ == "__main__":
    main()