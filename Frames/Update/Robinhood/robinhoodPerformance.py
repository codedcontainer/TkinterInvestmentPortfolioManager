from tkinter import ttk
from tkinter import *
from ButtonCommands.robinhoodPerformanceUdpate import robinhoodPerformanceUdpate
from SetDefaultData.Common import Common
from Common.Helper import *


def robinhoodPerformance(tkroot):
    tkroot.robinhoodPerformance = ttk.Frame(tkroot, padding="12 12 12 12")
    tkroot.robinhoodPerformance.place(relx=.52, rely=-.01, anchor=N)
    tkroot.columnconfigure(0, weight=1)
    tkroot.rowconfigure(0, weight=1)

    label_rb_head = Label(tkroot.robinhoodPerformance, text="Robinhood Performance", font=("*Font", 16))
    label_rb_head.grid(column=1, row=0, sticky=(W), pady=10, columnspan=2)

    label_rb_oddr = Label(tkroot.robinhoodPerformance, text="One day dollar return:")
    label_rb_oddr.grid(column=1, row=1, sticky=(W), pady=5, padx=5)    

    input_rb_oddrt = Text(tkroot.robinhoodPerformance, width=22, height=1)
    input_rb_oddrt.grid(column=1, row=2, sticky=(W), padx=5)
    input_rb_oddrt.bind("<Tab>", Helper.focus_next_widget)
    input_rb_oddrt.bind("<Control-a>", Helper.select_all)

    label_rb_owdr = Label(tkroot.robinhoodPerformance, text="One week dollar return:")
    label_rb_owdr.grid(column=2, row=1, sticky=(W), pady=5, padx=5)

    input_rb_owdrt = Text(tkroot.robinhoodPerformance, width=22, height=1)
    input_rb_owdrt.grid(column=2, row=2, sticky=(W), padx=5)
    input_rb_owdrt.bind("<Tab>", Helper.focus_next_widget)
    input_rb_owdrt.bind("<Control-a>", Helper.select_all)

    label_rb_omdr = Label(tkroot.robinhoodPerformance, text="One month dollar return:")
    label_rb_omdr.grid(column=1, row=3, sticky=(W), pady=5, padx=5)

    input_rb_omdrt = Text(tkroot.robinhoodPerformance, width=22, height=1)
    input_rb_omdrt.grid(column=1, row=4, sticky=(W), padx=5)
    input_rb_omdrt.bind("<Tab>", Helper.focus_next_widget)
    input_rb_omdrt.bind("<Control-a>", Helper.select_all)

    label_rb_tmdr = Label(tkroot.robinhoodPerformance, text="Three month dollar return:")
    label_rb_tmdr.grid(column=2, row=3, sticky=(W), pady=5, padx=5)

    input_rb_tmdrt = Text(tkroot.robinhoodPerformance, width=22, height=1)
    input_rb_tmdrt.grid(column=2, row=4, sticky=(W), padx=5)
    input_rb_tmdrt.bind("<Tab>", Helper.focus_next_widget)
    input_rb_tmdrt.bind("<Control-a>", Helper.select_all)

    label_rb_oydr = Label(tkroot.robinhoodPerformance, text="One year dollar return:")
    label_rb_oydr.grid(column=1, row=5, sticky=(W), pady=5, padx=5)

    input_rb_oydrt = Text(tkroot.robinhoodPerformance, width=22, height=1)
    input_rb_oydrt.grid(column=1, row=6, sticky=(W), padx=5)
    input_rb_oydrt.bind("<Tab>", Helper.focus_next_widget)
    input_rb_oydrt.bind("<Control-a>", Helper.select_all)

    label_rb_atdr = Label(tkroot.robinhoodPerformance, text="All time dollar return:")
    label_rb_atdr.grid(column=2, row=5, sticky=(W), pady=5, padx=5)

    input_rb_atdrt = Text(tkroot.robinhoodPerformance, width=22, height=1)
    input_rb_atdrt.grid(column=2, row=6, sticky=(W), padx=5)
    input_rb_atdrt.bind("<Tab>", Helper.focus_next_widget)
    input_rb_atdrt.bind("<Control-a>", Helper.select_all)

    label_rb_atpr = Label(tkroot.robinhoodPerformance, text="All time percentage return:")
    label_rb_atpr.grid(column=1, row=7, sticky=(W), pady=5, padx=5)

    input_rb_atprt = Text(tkroot.robinhoodPerformance, width=22, height=1)
    input_rb_atprt.grid(column=1, row=8, sticky=(W), padx=5)
    input_rb_atprt.bind("<Tab>", Helper.focus_next_widget)
    input_rb_atprt.bind("<Control-a>", Helper.select_all)

    tkroot.rbp_label_response = Label(tkroot.robinhoodPerformance, text="")
    tkroot.rbp_label_response.grid(column=1, row=11, sticky=(W,E), columnspan=2)

    label_rb_update = Label(tkroot.robinhoodPerformance)
    last_update_date = Common.lastUpdated('robinhood_performance')
    label_rb_update.config(text="Last updated: " + last_update_date)
    label_rb_update.grid(column=1, row=10, sticky=(W), pady=20)

    text_inputs = {
        "one_day_dollar_return": input_rb_oddrt,
        "one_week_dollar_return": input_rb_owdrt, 
        "one_month_dollar_return": input_rb_omdrt, 
        "three_month_dollar_return": input_rb_tmdrt, 
        "one_year_dollar_return": input_rb_oydrt, 
        "all_time_dollar_return": input_rb_atdrt,
        "all_time_percentage_return": input_rb_atprt
    }

    button_rb = Button(tkroot.robinhoodPerformance, text="Update", command=lambda: robinhoodPerformanceUdpate(text_inputs, tkroot))
    button_rb.grid(column=2,row=10, sticky=(S,E), pady=5)



