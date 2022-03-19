class FinvizScreenerLink():
    @staticmethod
    def generateLink(ticker_list):
        ticker_list = ",".join(str(x) for x in ticker_list)
        link = "https://www.finviz.com/screener.ashx?t={}".format(ticker_list)
        return link       