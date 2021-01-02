import random
from tkinter import * 

root = Tk() # To create a tkinter GUI instance
root.geometry("700x450") # 700 x 450

l1 = Label(root, font=("times", 200)) # 200 is the size and  times is the font style

def roll():
    number = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685'] # unicode characters for the number to be displayed on dice
    l1.config(text=f'{random.choice(number)}{random.choice(number)}')
    l1.pack()

b1 = Button(root,text="lets roll....",command=roll) # this Button triggers a function roll to generate random numbers

b1.place(x = 330, y = 0) # placing the button at top-mid

root.mainloop() # to run the GUI instance