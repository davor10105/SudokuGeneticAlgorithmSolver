import random

class Mutation():
    def simpleMutate(child,pm):
        for i in range(len(child.values)):
            if random.random()<=pm:
                indexes_of_fixed=[]
                random_indexes=[]
                for j in range(len(child.values[i])):
                    if child.scheme[i][j]!=-1:
                        indexes_of_fixed.append(j)
                if len(indexes_of_fixed)>=len(child.values)-1:
                    continue
                while len(random_indexes)<2:
                    random_index=random.randint(0,len(child.values)-1)
                    #print(indexes_of_fixed)
                    if random_index not in indexes_of_fixed:
                        random_indexes.append(random_index)
                t=child.values[i][random_indexes[0]]
                child.values[i][random_indexes[0]]=child.values[i][random_indexes[1]]
                child.values[i][random_indexes[1]]=t

        return child
