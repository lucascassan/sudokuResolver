from tkintertable import TableCanvas, TableModel
from tkinter import *
import random
from collections import OrderedDict
import numpy as np
import sudokuResolver


listColumn = ["1","2","3","4","5","6","7","8","9"]

data = {'1': {'1': "", '2': "", '3': "", '4': "", '5': "", '6': "", '7': "", '8': "", '9': ""},
        '2': {'1': "", '2': "", '3': "", '4': "", '5': "", '6': "", '7': "", '8': "", '9': ""},
        '3': {'1': "", '2': "", '3': "", '4': "", '5': "", '6': "", '7': "", '8': "", '9': ""},
        '4': {'1': "", '2': "", '3': "", '4': "", '5': "", '6': "", '7': "", '8': "", '9': ""},
        '5': {'1': "", '2': "", '3': "", '4': "", '5': "", '6': "", '7': "", '8': "", '9': ""},
        '6': {'1': "", '2': "", '3': "", '4': "", '5': "", '6': "", '7': "", '8': "", '9': ""},
        '7': {'1': "", '2': "", '3': "", '4': "", '5': "", '6': "", '7': "", '8': "", '9': ""},
        '8': {'1': "", '2': "", '3': "", '4': "", '5': "", '6': "", '7': "", '8': "", '9': ""},
        '9': {'1': "", '2': "", '3': "", '4': "", '5': "", '6': "", '7': "", '8': "", '9': ""} 
        }

data_test = {'1': {'1': "5", '2': "3", '3': "0", '4': "0", '5': "7", '6': "0", '7': "0", '8': "0", '9': "0"},
        '2': {'1': "6", '2': "0", '3': "0", '4': "1", '5': "9", '6': "5", '7': "0", '8': "0", '9': "0"},
        '3': {'1': "0", '2': "9", '3': "8", '4': "0", '5': "0", '6': "0", '7': "0", '8': "6", '9': "0"},
        '4': {'1': "8", '2': "0", '3': "0", '4': "0", '5': "6", '6': "0", '7': "0", '8': "0", '9': "3"},
        '5': {'1': "4", '2': "0", '3': "0", '4': "8", '5': "0", '6': "3", '7': "0", '8': "0", '9': "1"},
        '6': {'1': "7", '2': "0", '3': "0", '4': "0", '5': "2", '6': "0", '7': "0", '8': "0", '9': "6"},
        '7': {'1': "0", '2': "6", '3': "0", '4': "0", '5': "0", '6': "0", '7': "2", '8': "8", '9': "0"},
        '8': {'1': "0", '2': "0", '3': "0", '4': "4", '5': "1", '6': "9", '7': "0", '8': "0", '9': "5"},
        '9': {'1': "0", '2': "0", '3': "0", '4': "0", '5': "8", '6': "0", '7': "0", '8': "7", '9': "9"} 
        }


class TestApp(Frame):
    """Basic test frame for the table"""

    def __init__(self, master=None):
        self.parent = master
        
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()


        Frame.__init__(self)
        self.main = self.primeiroContainer
        f = Frame(self.primeiroContainer)
        f.pack(fill=BOTH,expand=1)
        self.table = TableCanvas(f, data=data, rowheaderwidth=30, cellwidth=6, showkeynamesinheader=True)

        self.table.show()
        self.sair = Button(self.segundoContainer)
        self.sair["text"] = "Resolver Sudoko!"
        self.sair["font"] = ("Verdana", "10")
        self.sair["width"] = 30
        self.sair["command"] = self.resolve
        self.sair.pack (side=RIGHT)
        return
    
    def resolve(self):
        dt = self.table.model.data
        listData = []

        for i in range(0,9):
            for j in range(0,9):
                if dt[listColumn[i]][listColumn[j]] != '':
                    listData.append(int(dt[listColumn[i]][listColumn[j]]))
                else:
                    listData.append(0)

        arrayData = np.array(listData).reshape([9, 9])
        res = (sudokuResolver.retornaSudokuResolvido(arrayData))



        for i in range(0,9):
            for j in range(0,9):
                dt[listColumn[i]][listColumn[j]] = str(res[i][j])
        
        self.table.model.data = dt
        self.table.redraw()
   

app=TestApp()
app.mainloop()
