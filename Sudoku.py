class Sudoku:
    def evaluateUnit(unit):
        solve=unit.returnRows()
        error=0
        for row in solve:
            row_set=set()
            for x in row:
                if x in row_set:
                    error+=1
                row_set.add(x)
        for col_i in range(len(solve[0])):
            column_set=set()
            for row_i in range(len(solve)):
                if solve[row_i][col_i] in column_set:
                    error+=1
                column_set.add(solve[row_i][col_i])
        return error

#print(Sudoku.evaluateUnit(None))