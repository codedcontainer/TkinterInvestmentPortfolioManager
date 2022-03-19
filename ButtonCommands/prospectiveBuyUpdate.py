import sqlite3
from Common.Helper import Helper
from Database.CommonSqliteActions import CommonSqliteActions
import datetime
import Menu.MenuCommands as MenuCommands

async def prospectiveBuyUpdate(input_rb,tkroot):
    tickers = input_rb.get("1.0",'end-1c')
    tickers = Helper.sanitizeList(tickers)
    sql = CommonSqliteActions()
    
    try:
        sql.cursor.execute("DELETE FROM prospective_buy")
        for ticker in tickers:
            if(ticker != ""):
                sql.cursor.execute("INSERT INTO prospective_buy VALUES(\"{}\", \"{}\")"
                .format(datetime.datetime.now(),ticker))

        sql.closeDb()
        await MenuCommands.MenuCommands.showProspectiveBuyFrame(tkroot, "Table Updated") 

    except sqlite3.Error as error:
        await MenuCommands.MenuCommands.showProspectiveBuyFrame(tkroot,  "Database Error: " + str(error.args))