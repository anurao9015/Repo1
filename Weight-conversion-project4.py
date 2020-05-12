#convert feet to meter

from tkinter import *
from tkinter import ttk
from tkinter import font

root =  Tk() # set up main window
root.title("feet to Meter")   #title of window

def calculate(*args):
    try:
         value= float(feet.get())
         meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass
        

mainframe = ttk.Frame(root,padding="3 3 12 12")   # frame is placed inside main window
mainframe.grid(column=0, row=0, sticky=(N, W, E, S)) #it tells tkinter main windo should expand
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)  #configure row

feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="meters").grid(column=2, row=2, sticky=E)


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate)
root.mainloop()


