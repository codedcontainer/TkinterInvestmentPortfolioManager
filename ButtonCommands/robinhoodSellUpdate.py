import sqlite3
from Common.Helper import Helper
from Database.CommonSqliteActions import CommonSqliteActions
import datetime
import Menu.MenuCommands as MenuCommands


def robinhoodSellUpdate(input_rb, tkroot):
    tickers = input_rb.get("1.0",'end-1c')
    tickers = Helper.sanitizeList(tickers)
    sql = CommonSqliteActions()
    
    try:
        sql.cursor.execute("DELETE FROM robinhood_sell")
        for ticker in tickers:
            if(ticker != ""):
                sql.cursor.execute("INSERT INTO robinhood_sell VALUES(\"{}\", \"{}\")"
                .format(datetime.datetime.now(),ticker))

        sql.closeDb()

        MenuCommands.MenuCommands.showRobinhoodSellFrame(tkroot, "Table Updated")
    except sqlite3.Error as error:
        MenuCommands.MenuCommands.showRobinhoodBuyFrame(tkroot,  "Database Error: " + str(error.args))