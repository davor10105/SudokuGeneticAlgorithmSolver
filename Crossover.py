import random
from Unit import *

class Crossover():
    def onePointCross(parent1,parent2):
        index=random.randint(1,len(parent1.values)-2)
        child1=Unit([[x for x in row] for row in parent1.scheme])
        child2=Unit([[x for x in row] for row in parent1.scheme])
        p1_values=[[x for x in row] for row in parent1.values]
        p2_values = [[x for x in row] for row in parent2.values]
        child1.values=p1_values[:index]+p2_values[index:]
        child2.values=p2_values[:index]+p1_values[index:]

        return (child1,child2)
