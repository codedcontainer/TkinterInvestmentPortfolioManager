from tkinter import ttk
from tkinter import *
import tkinter as tk
from ButtonCommands.robinhoodBuyUpdate import robinhoodBuyUpdate
from SetDefaultData.Common import Common
from async_tkinter_loop import async_command
from Common.Helper import *


def robinhoodBuy(tkroot):
    tkroot.robinhoodBuy = ttk.Frame(tkroot, padding="12 12 12 12")
    tkroot.robinhoodBuy.place(relx=.51, rely=0, anchor=N)
    tkroot.columnconfigure(0, weight=1)
    tkroot.rowconfigure(0, weight=1)

    label_rb_head = Label(tkroot.robinhoodBuy, text="Robinhood Buy List", font=("*Font", 16))
    label_rb_head.grid(column=1, row =0, sticky=(W), pady=5)

    label_rb = Label(tkroot.robinhoodBuy, text="Comma seperated list of stocks interested in buying:")
    label_rb.grid(column=1, row=1, sticky=(W), pady=5)

    input_rb = Text(tkroot.robinhoodBuy, width=45, height=10)
    tkroot.default_robinhood_buy_list = Common.tickers('robinhood_buy',index=1)
    input_rb.insert(tk.END, tkroot.default_robinhood_buy_list)
    input_rb.grid(column=1, row=2, sticky=(W, E, N, S)) 
    input_rb.bind("<Tab>", Helper.focus_next_widget)
    input_rb.bind("<Control-a>", Helper.select_all)

    tkroot.label_rb_total = Label(tkroot.robinhoodBuy, text="Current Price Total: Loading...")
    tkroot.label_rb_total.grid(column=1, row=3, sticky=(E), pady=5)

    label_rb_update = Label(tkroot.robinhoodBuy)
    last_update_date = Common.lastUpdated('robinhood_buy')
    label_rb_update.config(text="Last updated: " + last_update_date)
    label_rb_update.grid(column=1, row=4, sticky=(W))

    tkroot.rb_label_response = Label(tkroot.robinhoodBuy, text="")
    tkroot.rb_label_response.grid(column=1, row=6, sticky=(W,E))

    button_rb = Button(tkroot.robinhoodBuy, text="Update", command= async_command(robinhoodBuyUpdate, input_rb, tkroot))
    button_rb.grid(column=1,row=4, sticky=(S,E), pady=5)
    