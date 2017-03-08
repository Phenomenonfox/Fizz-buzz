from tkinter import *
from datetime import datetime, date, time
import os

def notyet(event):
    _field.delete(1.0, END)
    a = len(insert_field.get())
    _field.insert(1.0, a)
root = Tk()
root.title('B-Double Client')
root.geometry('800x400+300+200')
root.resizable(True, True)

menu_frame = Frame(root ,bg='green',bd=5).pack(side=TOP, expand = YES, fill = BOTH)
active_frame1 = Frame(root,height=25, background = 'red', borderwidth = 15).pack(side=BOTTOM)
#insert

_field = Text(active_frame1, height=10, width=7, font='Arial 11', wrap=WORD)
_field.pack(expand=NO, fill = 'x')

button = Button(active_frame1, text='ok',bg='black',fg='red',font='arial 7', command = notyet)
button.pack(side = RIGHT)
insert_field = Entry(active_frame1, font='Arial 11')
insert_field.pack(fill = 'x')
insert_field.bind('<Return>', notyet)
root.mainloop()
