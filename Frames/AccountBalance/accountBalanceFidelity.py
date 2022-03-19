from tkinter import ttk
from tkinter import *
from SetDefaultData.Common import Common

def accountBalanceFidelity(tkroot):
    tkroot.accountBalanceFidelity = ttk.Frame(tkroot, padding="12 12 12 12")
    tkroot.accountBalanceFidelity.place(relx=.425, rely=-.01, anchor=N)

    label_f_head = Label(tkroot.accountBalanceFidelity, text="Fidelity Account Balance", font=("*Font", 16))
    label_f_head.grid(column=1, row=0, sticky=(W), pady=10, columnspan=2)

    purchasing_power = Common.purchasingPower('fidelity_account')
    label_f_pp = Label(tkroot.accountBalanceFidelity, text="Purchasing Power: ${:,.2f}".format(purchasing_power))
    label_f_pp.grid(column=1, row=1, sticky=(W), pady=5, padx=5) 

    account_value = Common.accountBalance('fidelity_account')
    label_f_av = Label(tkroot.accountBalanceFidelity, text="Account Value: ${:,.2f}".format(account_value))
    label_f_av.grid(column=1, row=2, sticky=(W), pady=5, padx=5) 

    tkroot.label_abf_pbb = Label(tkroot.accountBalanceFidelity, text="Prospective Buy Balance: ")
    tkroot.label_abf_pbb.grid(column=1, row=3, sticky=(W), pady=5, padx=5) 

    label_f_spaa = Label(tkroot.accountBalanceFidelity, text="Stock Purchasing Allocation Availability:")
    label_f_spaa.grid(column=1, row=4, sticky=(W), pady=5, padx=5) 

    tkroot.label_abf_spaav = Message(tkroot.accountBalanceFidelity, text="Loading...", width=350)
    tkroot.label_abf_spaav.grid(column=1, row=5, sticky=(W), pady=5, padx=5) 