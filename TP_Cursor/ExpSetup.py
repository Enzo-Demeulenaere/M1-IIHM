from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from XPManager import *

class ExpSetup(QDialog):
    densities = [30,90]
    targetSizes = [9,18]

    def __init__(self,app):
        super().__init__()
        self.app = app
        self.initLayout()
        

    def initLayout(self):


  
        validateButton = QPushButton("Validate",self)
        validateButton.clicked.connect(self.validate)
        self.textInput = QLineEdit(self)

        layout = QVBoxLayout(self)
        self.setLayout(layout)

        userLayout = QHBoxLayout()
        userLayout.addWidget(QLabel("User ID:"))
        userLayout.addWidget(self.textInput)
        layout.addLayout(userLayout)

        layout.addWidget(validateButton)

    def validate(self):
        self.userID = self.textInput.text()
        manager = XPManager(self.userID,self.window())
        manager.initCombinations()