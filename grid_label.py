from pkgutil import ImpImporter
from tkinter import *
root = Tk()

for i in range(20):
    for j in range(20):
        Label(root,text="[{},{}]".format(i,j)).grid(row=i,column=j)

root.mainloop()