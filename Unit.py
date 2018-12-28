import random
from Sudoku import *

class Unit():
    def __init__(self,scheme):
        self.scheme=scheme
        self.values=[[-1 for x in row] for row in scheme]

        for i in range(len(scheme)):
            sampleList=list(range(1,len(scheme[i])+1))
            for j in range(len(scheme[i])):
                if scheme[i][j]==-1:
                    while True:
                        random_num=random.randint(0,len(sampleList)-1)
                        if sampleList[random_num] not in self.scheme[i]:
                            self.values[i][j]=sampleList[random_num]
                            del sampleList[random_num]
                            break
                        del sampleList[random_num]
                else:
                    self.values[i][j]=scheme[i][j]
        self.fitness=None
    def returnRows(self):
        retVal=[[] for square in self.values]
        square_size=int(round(len(self.scheme[0])**(1./2)))

        for i in range(square_size):
            currentRow=[]
            for j in range(len(self.values)):
                currentRow+=self.values[j][i*square_size:(i+1)*square_size]
            for j in range(square_size):
                retVal[i+j*square_size]=currentRow[j*square_size**2:(j+1)*square_size**2]

        return retVal
    def __str__(self):
        return str(self.values)
