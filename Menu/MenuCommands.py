from tkinter import filedialog, ttk
from ButtonCommands.robinhoodHoldingsImport import robinhoodHoldingsImport
from ButtonCommands.fidelityHoldingsImport import fidelityHoldingsImport
from Common.Helper import Helper
from Frames.AccountBalance.accountBalanceFidelity import accountBalanceFidelity
from Frames.AccountBalance.accountBalanceRobinhood import accountBalanceRobinhood
from Frames.Update.Fidelity.fidelitySell import fidelitySell
from Frames.Update.Robinhood.robinhoodBuy import robinhoodBuy
from Frames.Update.Robinhood.robinhoodPerformance import robinhoodPerformance
from Frames.Update.Robinhood.robinhoodSell import robinhoodSell
from Frames.Update.prospectiveBuy import prospectiveBuy
from Frames.Update.Fidelity.fidelityBuy import fidelityBuy
from Frames.Update.Robinhood.robinhoodAccountBalance import robinhoodAccountBalance
from Frames.Update.Fidelity.fidelityPerformance import fidelityPerformance
from Frames.Update.Fidelity.fidelityAccountBalance import fidelityAccountBalance
from Frames.StockHoldings.stockHoldingsRobinhood import stockHoldingsRobinhood
from Frames.AccountBalance.accountBalanceAll import accountBalanceAll
from Frames.index import index
from Frames.Performance.Robinhood import performanceRobinhood
from Frames.StockHoldings.stockHoldingsFidelity import stockHoldingsFidelity
from Frames.Performance.Fidelity import performanceFidelity
from Common.TickerListTotalPrice import TickerListTotalPrice
from SetDefaultData.Common import Common

class MenuCommands:

    @staticmethod
    async def showRobinhoodBuyFrame(tkroot, table_update_response):
        MenuCommands.hideAllFrames(tkroot)
        robinhoodBuy(tkroot)
        default_total = await TickerListTotalPrice().getTotalCurrentPriceAsync(tkroot.default_robinhood_buy_list) 
        try:                
            tkroot.label_rb_total.config(text="Current price total: ${:,.2f}".format(default_total)) 
            tkroot.rb_label_response.config(text = table_update_response)
        except Exception:
            pass

    @staticmethod
    def showRobinhoodSellFrame(tkroot, table_update_response):
        MenuCommands.hideAllFrames(tkroot)
        robinhoodSell(tkroot)
        tkroot.rbs_label_response.config(text = table_update_response)

    @staticmethod
    async def showFidelityBuyFrame(tkroot, table_update_response):
        MenuCommands.hideAllFrames(tkroot)
        fidelityBuy(tkroot)
        default_total = await TickerListTotalPrice().getTotalCurrentPriceAsync(tkroot.default_fidelity_buy_list)     
        try:
            tkroot.label_fidelity_total.config(text="Current price total: ${:,.2f}".format(default_total)) 
            tkroot.fidelity_label_response.config(text = table_update_response)
        except Exception:
            pass

    @staticmethod
    async def showAccountBalanceRobinhoodFrame(tkroot):
        MenuCommands.hideAllFrames(tkroot)
        accountBalanceRobinhood(tkroot)
        purchasing_power = Common.purchasingPower('robinhood_account') 
        robinhood_ticker_buy_list = Common.tickers('robinhood_buy', index=1)
        robinhood_ticker_buy_total_price = await TickerListTotalPrice.getTotalCurrentPriceAsync(robinhood_ticker_buy_list)
        balance_difference = purchasing_power - robinhood_ticker_buy_total_price
        try:
            tkroot.label_abr_pbbd.config(text = "Prospective Buy Balance: ${:,.2f}".format(balance_difference))
        except Exception:
            pass

        if robinhood_ticker_buy_list != '':
            closing_prices_dict = await TickerListTotalPrice.closingPricesAsync(robinhood_ticker_buy_list)
            accumulated_sum = TickerListTotalPrice().accumulatedSum(closing_prices_dict)
            ticker_filter_ab = TickerListTotalPrice().filterByAccountBalance(accumulated_sum, purchasing_power)
            ticker_filter_ab = Helper.sortAscending(ticker_filter_ab)
            if len(ticker_filter_ab) == 0:
                try:
                    tkroot.label_abr_spaav.config(text = "\t No stocks available to purchase")
                except Exception:
                    pass
            else:
                try:
                    tkroot.label_abr_spaav.config(text =', '.join(ticker_filter_ab))
                except Exception:
                    pass
        else:
            tkroot.label_abr_spaav.config(text ="\t No stocks listed in buy list.")

    @staticmethod
    async def showAccountBalanceFidelityFrame(tkroot):
        MenuCommands.hideAllFrames(tkroot)
        accountBalanceFidelity(tkroot)
        purchasing_power = Common.purchasingPower('fidelity_account')
        fidelity_ticker_buy_list = Common.tickers('fidelity_buy', index=1)
        fidelity_ticker_buy_total_price = await TickerListTotalPrice.getTotalCurrentPriceAsync(fidelity_ticker_buy_list)
        balance_difference = purchasing_power - fidelity_ticker_buy_total_price
        try:
            tkroot.label_abf_pbb.config(text = "Prospective Buy Balance: ${:,.2f}".format(balance_difference))
        except Exception:
            pass

        if fidelity_ticker_buy_list != '':
            closing_prices_dict = await TickerListTotalPrice.closingPricesAsync(fidelity_ticker_buy_list)
            accumulated_sum = TickerListTotalPrice().accumulatedSum(closing_prices_dict)
            ticker_filter_ab = TickerListTotalPrice().filterByAccountBalance(accumulated_sum, purchasing_power)
            ticker_filter_ab = Helper.sortAscending(ticker_filter_ab)
            if len(ticker_filter_ab) == 0:
                try:
                    tkroot.label_abf_spaav.config(text = "\t No stocks available to purchase")
                except Exception:
                    pass
            else:
                try:
                    tkroot.label_abf_spaav.config(text =', '.join(ticker_filter_ab))
                except Exception:
                    pass
        else:
            tkroot.label_abf_spaav.config(text ="\t No stocks listed in buy list.")


    @staticmethod 
    def showFidelitySellFrame(tkroot):
        MenuCommands.hideAllFrames(tkroot)
        fidelitySell(tkroot)

    @staticmethod
    def robinhoodHoldingsUpload():
        filename = filedialog.askopenfile(initialdir="./", title="Select Robinhood Holdings CSV", filetypes=[("csv files", "*.csv")])
        robinhoodHoldingsImport(filename)

    @staticmethod
    def showRobinhoodPerformanceFrame(tkroot, table_update_response):
        MenuCommands.hideAllFrames(tkroot)
        robinhoodPerformance(tkroot)
        tkroot.rbp_label_response.config(text=table_update_response)

    @staticmethod
    def showRobinhoodAccountBalanceFrame(tkroot, table_update_response):
        MenuCommands.hideAllFrames(tkroot)
        robinhoodAccountBalance(tkroot)
        tkroot.rab_label_response.config(text=table_update_response)

    @staticmethod
    def showFidelityAccountBalanceFrame(tkroot, table_update_response):
        MenuCommands.hideAllFrames(tkroot)
        fidelityAccountBalance(tkroot)
        tkroot.fab_label_response.config(text=table_update_response)

    @staticmethod
    def fidelityUpload():
        filename = filedialog.askopenfile(initialdir="./", title="Select Fidelity holdings CSV", filetypes=[("csv files", "*.csv")])
        fidelityHoldingsImport(filename)

    @staticmethod
    async def showProspectiveBuyFrame(tkroot, table_update_response):
        MenuCommands.hideAllFrames(tkroot)
        prospectiveBuy(tkroot)
        default_total = await TickerListTotalPrice().getTotalCurrentPriceAsync(tkroot.default_prospective_buy_list)  
        try:
            tkroot.label_pb_total.config(text="Current price total: ${:,.2f}".format(default_total)) 
            tkroot.pb_label_response.config(text = table_update_response)
        except Exception:
            pass

    @staticmethod
    def showFidelityPerformanceFrame(tkroot, table_update_response):
        MenuCommands.hideAllFrames(tkroot)
        fidelityPerformance(tkroot)
        tkroot.fp_label_response.config(text=table_update_response)

    @staticmethod
    def showStockHoldingsRobinhoodFrame(tkroot):
        MenuCommands.hideAllFrames(tkroot)
        stockHoldingsRobinhood(tkroot)

    @staticmethod
    def showStockHoldingsFidelityFrame(tkroot):
        MenuCommands.hideAllFrames(tkroot)
        stockHoldingsFidelity(tkroot)

    @staticmethod
    def showIndexFrame(tkroot):
        MenuCommands.hideAllFrames(tkroot)
        index(tkroot)

    @staticmethod
    def showPerformanceRobinhoodFrame(tkroot):
        MenuCommands.hideAllFrames(tkroot)
        performanceRobinhood(tkroot)

    @staticmethod
    def showPerformanceFidelityFrame(tkroot):
        MenuCommands.hideAllFrames(tkroot)
        performanceFidelity(tkroot)

    @staticmethod
    def showAccountBalanceAllFrame(tkroot):
        MenuCommands.hideAllFrames(tkroot)
        accountBalanceAll(tkroot)

    @staticmethod
    def noCommand():
        pass

    @staticmethod
    def hideAllFrames(tkroot):
        for child in tkroot.winfo_children():
            if(type(child) == ttk.Frame):
                child.destroy()         
