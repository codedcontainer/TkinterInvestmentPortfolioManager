from tkinter import ttk
from tkinter import *
from SetDefaultData.Common import Common

def performanceFidelity(tkroot):
    tkroot.performanceFidelity = ttk.Frame(tkroot, padding="12 12 12 12")
    tkroot.performanceFidelity.place(relx=.398, rely=-.01, anchor=N)
    tkroot.columnconfigure(0, weight=1)
    tkroot.rowconfigure(0, weight=1)

    label_pfr_head = Label(tkroot.performanceFidelity, text="Fidelity Performance", font=("*Font", 16))
    label_pfr_head.grid(column=1, row=0, sticky=(W), pady=10, columnspan=2)

    metrics = Common.metrics('fidelity_performance')

    label_pfr_odpr = Label(tkroot.performanceFidelity, text="One day percent return: ${:,.2f}".format(metrics["percent_one_day"]))
    label_pfr_odpr.grid(column=1, row=1, stick=(W), pady=5, columnspan=2)

    label_pfr_ytdpr = Label(tkroot.performanceFidelity, text="YTD percent return: ${:,.2f}".format(metrics["percent_ytd"]))
    label_pfr_ytdpr.grid(column=1, row=2, stick=(W), pady=5, columnspan=2)

    label_pfr_oypr = Label(tkroot.performanceFidelity, text="One year percent return: ${:,.2f}".format(metrics["percent_one_year"]))
    label_pfr_oypr.grid(column=1, row=3, stick=(W), pady=5, columnspan=2)

    label_pfr_typr = Label(tkroot.performanceFidelity, text="Three year percent return: ${:,.2f}".format(metrics["percent_three_year"]))
    label_pfr_typr.grid(column=1, row=4, stick=(W), pady=5, columnspan=2)

    label_pfr_fypr = Label(tkroot.performanceFidelity, text="Five year percent return: ${:,.2f}".format(metrics["percent_five_year"]))
    label_pfr_fypr.grid(column=1, row=5, stick=(W), pady=5, columnspan=2)

    label_pfr_tenypr = Label(tkroot.performanceFidelity, text="Ten year percent return: ${:,.2f}".format(metrics["percent_ten_year"]))
    label_pfr_tenypr.grid(column=1, row=6, stick=(W), pady=5, columnspan=2)