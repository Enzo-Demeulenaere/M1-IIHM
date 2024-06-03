import sys
import csv
import random as r
import math

nbTarget = None
targetSize = None
minimumPadding = None
h = None
w = None
placedTargets = []

def main(args):
    global nbTarget, targetSize, minimumPadding, h, w, placedTargets

    if (len(args) != 4) :
        print('Incorrect number of arguments. Please provide a target amount (int), target size (int) and minimum padding (int)')
    else :    
        nbTarget = int(args[1])
        targetSize = int(args[2])
        minimumPadding = int(args[3])

        fileName = "targets90-9.csv"
        with open(fileName,'w',newline = '') as csvfile:
            csv_writer = csv.writer(csvfile)

            w,h = 1024-targetSize,800-targetSize
            for i in range (nbTarget):
                x = r.randint(targetSize,w)
                y = r.randint(targetSize,h)
                checkAlreadyPlacedTargets([x,y])
            for target in placedTargets:
                csv_writer.writerow(target)



def checkAlreadyPlacedTargets(currentCenter):
    canBePlaced = True
    for placed in placedTargets:
        placedCenter = [placed[0],placed[1]]
        distance = math.dist(currentCenter,placedCenter)
        if distance < (2 * targetSize) + minimumPadding :
            canBePlaced = False
            newCurrentCenter = [r.randint(targetSize,w),r.randint(targetSize,h)]
            checkAlreadyPlacedTargets(newCurrentCenter)
            return 
    if canBePlaced:
        placedTargets.append(currentCenter)



if __name__ == "__main__":
    main(sys.argv)