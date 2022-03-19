from tkinter import *
from async_tkinter_loop import async_mainloop
from Database.DatabaseInit import DatabaseInit
from Menu.MainMenu import MainMenu
from Menu.MenuCommands import *

DatabaseInit()

root = Tk()
root.geometry('500x350')
root.minsize(width=500, height=400)
root.maxsize(width=500, height=400)

title_icon = PhotoImage(file="title-icon.png")
root.iconphoto(False, title_icon)

root.title("Investment Portfolio Management")
_mainMenu = MainMenu(tkRoot=root)
index(root)

root.config(menu=_mainMenu.menubar)
async_mainloop(root)
