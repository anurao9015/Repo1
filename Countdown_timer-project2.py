from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import datetime

root = Tk()
global  endTime

def quit(*args):
    root.destroy()

def cant_wait():
    timeLeft = endTime - datetime.datetime.now()
    timeLeft = timeLeft -datetime.timedelta(microseconds=timeLeft.microseconds)

    txt.set(timeLeft)
    root.after(1000,cant_wait)

root.attributes("-fullscreen",False)
root.configure(background="black")
root.bind("x",quit)
root.after(1000,cant_wait)

endTime = datetime.datetime(2020,5,20,0,0)

fnt = font.Font(family='Helvetica', size=100, weight='bold')
txt = StringVar()
lbl = ttk.Label(root,textvariable=txt, font=fnt, foreground='white', background='black')
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()

                   
 



    





