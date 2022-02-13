from tkinter import *
windows= Tk()
windows.title("miles to kms converter")
windows.minsize(250,100)

label=Label(text="miles?", font=24)
label.grid(column =2, row =0)

input=Entry(width=10)
input.grid(column= 1, row = 0)




label2=Label(text="is equal to", font=24)
label2.grid(column =0, row =1)


label3 = Label(text=0, font=24)
label3.grid(column=1, row=1)
def do():
    miles = float(input.get())
    print(miles)
    kms=miles*1.6
    kms=round(kms,2)
    label3.config(text=f"{kms}")

label4=Label(text="kilometers", font=24)
label4.grid(column =2, row =1)





butt=Button(text="Calculate", command=do)
butt.grid(column =1, row=2)
windows.mainloop()