import tkinter as tk
from tkinter import *


root=tk.Tk()
root.title('notepad')
root.geometry('700x700')

textarea=Text(root)
textarea.pack(expand=True,fill=BOTH)

# scroll bar
scrollbar = Scrollbar(textarea)
scrollbar.pack(side=RIGHT, fill=Y)
scrollbar.config(command=textarea.yview)
textarea.config(yscrollcommand=scrollbar.set)


def newfile():
    pass
def openfile():
    pass
def savefile():
    pass

def cut():
    textarea.event_generate(("<<Cut>>"))

def copy():
    textarea.event_generate(("<<Copy>>"))

def paste():
    textarea.event_generate(("<<Paste>>"))




MenuBar= Menu(root)

# File menu starts
filemenu = Menu(MenuBar, tearoff=0)
filemenu.add_command(label='New',command=newfile)
filemenu.add_command(label='Open',command=openfile)
filemenu.add_command(label='Save',command=savefile)
filemenu.add_command(label='Exit',command=root.quit)
MenuBar.add_cascade(label='File',menu=filemenu)


# edit menu starts
EditMenu = Menu(MenuBar,tearoff=0)
EditMenu.add_command(label='Cut',command=cut)
EditMenu.add_command(label='Copy',command=copy)
EditMenu.add_command(label='Paste',command=paste)
MenuBar.add_cascade(label='Edit',menu=EditMenu)





root.config(menu=MenuBar)

root.mainloop()
