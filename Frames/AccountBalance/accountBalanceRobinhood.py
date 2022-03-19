from tkinter import ttk
from tkinter import *
from SetDefaultData.Common import Common

def accountBalanceRobinhood(tkroot):
    tkroot.accountBalanceRobinhood = ttk.Frame(tkroot, padding="12 12 12 12")
    tkroot.accountBalanceRobinhood.place(relx=.41, rely=-.01, anchor=N)

    label_abr_head = Label(tkroot.accountBalanceRobinhood, text="Robinhood Account Balance", font=("*Font", 16))
    label_abr_head.grid(column=1, row=0, sticky=(W), pady=10, columnspan=2)

    purchasing_power = Common.purchasingPower('robinhood_account')
    label_abr_pp = Label(tkroot.accountBalanceRobinhood, text="Purchasing Power: ${:,.2f}".format(purchasing_power))
    label_abr_pp.grid(column=1, row=1, sticky=(W), pady=5, padx=5) 

    account_value = Common.accountBalance('robinhood_account')
    label_abr_av = Label(tkroot.accountBalanceRobinhood, text="Account Value: ${:,.2f}".format(account_value))
    label_abr_av.grid(column=1, row=2, sticky=(W), pady=5, padx=5) 

    tkroot.label_abr_pbbd = Label(tkroot.accountBalanceRobinhood, text="Prospective Buy Balance: ")
    tkroot.label_abr_pbbd.grid(column=1, row=3, sticky=(W), pady=5, padx=5) 

    label_abr_spaa = Label(tkroot.accountBalanceRobinhood, text="Stock Purchasing Allocation Availability:")
    label_abr_spaa.grid(column=1, row=4, sticky=(W), pady=5, padx=5) 

    tkroot.label_abr_spaav = Message(tkroot.accountBalanceRobinhood, text="Loading...", width=350)
    tkroot.label_abr_spaav.grid(column=1, row=5, sticky=(W), pady=5, padx=5, columnspan=2) 