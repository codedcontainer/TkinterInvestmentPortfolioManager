from tkinter import ttk
from tkinter import *
import tkinter as tk
from ButtonCommands.fidelityBuyUpdate import fidelityBuyUpdate
from async_tkinter_loop import async_command
from Common.Helper import *
from SetDefaultData.Common import Common

def fidelityBuy(tkroot):
    tkroot.fidelityBuy = ttk.Frame(tkroot, padding="12 12 12 12")
    tkroot.fidelityBuy.place(relx=.51, rely=0, anchor=N)
    tkroot.columnconfigure(0, weight=1)
    tkroot.rowconfigure(0, weight=1)

    label_rb_head = Label(tkroot.fidelityBuy, text="Fidelity Buy List", font=("*Font", 16))
    label_rb_head.grid(column=1, row =0, sticky=(W), pady=5)

    label_rb = Label(tkroot.fidelityBuy, text="Comma seperated list of stocks interested in buying:")
    label_rb.grid(column=1, row=1, sticky=(W), pady=5)

    input_rb = Text(tkroot.fidelityBuy, width=45, height=10)
    tkroot.default_fidelity_buy_list = Common.tickers('fidelity_buy', index=1)
    input_rb.insert(tk.END, tkroot.default_fidelity_buy_list)
    input_rb.grid(column=1, row=2, sticky=(W, E, N, S)) 
    input_rb.bind("<Tab>", Helper.focus_next_widget)
    input_rb.bind("<Control-a>", Helper.select_all)

    tkroot.label_fidelity_total = Label(tkroot.fidelityBuy, text="Current Price Total: Loading...")
    tkroot.label_fidelity_total.grid(column=1, row=3, sticky=(E), pady=5)

    label_fidelity_update = Label(tkroot.fidelityBuy)
    last_update_date = Common.lastUpdated('fidelity_buy')
    label_fidelity_update.config(text="Last updated: " + last_update_date)
    label_fidelity_update.grid(column=1, row=4, sticky=(W))

    tkroot.fidelity_label_response = Label(tkroot.fidelityBuy, text="")
    tkroot.fidelity_label_response.grid(column=1, row=6, sticky=(W,E))

    button_rb = Button(tkroot.fidelityBuy, text="Update", command=async_command(fidelityBuyUpdate, input_rb, tkroot))
    button_rb.grid(column=1,row=4, sticky=(S,E), pady=5)