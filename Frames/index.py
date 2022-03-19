from tkinter import ttk
from tkinter import *


help_text = """
1. Export Robinhood holdings with Google Chrome Extention
     a. RobinHood Portfolio Export CSV/Excel(Updated)

2. Export Fidelity holdings (positions > download )

3. Import exported CSV files
     a. Make sure to save as plain CSV if encoding error

4. Update each accounts performance & balances

5. Add prospective buy list stocks

6. Open stock holdings for each account and update buy/sell lists

7. Update buy list using prospective buy list
"""

def index(tkroot):
    tkroot.index = ttk.Frame(tkroot, padding="12 12 12 12")
    tkroot.index.place(relx=.5, rely=0, anchor=N)
    tkroot.columnconfigure(0, weight=1)
    tkroot.rowconfigure(0, weight=1)

    label_index_head = Label(tkroot.index, text="Getting Started", font=("*Font", 16))
    label_index_head.grid(column=0, row=0, sticky=(W), pady=5, columnspan=3)

    label_mf = Message(tkroot.index, text=help_text, width=500)
    label_mf.grid(column=0, columnspan=3, row=1, sticky=(W,E))