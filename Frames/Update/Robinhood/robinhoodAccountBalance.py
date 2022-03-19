from tkinter import ttk
from tkinter import *
from ButtonCommands.robinhoodBalanceUpdate import robinhoodBalanceUpdate
from SetDefaultData.Common import Common
from Common.Helper import *

def robinhoodAccountBalance(tkroot):
    tkroot.robinhoodAccountBalance = ttk.Frame(tkroot, padding="12 12 12 12")
    tkroot.robinhoodAccountBalance.place(relx=.52, rely=-.01, anchor=N)
    tkroot.columnconfigure(0, weight=1)
    tkroot.rowconfigure(0, weight=1)

    label_rab_head = Label(tkroot.robinhoodAccountBalance, text="Robinhood Account Balance", font=("*Font", 16))
    label_rab_head.grid(column=1, row=0, sticky=(W), pady=10, columnspan=2)

    label_rab_pb = Label(tkroot.robinhoodAccountBalance, text="Purchasing Balance:")
    label_rab_pb.grid(column=1, row=1, sticky=(W), pady=5, padx=5)    

    input_rab_pbt = Text(tkroot.robinhoodAccountBalance, width=22, height=1)
    input_rab_pbt.grid(column=1, row=2, sticky=(W), padx=5)
    input_rab_pbt.bind("<Tab>", Helper.focus_next_widget)
    input_rab_pbt.bind("<Control-a>", Helper.select_all)

    label_rab_tb = Label(tkroot.robinhoodAccountBalance, text="Total Account Balance:")
    label_rab_tb.grid(column=2, row=1, sticky=(W), pady=5, padx=5)

    input_rab_tbt = Text(tkroot.robinhoodAccountBalance, width=22, height=1)
    input_rab_tbt.grid(column=2, row=2, sticky=(W), padx=5)
    input_rab_tbt.bind("<Tab>", Helper.focus_next_widget)
    input_rab_tbt.bind("<Control-a>", Helper.select_all)

    tkroot.rab_label_response = Label(tkroot.robinhoodAccountBalance, text="")
    tkroot.rab_label_response.grid(column=1, row=4, sticky=(W,E), columnspan=2)

    label_rab_update = Label(tkroot.robinhoodAccountBalance)
    last_update_date = Common.lastUpdated('robinhood_account')
    label_rab_update.config(text="Last updated: " + last_update_date)
    label_rab_update.grid(column=1, row=3, sticky=(W), pady=20)

    input_text_vals = {
        "purchasingBalance": input_rab_pbt, 
        "totalAccountBalance": input_rab_tbt
    }

    button_rab = Button(tkroot.robinhoodAccountBalance, text="Update", command=lambda: robinhoodBalanceUpdate(input_text_vals, tkroot))
    button_rab.grid(column=2,row=3, sticky=(S,E), pady=5)

    spacer_label = Label(tkroot.robinhoodAccountBalance, text="")
    spacer_label.grid(column = 1, row=6, columnspan=2, pady=55)




