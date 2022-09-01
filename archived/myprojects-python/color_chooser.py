from tkinter import *
color = colorchooser.askcolor()
print ('hex value =',color[1])
def ask():
    color = colorchooser.askcolor()
    print ('hex value =',color[1])
while True:    
    if messagebox.askyesno(title = 'Query',message = 'Use Again??'):
        ask()
    else:
        break
