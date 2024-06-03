import math
from PyQt5.QtCore import *
from PyQt5.QtCore import QSize
from PyQt5.QtGui import *
from PyQt5.QtGui import QMouseEvent, QResizeEvent
from PyQt5.QtWidgets import *

class Reconnaisseur:


    def interpolate(a,b,d):
        ax, ay = a.x(),a.y()
        bx, by = b.x(),b.y()
        ratio = d / math.dist((ax,ay),(bx,by))
        if ratio >= 1:
            return b 
        px = ax + (bx-ax) * ratio
        py = ay + (by-ay) * ratio
        return QPoint(int(px),int(py))
    
    def resample(stroke,d):
        i = 0
        newStroke = []
        currentDist = 0
        while i < len(stroke)-1:
            point = stroke[i]
            nextPoint = stroke[i+1]
            if ( currentDist < d):
                currentDist += math.dist((point.x(),point.y()),(nextPoint.x(),nextPoint.y()))
            else:
                interpolated = Reconnaisseur.interpolate(point,nextPoint,d-currentDist)
                currentDist = 0
                newStroke.append(interpolated)
            i+=1
        return newStroke