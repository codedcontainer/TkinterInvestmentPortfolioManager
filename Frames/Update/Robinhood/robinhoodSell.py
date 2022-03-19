from tkinter import ttk
from tkinter import *
import tkinter as tk
from ButtonCommands.robinhoodSellUpdate import robinhoodSellUpdate
from SetDefaultData.Common import Common
from Common.Helper import *

def robinhoodSell(tkroot):
    tkroot.robinhoodSell = ttk.Frame(tkroot, padding="12 12 12 12")
    tkroot.robinhoodSell.place(relx=.51, rely=0, anchor=N)
    tkroot.columnconfigure(0, weight=1)
    tkroot.rowconfigure(0, weight=1)

    label_rb_head = Label(tkroot.robinhoodSell, text="Robinhood Sell List", font=("*Font", 16))
    label_rb_head.grid(column=1, row =0, sticky=(W), pady=5)

    label_rb = Label(tkroot.robinhoodSell, text="Comma seperated list of stocks interested in selling:")
    label_rb.grid(column=1, row=1, sticky=(W), pady=5)

    input_rb = Text(tkroot.robinhoodSell, width=45, height=10)
    default_robinhood_sell_list = Common.tickers('robinhood_sell', index=1) 
    input_rb.insert(tk.END, default_robinhood_sell_list)
    input_rb.grid(column=1, row=2, sticky=(W, E, N, S)) 
    input_rb.bind("<Tab>", Helper.focus_next_widget)
    input_rb.bind("<Control-a>", Helper.select_all)

    label_rb_update = Label(tkroot.robinhoodSell)
    last_update_date = Common.lastUpdated('robinhood_sell')
    label_rb_update.config(text="Last updated: " + last_update_date)
    label_rb_update.grid(column=1, row=3, sticky=(W))

    tkroot.rbs_label_response = Label(tkroot.robinhoodSell, text="")
    tkroot.rbs_label_response.grid(column=1, row=6, sticky=(W,E))

    button_rb = Button(tkroot.robinhoodSell, text="Update", command=lambda: robinhoodSellUpdate(input_rb, tkroot))
    button_rb.grid(column=1,row=3, sticky=(S,E), pady=5)
    label_response = Label(tkroot.robinhoodSell, text="")
    label_response.grid(column=1, row=5, sticky=(W,E))