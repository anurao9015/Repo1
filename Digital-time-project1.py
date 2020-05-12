from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import datetime

root = Tk()
def quit(*args):
   root.destroy()


def clocktime():
      time = datetime.datetime.now()
      time = (time.strftime("%d/%m/%y %H:%M:%S"))
      txt.set(time)

      root.after(1000,clocktime)


root.attributes("-fullscreen",False)
root.configure(background="black")
root.bind("x",quit)
root.after(1000,clocktime)

fnt = font.Font(family='Helvetica', size=100, weight='bold')
txt = StringVar()
lbl = ttk.Label(root,textvariable=txt, font=fnt, foreground='white', background='black')
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()

                   
 

