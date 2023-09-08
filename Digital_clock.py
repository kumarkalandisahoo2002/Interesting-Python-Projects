from tkinter import Tk
from tkinter import Label
import time

root = Tk()
root.title("Digital clock")

def present_time():
    display_time = time.strftime("%I:%M:%S %p")
    digital_clock.config(text=display_time)
    digital_clock.after(200,present_time)
    
digital_clock = Label(root, font = ("arial",150), bg = "black", fg = "red")
digital_clock.pack()

present_time()
root.mainloop()