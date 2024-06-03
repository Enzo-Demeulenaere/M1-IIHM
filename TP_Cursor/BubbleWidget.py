from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Target import *
from BubbleCursor import *
from RopeCursor import *
from XPManager import *
import random
import time

class BubbleWidget(QWidget):
    def __init__(self,targetsFile,manager):
        super().__init__()
        self.targets = []
        self.setMouseTracking(True)
        self.readFile(targetsFile)
        self.cursor = BubbleCursor(self.targets)
        self.timeSinceClick = None
        self.nbTargetsToClick = 15
        self.nbTargetsClicked = 0
        self.nbErrors = 0
        self.manager = manager
        self.results = []
        self.selectNewTarget()
        
    def readFile(self,fileName):
        with open(fileName,"r") as file:
            for line in file:
                infos = line.split(',')
                x,y = int(infos[0]),int(infos[1])
                lastPart = fileName.split("-")[1]
                size = int(lastPart.split(".")[0])
                self.targets.append(Target(x,y,size))

    def paintEvent(self,event):
        painter = QPainter(self)
        for target in self.targets:
            target.paint(painter)
        self.cursor.paint(painter)

    def mouseMoveEvent(self,event):
        self.cursor.move(event.pos().x(),event.pos().y())
        self.update()

    def selectNewTarget(self):
        if (self.timeSinceClick == None):
            self.timeSinceClick=time.time()
        else:
            timeTaken = time.time()-self.timeSinceClick
            self.timeSinceClick = time.time()
            self.results.append([str(timeTaken*1000),str(self.nbErrors)])
            print('Temps de selection :{} ms '.format(timeTaken*1000))
            self.nbErrors = 0
        selected = self.targets[self.nbTargetsClicked]
        selected.toSelect = True
    
    def writeResults(self):
        
        with open("results.csv",'a') as file:

            for i in range(len(self.results)):
                m = self.manager
                line = [m.userID,m.technique,m.density,m.targetSize,str(i+1)]
                line = line+self.results[i]
                line = ';'.join(line)
                file.writelines(line + ";\n") 

    def mousePressEvent(self,event):
        closest = self.cursor.closest
        if (closest.toSelect):
            closest.toSelect = False
            self.nbTargetsClicked+=1
            self.selectNewTarget()
            self.update()
            if self.nbTargetsClicked == self.nbTargetsToClick:
                self.writeResults()
                self.close()
                self.manager.launchNext()
        else :
            self.nbErrors+=1
