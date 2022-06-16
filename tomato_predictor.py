from tkinter import *
import urllib.request
url = "http://192.168.1.8"  # ESP's url, ex: https://192.168.102/ (Esp serial prints it when connected to wifi)
data = "no data"
def predict_colour(int_readings,temp,humidity,time):
    final_a = -44.8955 + (0.8523*int_readings[0]) + (5.8093*temp) + (0.1442 * humidity) + (1.0911 * time) + (0.0052 * (int_readings[0]**2)) - (0.1053 * (temp**2)) + (0.0018 * (humidity**2)) - (0.0307*(time**2)) - (0.0218*int_readings[0]*temp) - (0.0011*int_readings[0]*humidity)-(0.0165*int_readings[0]*time)-(0.0275*temp*humidity)+(0.0153*temp*time)+(0.0058*humidity*time)
    final_h = 49.9931 + (0.9175*int_readings[1]) - (7.393*temp) + (0.3946 * humidity) - (0.1461 * time) + (0.0036 * (int_readings[1]**2)) + (0.1250 * (temp**2)) - (0.0031 * (humidity**2)) + (0.045*(time**2)) - (0.0166*int_readings[1]*temp) - (0.0019*int_readings[1]*humidity)-(0.0156*int_readings[1]*time)+(0.0572*temp*humidity)-(0.0142*temp*time)-(0.0108*humidity*time)
    fin_value = (final_a,final_h)
    return fin_value
# def lab_to_rgb(a,h):
#     r = 
#     g = 
#     b = 
#     return (r,g,b)

def getSensorvalues():
    global data
    n = urllib.request.urlopen(url).read() # get the raw html data in bytes (sends request and warn our esp8266)
    n = n.decode("utf-8") # convert raw html bytes format to string :3	
    data = n
    Label(root,text=data).grid(row=2,column=1)
    for i in range(0,42,3):
        print(predict_colour((-8.78,108.07),15,70,i))
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
