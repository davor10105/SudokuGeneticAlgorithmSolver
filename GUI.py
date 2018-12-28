import tkinter as tk
from GeneticAlgorithm import *

class SudokuGUI(tk.Frame):

    def __init__(self, master=None,sudoku_size=2):
        super().__init__(master)
        self.master = master
        self.sudoku_size=sudoku_size

        self.boxes=[]
        k=0
        for sq_i in range(sudoku_size):
            for sq_j in range(sudoku_size):
                for i in range(sudoku_size):
                    for j in range(sudoku_size):
                        content=tk.StringVar()
                        entry_box=tk.Entry(master,textvariable=content,font="Calibri 36",width=3,justify='center')
                        self.boxes.append(content)
                        entry_box.grid(row=sq_i*sudoku_size+i,column=sq_j*sudoku_size+j)
                        k += 1
        solve = tk.Button(master, text="SOLVE",command=self.startSolve)
        solve.grid(row=sudoku_size**2,column=0)
        clear=tk.Button(master, text="CLEAR",command=self.clear)
        clear.grid(row=sudoku_size ** 2, column=1)
        clear_with_scheme = tk.Button(master, text="SCHEME", command=self.clearWithScheme)
        clear_with_scheme.grid(row=sudoku_size ** 2, column=2)

    def startSolve(self):
        self.scheme=[]
        for i in range(self.sudoku_size**2):
            self.scheme.append(self.boxes[i*self.sudoku_size**2:(i+1)*self.sudoku_size**2])
        self.scheme=[[-1 if x.get()=="" else int(x.get()) for x in row] for row in self.scheme]

        print(self.scheme)


        genetic_algorithm = GeneticAlgorithmElimination(self.scheme, 100, 0.1, 1000)
        best_unit = genetic_algorithm.run()
        k=0
        print(best_unit.returnRows())

        for row in best_unit.values:
            for x in row:
                self.boxes[k].set(str(x))
                k+=1

        print(best_unit.fitness)

    def clear(self):
        for box in self.boxes:
            box.set("")
    def clearWithScheme(self):
        k=0
        for row in self.scheme:
            for x in row:
                if x==-1:
                    self.boxes[k].set("")
                k+=1





root=tk.Tk()
app = SudokuGUI(master=root,sudoku_size=2)
app.mainloop()
