from tkinter import *
from Menu.MenuCommands import MenuCommands
from async_tkinter_loop import async_command

class MainMenu:
    def __init__(self, tkRoot):
        self.root = tkRoot
        self.menubar = Menu(tkRoot)
        self.importMenu()
        self.updateMenu()
        self.updateProspectiveMenu()
        self.updateRobinhoodMenu()
        self.updatefidelityMenu()
        self.accountBalancesMenu()
        self.holdingsMenu()
        self.performanceMenu()

    def importMenu(self):
        file_menu = Menu(self.menubar, tearoff=0)
        file_menu.add_command(label="Getting Started", command=lambda: MenuCommands.showIndexFrame(self.root))
        import_menu = Menu(self.menubar, tearoff=0)
        import_menu.add_command(label="Robinhood Portfolio...", command=MenuCommands.robinhoodHoldingsUpload)
        import_menu.add_command(label="Fidelity Portfolio...", command=MenuCommands.fidelityUpload)
        
        file_menu.add_cascade(label="Import", menu=import_menu)
        self.menubar.add_cascade(label="File", menu=file_menu)

    def updateMenu(self):
        self.updatemenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Update", menu=self.updatemenu)

    def updateProspectiveMenu(self):
        self.updatemenu.add_command(label="Prospective Buy List", command=async_command(MenuCommands.showProspectiveBuyFrame,self.root, ""))        

    def updateRobinhoodMenu(self):
        robinhoodupdate = Menu(self.updatemenu, tearoff=0)
        robinhoodupdate.add_command(label="Performance", command=lambda: MenuCommands.showRobinhoodPerformanceFrame(self.root, ""))
        robinhoodupdate.add_command(label="Balances", command=lambda: MenuCommands.showRobinhoodAccountBalanceFrame(self.root, ""))
        robinhoodupdate.add_command(label="Sell list", command=lambda: MenuCommands.showRobinhoodSellFrame(self.root, ""))
        robinhoodupdate.add_command(label="Buy list",  command= async_command(MenuCommands.showRobinhoodBuyFrame, self.root, ""))
        self.updatemenu.add_cascade(label="Robinhood", menu=robinhoodupdate)

    def updatefidelityMenu(self):
        fidelityupdate = Menu(self.updatemenu, tearoff=0)
        fidelityupdate.add_command(label="Performance", command=lambda: MenuCommands.showFidelityPerformanceFrame(self.root, ""))
        fidelityupdate.add_command(label="Balances", command=lambda: MenuCommands.showFidelityAccountBalanceFrame(self.root, ""))
        fidelityupdate.add_command(label="Sell list", command=lambda: MenuCommands.showFidelitySellFrame(self.root))
        fidelityupdate.add_command(label="Buy list", command= async_command(MenuCommands.showFidelityBuyFrame, self.root, ""))
        self.updatemenu.add_cascade(label="Fidelity", menu=fidelityupdate)
    
    def accountBalancesMenu(self):
        account_balance_menu = Menu(self.menubar, tearoff=0)
        account_balance_menu.add_command(label="All", command=lambda: MenuCommands.showAccountBalanceAllFrame(self.root))
        account_balance_menu.add_command(label="Robinhood", command=async_command(MenuCommands.showAccountBalanceRobinhoodFrame, self.root))
        account_balance_menu.add_command(label="Fidelity", command=async_command(MenuCommands.showAccountBalanceFidelityFrame, self.root))
      
        self.menubar.add_cascade(label="Account Balances", menu=account_balance_menu)

    def holdingsMenu(self):
        holdings_menu = Menu(self.menubar, tearoff=0)
        holdings_menu.add_command(label="Robinhood", command=lambda: MenuCommands.showStockHoldingsRobinhoodFrame(self.root))
        holdings_menu.add_command(label="Fidelity", command=lambda: MenuCommands.showStockHoldingsFidelityFrame(self.root))
        self.menubar.add_cascade(label="Stock Holdings", menu=holdings_menu)

    def performanceMenu(self):
        performance_menu = Menu(self.menubar, tearoff=0)
        performance_menu.add_command(label="Robinhood", command=lambda: MenuCommands.showPerformanceRobinhoodFrame(self.root))
        performance_menu.add_command(label="Fidelity", command=lambda: MenuCommands.showPerformanceFidelityFrame(self.root))
        self.menubar.add_cascade(label="Performance", menu=performance_menu)