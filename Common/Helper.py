import datetime
import webbrowser

class Helper:
    @staticmethod
    def sanitizeList(stock_tickers_array):
        stock_tickers_array = Helper.splitTickers(stock_tickers_array)
        return Helper.removeDuplicates(stock_tickers_array)      

    @staticmethod
    def splitTickers(stock_tickers_array):
        return stock_tickers_array.replace(" ", "").split(',')
        
    @staticmethod
    def removeDuplicates(stock_tickers_array):
        return list(dict.fromkeys(stock_tickers_array))

    @staticmethod
    def dateTimeFormat(dateTimeString):
        date_time_obj = datetime.datetime.strptime(dateTimeString, "%Y-%m-%d %H:%M:%S.%f")
        return date_time_obj.strftime("%m/%d/%Y %I:%M %p")

    @staticmethod
    def focus_next_widget(event):
        event.widget.tk_focusNext().focus()
        return("break")

    @staticmethod
    def select_all(event):
        event.widget.tag_add('sel', '1.0', 'end')
        return "break"

    @staticmethod
    def openUrl(url):
        webbrowser.open_new_tab(url)

    @staticmethod
    def sortAscending(stock_tickers_array):
        return sorted(stock_tickers_array)