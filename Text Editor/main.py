#!/usr/bin/python
# -*- coding: utf-8 -*-
# Said Gourida



from tkinter import *

root=Tk()
root.title("Moino")
#root.resizable(True,True)
root.state('zoomed')


menu=Menu(root)
root.config(menu=menu)

#-------   make first menu   ---------
first=Menu(menu,tearoff=0)
menu.add_cascade(label="File",menu=first)
first.add_command(label="New",accelerator="Ctrl+N")
first.add_command(label="Open...,",accelerator="Ctrl+O")
first.add_command(label="Close",accelerator="Ctrl+W")

#make separator between the labels
first.add_separator()

first.add_command(label="Sava",accelerator="Ctrl+S")
first.add_command(label="Sava As...",accelerator="Ctrl+Shift+S")

#make separator between the labels
first.add_separator()

first.add_command(label="Page Setup...")
first.add_command(label="Quit",accelerator="Ctrl+Q")

#-------   make second menu   ---------
second=Menu(menu,tearoff=0)

menu.add_cascade(label="Edit",menu=second)
second.add_command(label="Cut",accelerator="Ctrl+X")
second.add_command(label="Copy",accelerator="Ctrl+C")
second.add_command(label="Paste",accelerator="Ctrl+V")
second.add_command(label="Clear")

# make separator between the labels
second.add_separator()

# add new menu inside label select
select_menu=Menu(second,tearoff=0)
second.add_cascade(label="Select",menu=select_menu)
select_menu.add_command(label="Select All",accelerator="Ctrl+A")
select_menu.add_command(label="Select More",accelerator="Ctrl+Up")
select_menu.add_command(label="Select Less",accelerator="Ctrl+Down")

ser_rep=Menu(second,tearoff=0)
menu.add_cascade(label="Search and replace",menu=ser_rep)
ser_rep.add_command(label="Search",accelerator="Ctrl+F")
ser_rep.add_command(label="Replace",accelerator="Ctrl+H")
second.add_command(label="Goto Line...")

#-------   make third menu   ---------
third=Menu(menu,tearoff=0)
menu.add_cascade(label="Project",menu=third)
third.add_command(label="New Project...")
third.add_command(label="Open Project...")

select_menu1=Menu(third,tearoff=0)
third.add_cascade(label="Recent",menu=select_menu1)
select_menu1.add_command(label="Default Project")

third.add_command(label="Add New File")
third.add_command(label="Add Existing File")

# make separator 
third.add_separator()
third.add_command(label="Show Current File in Project Tool")
# make separator 
third.add_separator()
third.add_command(label="Project Properties...")

#-------   make last menu   ---------
last=Menu(menu,tearoff=0)
menu.add_cascade(label="Help",menu=last)
last.add_command(label="Moino Manual")
last.add_command(label="Tutorial")

# make separator 
last.add_separator()
last.add_command(label="Python Manual (HTML)...")
last.add_command(label="Python Website...")
last.add_command(label="Python Interface to Tcl/Tk")
last.add_command(label="Python Turtle Graphics")
# make separator 
last.add_separator()
last.add_command(label="Check for Updates...")
last.add_command(label="About...")


root.mainloop()
