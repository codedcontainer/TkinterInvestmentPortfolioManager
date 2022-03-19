from tkinter import ttk
from tkinter import *
import tkinter as tk
from ButtonCommands.fidelitySellUpdate import fidelitySellUpdate
from Common.Helper import *
from SetDefaultData.Common import Common

def fidelitySell(tkroot):
    tkroot.fidelitySell = ttk.Frame(tkroot, padding="12 12 12 12")
    tkroot.fidelitySell.place(relx=.51, rely=0, anchor=N)
    tkroot.columnconfigure(0, weight=1)
    tkroot.rowconfigure(0, weight=1)

    label_rb_head = Label(tkroot.fidelitySell, text="Fidelity Sell List", font=("*Font", 16))
    label_rb_head.grid(column=1, row =0, sticky=(W), pady=5)

    label_rb = Label(tkroot.fidelitySell, text="Comma seperated list of stocks interested in selling:")
    label_rb.grid(column=1, row=1, sticky=(W), pady=5)

    input_rb = Text(tkroot.fidelitySell, width=45, height=10)
    default_fidelity_sell_list = Common.tickers('fidelity_sell', index=1) 
    input_rb.insert(tk.END, default_fidelity_sell_list)
    input_rb.grid(column=1, row=2, sticky=(W, E, N, S)) 
    input_rb.bind("<Tab>", Helper.focus_next_widget)
    input_rb.bind("<Control-a>", Helper.select_all)

    label_rb_update = Label(tkroot.fidelitySell)
    last_update_date = Common.lastUpdated('fidelity_sell')
    label_rb_update.config(text="Last updated: " + last_update_date)
    label_rb_update.grid(column=1, row=3, sticky=(W))

    button_rb = Button(tkroot.fidelitySell, text="Update", command=lambda: fidelitySellUpdate(input_rb, label_response))
    button_rb.grid(column=1,row=3, sticky=(S,E), pady=5)
    label_response = Label(tkroot.fidelitySell, text="")
    label_response.grid(column=1, row=5, sticky=(W,E))