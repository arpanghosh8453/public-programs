from tkinter import *
from tkinter import ttk
root = Tk()
logo = PhotoImage(file = 'C:\\Users\\arpan\\Desktop\\Exercise Files\\Ch03\\python_logo.jpg')
small_image = logo.subsample(7,7)
entry = ttk.Entry(root,width = 100)
button = ttk.Button(root,text = 'I want to see')
button.config(image = small_image,compound = LEFT)
button1 = ttk.Button(root,text = 'Repair')
button1.config(image = small_image,compound = RIGHT)
entry.pack()
button.pack()
button1.pack()
button1.state(['disabled'])
def click(val):
    entry.state(['disabled'])
    button1.state(['!disabled'])
    button.state(['disabled'])
    messagebox.showinfo(title = 'Entry Window',message = val)
def repair(val):
    entry.state(['!disabled'])
    button.state(['!disabled'])
    button1.state(['disabled'])
    entry.delete(0,END)
    messagebox.showinfo(title = 'Repairer',message = val)
entry.config(show = '?')
button.config(command = lambda:click(entry.get()))
button1.config(command = lambda:repair('Window Repaired'))





