from Unit import *
from Sudoku import *

scheme=[[-1,-1,-1,2],[-1,-1,-1,1],[4,-1,-1,-1],[2,-1,-1,-1]]
for i in range(100):
    a=Unit(scheme)
    if Sudoku.evaluateUnit(a)==0:
        print(a)
#print(a.returnRows())
#print(Sudoku.evaluateUnit(a))