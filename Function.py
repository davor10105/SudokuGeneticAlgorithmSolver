import math

class Function():
    def __init__(self,f,file,numvars):
        self.f=f
        self.numvars=numvars
        self.inputs=[]

        with open(file,'r') as f_input:
            for line in f_input.readlines():
                x,y,fxy=line[:-1].split('\t')
                self.inputs.append([float(x),float(y),float(fxy)])
    def __call__(self,values):
        #returns a list of tuples (value,realValue)
        retVal=[]
        for line in self.inputs:
            value=self.f(line[:-1]+values)
            retVal.append((value,line[-1]))
        return retVal

#a=Function(lambda x: math.sin(x[2]+x[3]*x[0])+x[4]*math.cos(x[0]*(x[5]+x[1]))+1./(1+math.exp((x[0]-x[6])**2)),'zad4-dataset1.txt',5)

#print(a([0,0,0,0,0]))
