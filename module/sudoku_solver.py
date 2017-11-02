import numpy as np

class sudoku:
    def __init__(self):

        """self.sudoku = np.array([[5, 0, 0, 4, 0, 0, 0, 0, 1], [0, 8, 0, 0, 2, 5, 9, 0, 6], [6, 0, 7, 1, 0, 0, 2, 0, 0],
         [0, 0, 2, 0, 0, 7, 6, 1, 0], [0, 0, 1, 0, 4, 8, 3, 0, 0], [0, 5, 3, 0, 0, 6, 8, 0, 0],
         [0, 0, 8, 0, 0, 2, 1, 0, 3], [2, 0, 5, 9, 3, 0, 0, 6, 0], [3, 0, 0, 0, 0, 4, 0, 0, 9]])"""
        self.sudoku = np.array([[8,0,0,0,0,0,0,0,0],[0,0,3,6,0,0,0,0,0],[0,7,0,0,9,0,2,0,0],[0,5,0,0,0,7,0,0,0],[0,0,0,0,4,5,7,0,0],[0,0,0,1,0,0,0,3,0],[0,0,1,0,0,0,0,6,8],[0,0,8,5,0,0,0,1,0],[0,9,0,0,0,0,4,0,0]])
        self.values = []
        for i in range(0,81):
            self.values.append([1,2,3,4,5,6,7,8,9])
        self.process_loop()
        print(self.sudoku)


    def check_nonprintable_values(self):
        for i in range(0,9):
            for j in range(0,9):
                self.del_values(value=self.sudoku[i][j],row=i)
                self.del_values(value=self.sudoku[i][j],column=j)
                self.del_values(value=self.sudoku[i][j],row=i,column=j)

    def del_values(self,value,row=-1,column=-1):
        if row != -1 and column != -1:
            square_row = row // 3
            square_column = column // 3
            for i in range(0,3):
                for j in range(0,3):
                    if self.sudoku[i+square_row*3][j+square_column*3] == 0:
                        try:
                            self.values[((i+square_row*3))*9+(j+square_column*3)].remove(value)
                        except:
                            print("asdasd")
        elif row != -1:
            for j in range(0,9):
                if self.sudoku[row][j] == 0:
                    try:
                        self.values[row*9+j].remove(value)
                    except:
                        pass
        elif column != -1:
            for i in range(0,9):
                if self.sudoku[i][column] == 0:
                    try:
                        self.values[i*9+column].remove(value)
                    except:
                        pass

    def check_last_value(self):
        for i in range(0,81):
            if self.values[i].__len__() == 1:
                self.sudoku[i//9][i%9] = self.values[i][0]

    def process_loop(self):
        i = 0
        while(i<1000):
            self.check_nonprintable_values()
            self.check_last_value()
            i += 1


a = sudoku()