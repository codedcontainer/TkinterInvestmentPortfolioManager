from tkinter import ttk, tk
from tkinter import *
from ButtonCommands.prospectiveBuyUpdate import prospectiveBuyUpdate
from SetDefaultData.Common import Common
from async_tkinter_loop import async_command
from Common.Helper import *

def prospectiveBuy(tkroot):
    tkroot.prospectiveBuy = ttk.Frame(tkroot, padding="12 12 12 12")
    tkroot.prospectiveBuy.place(relx=.51, rely=0, anchor=N)
    tkroot.columnconfigure(0, weight=1)
    tkroot.rowconfigure(0, weight=1)

    label_pb_head = Label(tkroot.prospectiveBuy, text="Prospective Buy List", font=("*Font", 16))
    label_pb_head.grid(column=1, row =0, sticky=(W), pady=5)

    label_pb = Label(tkroot.prospectiveBuy, text="Comma seperated list of stocks interested in buying:")
    label_pb.grid(column=1, row=1, sticky=(W), pady=5)

    input_pb = Text(tkroot.prospectiveBuy, width=45, height=10)
    tkroot.default_prospective_buy_list = Common.tickers('prospective_buy', index=1)
    input_pb.insert(tk.END, tkroot.default_prospective_buy_list)
    input_pb.grid(column=1, row=2, sticky=(W, E, N, S)) 
    input_pb.bind("<Tab>", Helper.focus_next_widget)
    input_pb.bind("<Control-a>", Helper.select_all)

    tkroot.label_pb_total = Label(tkroot.prospectiveBuy, text="Current Price Total: Loading...")
    tkroot.label_pb_total.grid(column=1, row=3, sticky=(E), pady=5)

    label_pb_update = Label(tkroot.prospectiveBuy)
    last_update_date = Common.lastUpdated('prospective_buy')
    label_pb_update.config(text="Last updated: " + last_update_date)
    label_pb_update.grid(column=1, row=4, sticky=(W))

    tkroot.pb_label_response = Label(tkroot.prospectiveBuy, text="")
    tkroot.pb_label_response.grid(column=1, row=6, sticky=(W,E))

    button_pb = Button(tkroot.prospectiveBuy, text="Update", command= async_command(prospectiveBuyUpdate, input_pb, tkroot))
    button_pb.grid(column=1,row=4, sticky=(S,E), pady=5)