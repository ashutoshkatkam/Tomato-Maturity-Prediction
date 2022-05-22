from tkinter import *
import urllib.request
url = "http://192.168.1.8"  # ESP's url, ex: https://192.168.102/ (Esp serial prints it when connected to wifi)
data = "no data"
def getSensorvalues():
    global data
    n = urllib.request.urlopen(url).read() # get the raw html data in bytes (sends request and warn our esp8266)
    n = n.decode("utf-8") # convert raw html bytes format to string :3	
    data = n
    Label(root,text=data).grid(row=2,column=1)
    #print(data)
root = Tk()
Label(root,text="Tomato Life Predictor",fg="red",font="bold").grid(row=0,column=0,columnspan=2)
Button(root,text="Click here after placing",command=getSensorvalues).grid(row=1,column=0,columnspan=2)
Label(root,text="Sensor data is").grid(row=2,column=0)
#Entry(root).grid(row=2,column=1)
#Label(root,text=data).grid(row=2,column=1)
print(data)
# Entry(root).grid(row=3,column=1)
# Label(root,text="Parameter 3").grid(row=4,column=0)
# Entry(root).grid(row=4,column=1)
root.mainloop()