import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


root = tk.Tk()
root.title('Untitled-Notepad')
root.geometry('700x700')
file = None  # initially file is pointing to nothing


# Added a text widget
textarea = Text(root)
textarea.pack(expand=True, fill=BOTH)

# scroll bar
scrollbar = Scrollbar(textarea)
scrollbar.pack(side=RIGHT, fill=Y)
scrollbar.config(command=textarea.yview)
textarea.config(yscrollcommand=scrollbar.set)


def newfile():
    global file
    root.title('Untitled-Notepad')
    file = None
    textarea.delete(1.0, END)


def openfile():
    global file
    file = askopenfilename(defaultextension="*.txt", filetypes=[
        ("All files", "*.*"), ("Text Documents ", "*.txt"), ("Python files", "*.py")])

    if file == "":
        file = None         # No file to open
    else:
        # try to open the file
        root.title(os.path.basename(file) + "- Notepad")
        textarea.delete(1.0, END)
        f = open(file, "r")
        textarea.insert(1.0, f.read())
        f.close()


def savefile():
    global file
    if file == None:
        # save as new file
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension="*.txt", filetypes=[
            ("All files", "*.*"), ("Text Documents ", "*.txt"), ("Python files", "*.py")])
        if file == "":
            file = None
        else:
            # try to save the file
            root.title(os.path.basename(file) + "- Notepad")
            f = open(file, "w")
            f.write(textarea.get(1.0, END))
            f.close()
    else:
        f = open(file, "w")
        f.write(textarea.get(1.0, END))
        f.close()


def cut():
    textarea.event_generate(("<<Cut>>"))


def copy():
    textarea.event_generate(("<<Copy>>"))

  
def paste():
    textarea.event_generate(("<<Paste>>"))

MenuBar = Menu(root)

# File menu starts
filemenu = Menu(MenuBar, tearoff=0)
filemenu.add_command(label='New', command=newfile)
filemenu.add_command(label='Open', command=openfile)
filemenu.add_command(label='Save', command=savefile)
filemenu.add_command(label='Exit', command=root.quit)
MenuBar.add_cascade(label='File', menu=filemenu)


# edit menu starts
EditMenu = Menu(MenuBar, tearoff=0)
EditMenu.add_command(label='Cut', command=cut)
EditMenu.add_command(label='Copy', command=copy)
EditMenu.add_command(label='Paste', command=paste)
MenuBar.add_cascade(label='Edit', menu=EditMenu)



root.config(menu=MenuBar)

root.mainloop()
