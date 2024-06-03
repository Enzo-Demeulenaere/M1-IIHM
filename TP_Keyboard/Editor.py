from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from KeyboardWidget import *
import random
import time

class EditorWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initLayout()

    def initLayout(self):

        layout = QVBoxLayout(self)
        self.setLayout(layout)

        self.text = QLineEdit(self)
        keyboard = KeyboardWidget()
        keyboard.newletter.connect(self.addLetterToText)
        keyboard.newWord.connect(self.addWord)
        layout.addWidget(self.text)
        layout.addWidget(keyboard)

    def addLetterToText(self,key):
        self.text.setText(self.text.text() + key.symbol)

        
    def addWord(self,word):

        self.text.setText(self.text.text() + word + ' ')