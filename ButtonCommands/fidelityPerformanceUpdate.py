import sqlite3
import datetime
import Menu.MenuCommands as MenuCommands
from Database.CommonSqliteActions import CommonSqliteActions

def fidelityPerformanceUpdate(text_inputs, tkroot):
    _text_inputs = text_inputs.copy()
    for prop in _text_inputs:
        try:
            input_text = _text_inputs[prop].get("1.0", "end-1c").strip()
            _text_inputs[prop] = float(input_text)
        except ValueError:
            _text_inputs[prop] = "NULL"
        
    sql = CommonSqliteActions()

    try:

        sql.cursor.execute("INSERT INTO fidelity_performance VALUES(\"{}\", {}, {}, {}, {}, {}, {})".format(datetime.datetime.now(), _text_inputs["one_day_percent_return"],_text_inputs["year_to_date_percent_return"], _text_inputs["one_year_percent_return"], _text_inputs["three_year_percent_return"],_text_inputs["five_year_percent_return"], _text_inputs["ten_year_percent_return"] ))
        
        sql.closeDb()

        MenuCommands.MenuCommands.showFidelityPerformanceFrame(tkroot, "Table Updated") 

    except sqlite3.Error as error:        
        MenuCommands.MenuCommands.showFidelityPerformanceFrame(tkroot, error) 