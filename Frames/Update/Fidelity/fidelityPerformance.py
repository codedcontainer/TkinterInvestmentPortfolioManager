from tkinter import ttk
from tkinter import *
from ButtonCommands.fidelityPerformanceUpdate import fidelityPerformanceUpdate
from SetDefaultData.Common import Common
from Common.Helper import *

def fidelityPerformance(tkroot):
   tkroot.fidelityPerformance = ttk.Frame(tkroot, padding="12 12 12 12")
   tkroot.fidelityPerformance.place(relx=.52, rely=-.01, anchor=N)
   tkroot.columnconfigure(0, weight=1)
   tkroot.rowconfigure(0, weight=1)

   label_f_head = Label(tkroot.fidelityPerformance, text="Fidelity Performance", font=("*Font", 16))
   label_f_head.grid(column=1, row=0, sticky=(W), pady=10, columnspan=2)

   label_f_odpr = Label(tkroot.fidelityPerformance, text="One day percent return:")
   label_f_odpr.grid(column=1, row=1, sticky=(W), pady=5, padx=5)    

   input_f_odprt = Text(tkroot.fidelityPerformance, width=22, height=1)
   input_f_odprt.grid(column=1, row=2, sticky=(W), padx=5)
   input_f_odprt.bind("<Tab>", Helper.focus_next_widget)
   input_f_odprt.bind("<Control-a>", Helper.select_all)

   label_f_ytdpr = Label(tkroot.fidelityPerformance, text="ytd percent return:")
   label_f_ytdpr.grid(column=2, row=1, sticky=(W), pady=5, padx=5)

   input_f_ytdprt = Text(tkroot.fidelityPerformance, width=22, height=1)
   input_f_ytdprt.grid(column=2, row=2, sticky=(W), padx=5)
   input_f_ytdprt.bind("<Tab>", Helper.focus_next_widget)
   input_f_ytdprt.bind("<Control-a>", Helper.select_all)

   label_f_oypr = Label(tkroot.fidelityPerformance, text="one year percent return:")
   label_f_oypr.grid(column=1, row=3, sticky=(W), pady=5, padx=5)

   input_f_oyprt = Text(tkroot.fidelityPerformance, width=22, height=1)
   input_f_oyprt.grid(column=1, row=4, sticky=(W), padx=5)
   input_f_oyprt.bind("<Tab>", Helper.focus_next_widget)
   input_f_oyprt.bind("<Control-a>", Helper.select_all)

   label_f_typr = Label(tkroot.fidelityPerformance, text="three year percent return:")
   label_f_typr.grid(column=2, row=3, sticky=(W), pady=5, padx=5)

   input_f_typrt = Text(tkroot.fidelityPerformance, width=22, height=1)
   input_f_typrt.grid(column=2, row=4, sticky=(W), padx=5)
   input_f_typrt.bind("<Tab>", Helper.focus_next_widget)
   input_f_typrt.bind("<Control-a>", Helper.select_all)


   label_f_fypr = Label(tkroot.fidelityPerformance, text="five year percent return:")
   label_f_fypr.grid(column=1, row=5, sticky=(W), pady=5, padx=5)

   input_f_fyprt = Text(tkroot.fidelityPerformance, width=22, height=1)
   input_f_fyprt.grid(column=1, row=6, sticky=(W), padx=5)
   input_f_fyprt.bind("<Tab>", Helper.focus_next_widget)
   input_f_fyprt.bind("<Control-a>", Helper.select_all)

   label_f_typr = Label(tkroot.fidelityPerformance, text="ten year percent return:")
   label_f_typr.grid(column=2, row=5, sticky=(W), pady=5, padx=5)

   input_f_typrt = Text(tkroot.fidelityPerformance, width=22, height=1)
   input_f_typrt.grid(column=2, row=6, sticky=(W), padx=5)
   input_f_typrt.bind("<Tab>", Helper.focus_next_widget)
   input_f_typrt.bind("<Control-a>", Helper.select_all)

   tkroot.fp_label_response = Label(tkroot.fidelityPerformance, text="")
   tkroot.fp_label_response.grid(column=1, row=11, sticky=(W,E), columnspan=2)

   label_f_update = Label(tkroot.fidelityPerformance)
   last_update_date = Common.lastUpdated('fidelity_performance')
   label_f_update.config(text="Last updated: " + last_update_date)
   label_f_update.grid(column=1, row=10, sticky=(W), pady=30)

   text_inputs = {
      "one_day_percent_return": input_f_odprt, 
      "year_to_date_percent_return": input_f_ytdprt,
      "one_year_percent_return": input_f_oyprt,
      "three_year_percent_return": input_f_typrt,
      "five_year_percent_return": input_f_fyprt,
      "ten_year_percent_return": input_f_typrt
   }

   button_f = Button(tkroot.fidelityPerformance, text="Update", command=lambda: fidelityPerformanceUpdate(text_inputs, tkroot))
   button_f.grid(column=2,row=10, sticky=(S,E), pady=5)



