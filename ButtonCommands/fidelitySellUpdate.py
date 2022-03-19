import sqlite3
from Common.Helper import Helper
from Database.CommonSqliteActions import CommonSqliteActions
import datetime

def fidelitySellUpdate(input_rb, label_response):
    tickers = input_rb.get("1.0",'end-1c')
    tickers = Helper.sanitizeList(tickers)
    sql = CommonSqliteActions()
    
    try:
        sql.cursor.execute("DELETE FROM fidelity_sell")
        for ticker in tickers:
            if(ticker != ""):
                sql.cursor.execute("INSERT INTO fidelity_sell VALUES(\"{}\", \"{}\")"
                .format(datetime.datetime.now(),ticker))

        sql.closeDb()

        label_response.config(text = "Table updated")
    except sqlite3.Error as error:
        label_response.config(text = "Database Error: " + str(error.args))