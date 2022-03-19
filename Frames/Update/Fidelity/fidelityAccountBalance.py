from tkinter import ttk
from tkinter import *
from ButtonCommands.fidelityBalanceUpdate import fidelityBalanceUpdate
from SetDefaultData.Common import Common
from Common.Helper import *

def fidelityAccountBalance(tkroot):
    tkroot.fidelityAccountBalance = ttk.Frame(tkroot, padding="12 12 12 12")
    tkroot.fidelityAccountBalance.place(relx=.52, rely=-.01, anchor=N)
    tkroot.columnconfigure(0, weight=1)
    tkroot.rowconfigure(0, weight=1)

    label_fb_head = Label(tkroot.fidelityAccountBalance, text="Fidelity Account Balance", font=("*Font", 16))
    label_fb_head.grid(column=1, row=0, sticky=(W), pady=10, columnspan=2)

    label_fb_pb = Label(tkroot.fidelityAccountBalance, text="Purchasing Balance:")
    label_fb_pb.grid(column=1, row=1, sticky=(W), pady=5, padx=5)    

    input_fb_pbt = Text(tkroot.fidelityAccountBalance, width=22, height=1)
    input_fb_pbt.grid(column=1, row=2, sticky=(W), padx=5)
    input_fb_pbt.bind("<Tab>", Helper.focus_next_widget)
    input_fb_pbt.bind("<Control-a>", Helper.select_all)

    label_fb_tb = Label(tkroot.fidelityAccountBalance, text="Total Account Balance:")
    label_fb_tb.grid(column=2, row=1, sticky=(W), pady=5, padx=5)

    input_fb_tbt = Text(tkroot.fidelityAccountBalance, width=22, height=1)
    input_fb_tbt.grid(column=2, row=2, sticky=(W), padx=5)
    input_fb_tbt.bind("<Tab>", Helper.focus_next_widget)
    input_fb_tbt.bind("<Control-a>", Helper.select_all)

    tkroot.fab_label_response = Label(tkroot.fidelityAccountBalance, text="")
    tkroot.fab_label_response.grid(column=1, row=4, sticky=(W,E), columnspan=2)

    label_fb_update = Label(tkroot.fidelityAccountBalance)
    last_update_date = Common.lastUpdated('fidelity_account')
    label_fb_update.config(text="Last updated: " + last_update_date)
    label_fb_update.grid(column=1, row=3, sticky=(W), pady=20)

    input_text_vals = {
        "purchasingBalance": input_fb_pbt, 
        "totalAccountBalance": input_fb_tbt
    }

    button_fb = Button(tkroot.fidelityAccountBalance, text="Update", command=lambda: fidelityBalanceUpdate(input_text_vals, tkroot))
    button_fb.grid(column=2,row=3, sticky=(S,E), pady=5)