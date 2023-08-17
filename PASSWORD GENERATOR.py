import random
from tkinter import *
from tkinter.ttk import *
root = Tk()
root.title("PASSWORD GENERATOR")
def generate():
    entry.delete(0, END)
    length = int(entry1.get(),base=10)
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password = ""
    for i in range(0, length):
	    password = password + random.choice(upper)
    entry.insert(10, password)
txt = Label(root, text="Generate your Password")
txt.grid(row=0,column=1)
Random_password = Label(root, text="Password")
Random_password.grid(row=1)
entry = Entry(root)
entry.grid(row=1, column=1)
label = Label(root, text="Length")
label.grid(row=2)
button = Button(root, text="Generate",command=generate)
button.grid(row=6, column=1)
entry1 = Entry(root)
entry1.grid(column=1, row=2)
root.mainloop()