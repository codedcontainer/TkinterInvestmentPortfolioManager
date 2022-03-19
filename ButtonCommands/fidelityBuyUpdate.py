import sqlite3
from Common.Helper import Helper
import datetime
import Menu.MenuCommands as MenuCommands
from Database.CommonSqliteActions import CommonSqliteActions
 
async def fidelityBuyUpdate(input_rb, tkroot):
    tickers = input_rb.get("1.0",'end-1c')
    tickers = Helper.sanitizeList(tickers)
    sql = CommonSqliteActions()
    
    try:
        sql.cursor.execute("DELETE FROM fidelity_buy")
        for ticker in tickers:
            if(ticker != ""):
                sql.cursor.execute("INSERT INTO fidelity_buy VALUES(\"{}\", \"{}\")"
                .format(datetime.datetime.now(),ticker))

        sql.closeDb()

        await MenuCommands.MenuCommands.showFidelityBuyFrame(tkroot, "Table Updated")

    except sqlite3.Error as error:
        await MenuCommands.MenuCommands.showFidelityBuyFrame(tkroot, "Database Error: " + str(error.args))