from tkinter import *
from tkinter import messagebox

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("note", "Please enter some task.")

def deleteTask():
    lb.delete(ANCHOR)
ws = Tk()
ws.geometry('500x450+500+200')
ws.title('TO-DO-List')
ws.config(bg='Black')
ws.resizable(width=False, height=False)

frame = Frame(ws)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=30,
    height=10,
    font=('arial', 15),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
)

lb.pack(side=LEFT, fill=BOTH)

task_list =[
    'eat apple',
    'drink water',
    'go gym',
    'write code',
    'paint canvas',
    'take a nap',
    ]

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    ws,
    font=('calbiri', 30)
    )

my_entry.pack(pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('arial, 20'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('arial, 20'),
    bg='#ff8b61',
    padx=20,
    pady=10,
        command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

#3mainloop
ws.mainloop()