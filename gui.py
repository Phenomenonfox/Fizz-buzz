from tkinter import *
#импортируем необходимые модули из библиотеки
def button_clicked(x):
	print(len(x))

root = Tk()

ent = Entry()
ent.pack()

button1 = Button()
button1.pack()

button2 = Button(root, bg='red', text = u"CLICK", command = button_clicked(ent))
button2.pack()

okno = Label()
okno.pack()

root.mainloop()