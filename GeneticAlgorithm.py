from Unit import *
from Selection import *
from Crossover import *
from Mutation import *
from Function import *
import random
from Sudoku import *

class GeneticAlgorithm():

    def run(self):
        for i in range(len(self.population)):
            self.population[i].fitness=Sudoku.evaluateUnit(self.population[i])
            #print(self.population[i])

        for i in range(self.iterations):
            if i%100==0:
                print("ITERATION: "+str(i))
            best_unit=self.iteration(i)
            if best_unit!=None:
                break
        self.population=sorted(self.population,key=lambda x:x.fitness)
        return self.population[0]


class GeneticAlgorithmElimination(GeneticAlgorithm):
    def __init__(self,scheme,popsize,mutation=0.01,iterations=1000):
        self.scheme=scheme
        self.population=[Unit(self.scheme) for i in range(popsize)]
        self.iterations=iterations
        self.popsize=popsize
        self.mutation=mutation

        self.lastFitness=None

    def iteration(self,index):
        self.population=sorted(self.population,key=lambda x:x.fitness)

        if self.lastFitness==None or self.lastFitness>self.population[0].fitness:
            self.lastFitness=self.population[0].fitness
            print('iteration '+str(index)+': '+str(self.population[0].fitness))
            if self.lastFitness==0:
                return self.population[0]

        for i in range(self.popsize//3):

            tournament=[]
            tournament.append(Selection.selectRandomIndex(self.population))
            while len(tournament)<3:
                new_index=Selection.selectRandomIndex(self.population)
                if new_index not in tournament:
                    tournament.append(new_index)

            tournament=sorted(tournament,key=lambda x:self.population[x].fitness)
            parent1=self.population[tournament[0]]
            parent2=self.population[tournament[1]]
            #print(parent1.fitness,parent2.fitness,self.population[tournament[2]].fitness)


            child1,child2=Crossover.onePointCross(parent1,parent2)


            child1=Mutation.simpleMutate(child1,self.mutation)
            child2=Mutation.simpleMutate(child2,self.mutation)

            child1.fitness=Sudoku.evaluateUnit(child1)
            child2.fitness=Sudoku.evaluateUnit(child2)

            if child1.fitness<child2.fitness:
                self.population[tournament[len(tournament)-1]]=child1

            else:
                self.population[tournament[len(tournament)-1]]=child2
            #print("switched " + str(tournament[len(tournament)-1]))





