from Database.CommonSqliteActions import CommonSqliteActions

class DatabaseInit(CommonSqliteActions):
    def __init__(self):
        super().__init__()       
        self.createRobinhoodTables()
        self.createFidelityTables()
        self.createRobinhoodTransactionsTables()
        self.createFidelityTransactionsTable()
        self.createPotentialBuyTable()
        self.closeDb()

    def createRobinhoodTables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS robinhood_portfolio
                    (ticker text, name text, shares float, return float, equity float, percent_gain float, percent_allocation float)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS robinhood_account
                    (insert_date text, buying_power float, portfolio_value float)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS robinhood_performance
                    (insert_date text, one_day_dollar float, one_week_dollar float, one_month_dollar float, three_month_dollar float, one_year_dollar float, all_time_dollar float, all_time_percentage float)''')

    def createFidelityTables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS fidelity_portfolio
                    (ticker text, name text, shares float, return float, equity float, percent_gain float, percent_allocation float)''')

        self.cursor.execute(('''CREATE TABLE IF NOT EXISTS fidelity_account
                    (insert_date text, buying_power float, portfolio_value float)'''))

        self.cursor.execute(('''CREATE TABLE IF NOT EXISTS fidelity_performance
                    (insert_date text, percent_one_day float, percent_ytd float, percent_one_year float, percent_three_year float, percent_five_year float, percent_ten_year float )'''))

    def createRobinhoodTransactionsTables(self):
        self.cursor.execute(('''CREATE TABLE IF NOT EXISTS robinhood_buy
                    (insert_date text, ticker text)'''))

        self.cursor.execute(('''CREATE TABLE IF NOT EXISTS robinhood_sell
                    (insert_date text, ticker text)'''))

    def createFidelityTransactionsTable(self):
        self.cursor.execute(('''CREATE TABLE IF NOT EXISTS fidelity_buy
                    (insert_date text, ticker text)'''))

        self.cursor.execute(('''CREATE TABLE IF NOT EXISTS fidelity_sell
                    (insert_date text, ticker text)'''))
    def createPotentialBuyTable(self):
        self.cursor.execute(('''CREATE TABLE IF NOT EXISTS prospective_buy
                    (insert_date text, ticker text)'''))