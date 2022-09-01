#!/usr/bin/python3
# mouse.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com
global color
color = 'black'
from tkinter import *
from tkinter import ttk
def pickcolor():
    global color
    tupleColor = colorchooser.askcolor(initialcolor = 'black')
    color = tupleColor[1]
button = ttk.Button(text = 'click',command = pickcolor)
button.pack()
def mouse_press(event):
    global prev
    print('type: {}'.format(event.type))
    print('widget: {}'.format(event.widget))
    print('num: {}'.format(event.num)) 
    print('x: {}'.format(event.x))
    print('y: {}'.format(event.y))
    print('x_root: {}'.format(event.x_root))
    print('y_root: {}\n'.format(event.y_root))
    prev = event

def draw(event):
    global prev
    global color
    canvas.create_line(prev.x, prev.y, event.x, event.y, width = 5,fill = color)
    prev = event
    
root = Tk()

canvas = Canvas(root, width = 640, height = 480, 
                background = 'white')
canvas.pack()
canvas.bind('<ButtonPress>', mouse_press)
canvas.bind('<B1-Motion>', draw)

root.mainloop()
