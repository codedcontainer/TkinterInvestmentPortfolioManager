
# Python Tkinter Investment Account Portfolio Management Desktop Application 

## About
A simple financial portfolio GUI for managing a Robinhood and Fidelity account using Python's Tkinter module. Uses Sq3lite and asynchronous programming to display and set account performances, watch lists, and balances. Will run in either Windows, Linux, or Mac OS with Python and associated modules installed via PIP.

## To Run
- install Python3 and PIP packages listed below 
- open terminal or command prompt and enter `python index.py` or `python3 index.py`

## PIP Installations
- async_tkinter_loop
- yahoo_finance_async

## Other resources

### PyInstaller
`pyinstaller -w --add-data "Database\investment_accounts.db;.\Database" --onefile index.py`

## Placing a URL image from a request in a frame
```req = urllib.request.Request("https://stockcharts.com/c-sc/sc?s=AAPL&p=W&b=5&g=0&i=t2656791252c&r=1645919909673",headers={'User-Agent': 'Mozilla/5.0'} )
    raw_data = urllib.request.urlopen(req).read()
    im = Image.open(io.BytesIO(raw_data)).resize((500,500))
    image = ImageTk.PhotoImage(im, size="200x200")
    label1 = Label(mainframe, image=image)
    label1.grid(column=1, row=1, sticky=(W,E,S,N))
```
