from tkinter import ttk
from tkinter import *
from SetDefaultData.AllBalanceDefaultData import AllBalanceDefaultData

def accountBalanceAll(tkroot):
    tkroot.accountBalanceAll = ttk.Frame(tkroot, padding="12 12 12 12")
    tkroot.accountBalanceAll.place(relx=.394, rely=-.011, anchor=N)

    label_aba_head = Label(tkroot.accountBalanceAll, text="All Account Balance Totals", font=("*Font", 16))
    label_aba_head.grid(column=1, row=0, sticky=(W), pady=10, columnspan=2)

    purchasing_power = AllBalanceDefaultData.purchasingPower()
    label_aba_pp = Label(tkroot.accountBalanceAll, text="Purchasing Power: ${:,.2f}".format(purchasing_power))
    label_aba_pp.grid(column=1, row=1, sticky=(W), pady=5, padx=5) 

    account_value = AllBalanceDefaultData.accountBalance()
    label_aba_av = Label(tkroot.accountBalanceAll, text="Account Value: ${:,.2f}".format(account_value))
    label_aba_av.grid(column=1, row=2, sticky=(W), pady=5, padx=5) 
