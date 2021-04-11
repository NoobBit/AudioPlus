import os
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import sapiva

root = Tk()
root.title('AudioPlus')
root.geometry('290x125')


def open_doc():
    global code
    path = askopenfilename(filetypes=[('Text Documents', '*.txt'), ('PDF', '*.pdf'), ('All Files', '*.*')])
    try:
        root.title('AudioPlus - ' + os.path.basename(path))
        with open(path, 'r') as file:
            code = file.read()
    except EXCEPTION:
        sapiva.speak('File Could Not be Read')
    finally:
        path.close()


def read_doc():
    sapiva.set_rate(125)
    sapiva.set_volume(1.0)
    sapiva.speak(code)


l_1 = Label(text='AudioPlus', font=('Arial', 12))
l_1.grid(row=0, column=0, padx=10, pady=10)

open_button = Button(text='Open', command=open_doc)
open_button.grid(row=1, column=1, pady=10, padx=0)

open_button = Button(text='Read', command=read_doc)
open_button.grid(row=1, column=2, pady=10, padx=50)

root.mainloop()