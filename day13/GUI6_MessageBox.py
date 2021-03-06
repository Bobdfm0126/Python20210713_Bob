import tkinter
from tkinter import messagebox as msg


def show_info():
    r = msg.showinfo('showinfo', 'This is [showinfo] dialog')
    result.set(r)
    print(r)


def show_askokcancel():
    r = msg.askokcancel('askokcancel', 'This is [askokcancel] dialog')
    result.set(r)
    print(r)


def show_askyesno():
    r = msg.askyesno('askyesno', 'This is [askyesno] dialog')
    result.set(r)
    print(r)


def show_askyesnocancel():
    r = msg.askyesnocancel('show_askyesnocancel', 'This is [askyesnocancel] dialog')
    result.set(r)
    print(r)


win = tkinter.Tk()
win.title("message box")
win.geometry("300x300")

b1 = tkinter.Button(win, text="show_info", command=show_info)
b1.pack()

b2 = tkinter.Button(win, text="show_askokcancel", command=show_askokcancel)
b2.pack()

b3 = tkinter.Button(win, text="show_askyesno", command=show_askyesno)
b3.pack()

b4 = tkinter.Button(win, text="show_askyesnocancel", command=show_askyesnocancel)
b4.pack()

result = tkinter.StringVar()
result.set("?")
label = tkinter.Label(win, textvariable=result, font=('Arial', 100))
label.pack()

win.mainloop()