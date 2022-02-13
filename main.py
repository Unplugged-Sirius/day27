from tkinter import *

window = Tk()
window.title("my first gui program")

window.minsize(500,500)


label=Label(text="im here")
label.grid(column=0,row=0)


new_button=Button(text="new boob")
new_button.grid(column=2, row =0)


input = Entry(width=10)
input.grid(column=3,row =3)

def dos():
    label.config(text=input.get())

button = Button(text="click me", command=dos)
button.grid(column= 1,row= 1)
window.mainloop()