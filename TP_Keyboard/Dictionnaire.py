from KeyboardWidget import *
import numpy as np
import math

class Mot:

    def __init__(self,word,trace):
        super().__init__()
        self.word = word 
        self.trace = trace
    
class Dictionnaire:

    def __init__(self,keyboard):
        super().__init__()
        self.keyboard = keyboard
        self.createDico()

    def createDico(self):
        self.dico = []
        with open("words.txt",'r') as file:
            for line in file:
                trace = self.keyboard.wordToStroke(line,self.keyboard.sampleDist)
                word = Mot(line,trace)
                self.dico.append(word)

    def findWords(self,stroke,firstKey,nbReco):
        # this will hold our foundWords at the end of the algorithm
        foundWords = []
        firstLetter = firstKey.symbol
        # we filter the words starting with the same letter
        wordsToSearch = list(filter(lambda x: x.word.startswith(firstLetter), self.dico))
        #we will store results of DTW in this dict
        resultsDTW = {}
        for word in wordsToSearch:
            #we apply the DTW
            dist = self.dtw(stroke,word.trace)
            # we put the word and its dist into the dict
            resultsDTW[word]=dist
        # We can now filter the minimum dist words
        sortedDict = dict(sorted(resultsDTW.items(),key= lambda item: item[1]))
        foundWords= list(sortedDict.keys())[:nbReco]
        return foundWords
    
    def dtw(self,stroke,wordTrace):
        matrix = np.empty([len(stroke),len(wordTrace)])
        matrix[0,1:]= np.inf
        matrix[1:,0]= np.inf
        matrix[0,0]= math.dist([stroke[0].x(),stroke[0].y()],[wordTrace[0].x(),wordTrace[0].y()])
        # need to fill up the matrix
        for i in range (1,len(stroke)):
            for j in range(1,len(wordTrace)):
                matrix[i,j]= math.dist([stroke[i].x(),stroke[i].y()],[wordTrace[j].x(),wordTrace[j].y()]) + min(matrix[i-1,j],matrix[i,j-1],matrix[i-1,j-1])
        return matrix[-1,-1]
    
# stroke = [(1,1),(2,2),(3,3)]
# wordTrace = [(4,4),(5,5),(6,6),(7,7)]
# matrix = np.zeros([len(stroke)+1,len(wordTrace)+1,2])
# matrix[1:,0]= stroke
# matrix[0,1:]= wordTrace
# matrix[1,2:]= np.inf
# matrix[2:,1]= np.inf
# matrix[1,1]= math.dist(stroke[0],wordTrace[0])
# print(matrix)