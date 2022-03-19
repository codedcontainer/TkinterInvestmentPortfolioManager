import sqlite3
import datetime
import Menu.MenuCommands as MenuCommands
from Database.CommonSqliteActions import CommonSqliteActions

def robinhoodPerformanceUdpate(text_inputs, tkroot):
    _text_inputs = text_inputs.copy()
    for prop in _text_inputs:
        try:
            input_text = _text_inputs[prop].get("1.0", "end-1c").strip()
            _text_inputs[prop] = float(input_text)
        except ValueError:
            _text_inputs[prop] = "NULL"
        
    sql = CommonSqliteActions()

    try:
        sql.cursor.execute("INSERT INTO robinhood_performance VALUES(\"{}\", {}, {}, {}, {}, {}, {}, {})".format(datetime.datetime.now(), _text_inputs["one_day_dollar_return"], _text_inputs["one_week_dollar_return"], _text_inputs[ "one_month_dollar_return"], _text_inputs[ "three_month_dollar_return"],_text_inputs["one_year_dollar_return"],_text_inputs["all_time_dollar_return"],_text_inputs["all_time_percentage_return"]))

        sql.closeDb()

        MenuCommands.MenuCommands.showRobinhoodPerformanceFrame(tkroot, "Table Updated") 

    except sqlite3.Error as error:        
        MenuCommands.MenuCommands.showRobinhoodPerformanceFrame(tkroot, error) 