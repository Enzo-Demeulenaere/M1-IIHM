from itertools import product
import subprocess as sp
from importlib import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from NormalWidget import *
from BubbleWidget import *
from RopeWidget import *

class XPManager: 


    def __init__(self,userID,window):
        super().__init__()
        self.userID=userID
        self.window = window
        self.queue = [] 


    def initCombinations(self):
        densities = ["30","90"]
        targetSizes = ["9","18"]
        techniques = ["Normal","Bubble","Rope"]

        self.queue = list(product(techniques,densities,targetSizes))
        self.queue += self.queue  #to have 2 repetitions 
        self.launchNext()

    def launchNext(self):
        if len(self.queue) != 0:
            combination = self.queue.pop(0) 
            self.launch(combination)
        else:
            self.window.close()

    def launch(self,combination):
        self.window.resize(1024,800)
        self.technique,self.density,self.targetSize = combination

        targetsFile = "targets"+self.density+"-"+self.targetSize+".csv"

        
        widget = None
        if self.technique == "Normal":
            widget = NormalWidget(targetsFile,self)
        elif self.technique == "Bubble":
            widget = BubbleWidget(targetsFile,self)
        else:
            widget = RopeWidget(targetsFile,self) 

        self.window.setCentralWidget(widget)

    def sendResults(results):

        for res in results:
            print(res)
            print("=============")