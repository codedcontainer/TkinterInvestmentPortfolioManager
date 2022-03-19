from tkinter import ttk
from tkinter import *
from SetDefaultData.Common import Common

def performanceRobinhood(tkroot):
    tkroot.performanceRobinhood = ttk.Frame(tkroot, padding="12 12 12 12")
    tkroot.performanceRobinhood.place(relx=.382, rely=-.01, anchor=N)
    tkroot.columnconfigure(0, weight=1)
    tkroot.rowconfigure(0, weight=1)

    label_rb_head = Label(tkroot.performanceRobinhood, text="Robinhood Performance", font=("*Font", 16))
    label_rb_head.grid(column=1, row=0, sticky=(W), pady=10, columnspan=2)

    metrics = Common.metrics('robinhood_performance')

    label_rb_odd = Label(tkroot.performanceRobinhood, text="One day return: ${:,.2f}".format(metrics["one_day_dollar"]))
    label_rb_odd.grid(column=1, row=1, stick=(W), pady=5, columnspan=2)

    label_rb_owd = Label(tkroot.performanceRobinhood, text="One week return: ${:,.2f}".format(metrics["one_week_dollar"]))
    label_rb_owd.grid(column=1, row=2, stick=(W), pady=5, columnspan=2)

    label_rb_omd = Label(tkroot.performanceRobinhood, text="One month return: ${:,.2f}".format(metrics["one_month_dollar"]))
    label_rb_omd.grid(column=1, row=3, stick=(W), pady=5, columnspan=2)

    label_rb_tmd = Label(tkroot.performanceRobinhood, text="Three month return: ${:,.2f}".format(metrics["three_month_dollar"]))
    label_rb_tmd.grid(column=1, row=4, stick=(W), pady=5, columnspan=2)

    label_rb_oyd = Label(tkroot.performanceRobinhood, text="One year return: ${:,.2f}".format(metrics["one_year_dollar"]))
    label_rb_oyd.grid(column=1, row=5, stick=(W), pady=5, columnspan=2)

    label_rb_atd = Label(tkroot.performanceRobinhood, text="All time return: ${:,.2f}".format(metrics["all_time_dollar"]))
    label_rb_atd.grid(column=1, row=6, stick=(W), pady=5, columnspan=2)

    label_rb_atp = Label(tkroot.performanceRobinhood, text="All time percentage return: {}%".format(metrics["all_time_percentage"]))
    label_rb_atp.grid(column=1, row=7, stick=(W), pady=5, columnspan=2)