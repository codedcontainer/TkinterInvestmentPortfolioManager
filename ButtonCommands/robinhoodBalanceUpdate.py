import sqlite3
import datetime
import Menu.MenuCommands as MenuCommands
from Database.CommonSqliteActions import CommonSqliteActions
import sqlite3

import Menu.MenuCommands as MenuCommands
from Database.CommonSqliteActions import CommonSqliteActions


def robinhoodBalanceUpdate(text_inputs,tkroot):
    _text_inputs = text_inputs.copy()
    for prop in _text_inputs:
        try:
            input_text = _text_inputs[prop].get("1.0", "end-1c").strip()
            _text_inputs[prop] = float(input_text)
        except ValueError:
            _text_inputs[prop] = "NULL"

    sql = CommonSqliteActions()
    
    try:
        sql.cursor.execute("INSERT INTO robinhood_account VALUES(\"{}\",{},{})".format(datetime.datetime.now(), _text_inputs["purchasingBalance"], _text_inputs["totalAccountBalance"]))
        sql.closeDb()
        MenuCommands.MenuCommands.showRobinhoodAccountBalanceFrame(tkroot, "Table Updated") 

    except sqlite3.Error as error:
        MenuCommands.MenuCommands.showRobinhoodAccountBalanceFrame(tkroot,  "Database Error: " + str(error.args))