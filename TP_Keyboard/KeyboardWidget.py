from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from MyKey import *
import json
from Reconnaisseur import *
from Dictionnaire import *

class KeyboardWidget(QWidget):
    newletter = pyqtSignal(Key)
    newWord = pyqtSignal(str)


    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)
        self.importJSON()
        self.createKeys()
        self.createButtons()
        self.tuples = []
        self.keyPressed = None
        self.mousePos = None
        self.sampleDist = 40
        self.dico = Dictionnaire(self)
        self.resampledStroke = None

    def importJSON(self):
        with open("layout.json",'r') as file:
            data = json.load(file)
        self.keyWidth = data["keyWidth"]
        self.keyHeight = data["keyHeight"]
        self.keySpacing = data["keySpacing"]
        self.nbReco = data["nbReco"]
        self.keys = data["keys"]

    def createKeys(self):
        newKeys = {}
        for key in self.keys:
            position = QRect((self.keyWidth+self.keySpacing)*key['x'],(self.keyHeight+self.keySpacing)*key['y'],self.keyWidth*key['width']+(key['width']-1)*self.keySpacing,self.keyHeight)
            newKeys[key['symbol']]=(Key(self,position,key['width'],key['symbol']))
        self.max_x = max(self.keys, key=lambda x: x["x"])["x"]+1 #+1 because goes from 0 to 9 where y goes from 1 to 4
        self.max_y = max(self.keys, key=lambda y: y["y"])["y"]
        self.keys = newKeys

    def createButtons(self):
        self.buttons= []
        buttonWidth = int(self.sizeHint().width()/self.nbReco)
        for i in range(self.nbReco):
            button = QPushButton(self)
            button.setGeometry(i*buttonWidth,0,buttonWidth,self.keyHeight)
            button.clicked.connect(self.buttonClicked)
            button.setObjectName(str(i))
            self.buttons.append(button)

    def buttonClicked(self):
        button = self.sender()
        self.newWord.emit(button.text())

    def mouseMoveEvent(self, event):
        self.mousePos = event.pos()

        for key in self.keys.values():
            key.isOver(event.pos())
        self.update()
        if self.keyPressed != None:
            self.tuples.append(event.pos())
        elif self.tuples != []:
            self.tuples = []
            

    def mousePressEvent(self,event):
        clickPos = event.pos()
        self.keyPressed = None
        for key in self.keys.values():
            if key.position.contains(clickPos):
                self.keyPressed = key
        #print(self.keyPressed.symbol)    
        return
    
    def mouseReleaseEvent(self,event):
        clickPos = event.pos()
        self.keyReleased = None
        for key in self.keys.values():
            if key.position.contains(clickPos):
                self.keyReleased = key
        if (self.keyPressed == self.keyReleased):
            #print(self.keyReleased.symbol)
            self.newletter.emit(self.keyReleased)
        foundWords = self.dico.findWords(self.resampledStroke,self.keyPressed,self.nbReco)
        self.overrideButtons(foundWords)
        self.keyPressed =None # On se sert de keyPressed comme marqueur de début de tracé aussi
        return

    def overrideButtons(self,words):
        for button,word in zip(self.buttons,words):
            button.setText(word.word)

    def paintEvent(self,event):
        painter = QPainter(self)
        for key in self.keys.values():
            key.paint(painter)
        if self.keyPressed:
            pen = QPen(QColor(50,0,100,20))
            pen.setWidth(8)
            painter.setPen(pen)
            for i in range(len(self.tuples)-1):
                t = self.tuples[i]
                t1 = self.tuples[i+1]
                painter.drawLine(t,t1)
                stroke = Reconnaisseur.resample(self.tuples,self.sampleDist)
                self.resampledStroke = stroke
                for p in stroke:
                    painter.drawEllipse(p.x(),p.y(),3,3)
                # Not satisfied, opacity can be created

    def sizeHint(self):

        newWidth = (self.keyWidth + self.keySpacing)* self.max_x
        newHeight = (self.keyHeight + self.keySpacing)* self.max_y
        return QSize(newWidth,newHeight)
    
    def wordToStroke(self,word,d):
        stroke = []
        for i in range(len(word)-2):
            key = self.keys[word[i]]
            nextKey = self.keys[word[i+1]]
            letterPos = key.position.center()
            nextLetterPos = nextKey.position.center()
            interpolated = letterPos
            while interpolated != nextLetterPos:
                interpolated = Reconnaisseur.interpolate(interpolated,nextLetterPos,d)
                stroke.append(interpolated)
        return stroke
    

# Creer une matrice taille MxN , M = nbpoint tracé, N = nbpoint tracé mot
# remplir les bords à infini
# pour chaque case : distance euclidienne + min 3 cases avant
# récuperer la case en fin de matrice ou faire le chemin (plus avancé)
# comparer seulement avec les mots commençant par la même lettre