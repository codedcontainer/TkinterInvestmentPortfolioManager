
# Python Tkinter Investment Account Portfolio Management Desktop Application 

## About
A simple financial portfolio GUI for managing a Robinhood and Fidelity account using Python 3 [Tkinter](https://docs.python.org/3/library/tkinter.html). Uses [Sqlite3](https://sqlite.org/index.html) and asynchronous programming to display and set account performances, watch lists, and balances. Will run on either Windows, Linux, or Mac OS with Python 3 and associated modules installed via PIP3

## To Run
- install [Python 3](https://www.python.org/downloads/) and PIP3 modules listed below 
- open terminal or command prompt and enter `python3 index.py`

## PIP3 Module Installation Requirments
- [async_tkinter_loop](https://pypi.org/project/async-tkinter-loop/)
- [yahoo_finance_async](https://pypi.org/project/yahoo_finance_async/)
    - App will break if module loses support from Yahoo Finance
- [pandas](https://pypi.org/project/pandas/)

## Other resources
### PyInstaller
If using multiple operating systems, skip this section
1. Convert app title icon to a base64 byte array or else app will not be able to run properly
2. `pyinstaller -w --add-data "Database\investment_accounts.db;.\Database" --onefile index.py`

## Placing a URL image from a request in a frame
```req = urllib.request.Request("https://stockcharts.com/c-sc/sc?s=AAPL&p=W&b=5&g=0&i=t2656791252c&r=1645919909673",headers={'User-Agent': 'Mozilla/5.0'} )
    raw_data = urllib.request.urlopen(req).read()
    im = Image.open(io.BytesIO(raw_data)).resize((500,500))
    image = ImageTk.PhotoImage(im, size="200x200")
    label1 = Label(mainframe, image=image)
    label1.grid(column=1, row=1, sticky=(W,E,S,N))
```
