from tkinter import *
root = Tk()
count = 0
def button_click():
    global count
    #It says that I am using the global variable here in this function
    Label(root,text="You clicked me {} times".format(count)).pack()
    count = count + 1
click_button = Button(root,text="Counter",bg="black",fg="white",command=button_click)
click_button.pack()
root.mainloop()
