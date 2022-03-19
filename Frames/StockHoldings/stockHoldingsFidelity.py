from tkinter import ttk
from tkinter import *
from Common.Helper import Helper
from Common.FinvizScreenerLink import FinvizScreenerLink
from SetDefaultData.Common import Common

def stockHoldingsFidelity(tkroot):
    tkroot.stockHoldingsFidelity = ttk.Frame(tkroot)
    tkroot.stockHoldingsFidelity.place(relx=.15, rely=.02, anchor=NW)

    label_rb_head = Label(tkroot.stockHoldingsFidelity, text="Fidelity Stock Holdings", font=("*Font", 16))
    label_rb_head.grid(column=0, row=0, sticky=(W), pady=10, columnspan=2)

    portfolio_stocks = Common.tickers('fidelity_portfolio')
    finviz_link = FinvizScreenerLink.generateLink(portfolio_stocks.split(','))
    label_rb_sh = Message(tkroot.stockHoldingsFidelity, text=finviz_link, fg="blue", cursor="hand2", width=350)
    label_rb_sh.grid(column=0, row=1, pady=10, columnspan=2 )
    label_rb_sh.bind("<Button-1>", lambda e: Helper.openUrl(finviz_link) )