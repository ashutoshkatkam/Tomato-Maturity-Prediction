from tkinter import *
from PIL import Image,ImageTk
def getSensorValues():
    pass
root = Tk()
root.title("Tomato Maturity Predictor")
head_label = Label(root,text="Tomato Prediction App",font="OpenSans")
head_label.grid(row=0,column=0,columnspan=2)
empty_label1 = Label(root,text="")
empty_label1.grid(row=1,column=0,columnspan=2)
sensor_button = Button(root,text="Click here to get Sensor Values",command=getSensorValues,bg="Green")
sensor_button.grid(row=2,column=0,columnspan=2)
empty_label2 = Label(root,text="")
empty_label2.grid(row=1,column=0,columnspan=2)
sensor_value_label = Label(root,text="Fruit Colour \nvalues are",font="OpenSansBold",justify=LEFT)
sensor_value_label.grid(row=3,column=0,columnspan=1)
sensor_values_measured = Label(root,text="R:255 G:200 B:125")
sensor_values_measured.grid(row=3,column=1,columnspan=1)
status_label = Label(root,text="Status",font="OpenSans")
status_label.grid(row=4,column=0)
status_value_label = Label(root,text="Connecting...")
status_value_label.grid(row=4,column=1)
#Expected Time to delivery Block
ex_time_label = Label(root,text="Estimated \nmarket time",font="OpenSans",justify=LEFT)
ex_time_label.grid(row=5,column=0)
time_entry = Entry(root)
time_entry.grid(row=5,column=1)

#requirement type
req_label = Label(root,text="Requirement \nType",font="OpenSans",justify=LEFT)
req_label.grid(row=6,column=0)
#drop menu
clicked = StringVar()
clicked.set("Breaker")
drop = OptionMenu(root,clicked,"Breaker","Pink","Red")
drop.grid(row=6,column=1)
print(clicked.get())

#Harvest Colour
Harvest_label = Label(root,text="Harvest \nColour",font="OpenSans",justify=LEFT)
Harvest_label.grid(row=7,column=0)
# colour = Label(root,text="Red")
# colour.grid(row=7,column=1)

#canvas
my_canvas = Canvas(root,width=80,height=20,bg="maroon")
my_canvas.grid(row=7,column=1)

graph = ImageTk.PhotoImage(Image.open("graph.png"))
graph_label = Label(root,image=graph,height=200,width=200)
graph_label.grid(row=8,column=0,columnspan=2)
root.mainloop()