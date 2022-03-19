import os
import sqlite3
from Common.Helper import Helper
from Database.CommonSqliteActions import CommonSqliteActions

class Common:
    db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Database', 'investment_accounts.db'))

    @staticmethod
    def purchasingPower(table_name):
        try:
            sql = CommonSqliteActions()
            records_exist = [row[0] for row in sql.cursor.execute(
                "SELECT EXISTS(SELECT 1 FROM {} WHERE insert_date IS NOT NULL)".format(table_name))]
            if records_exist[0] != 1:
                return 0
            buying_power = [buying_power[0] for buying_power in sql.cursor.execute(
                "SELECT buying_power from {} order by insert_date desc limit 1".format(table_name))][0]
            buying_power = 0 if buying_power is None else buying_power

            sql.closeDb()

            return buying_power

        except sqlite3.Error as error:
            return error.args

    @staticmethod
    def accountBalance(table_name):
        try:
            sql = CommonSqliteActions()
            records_exist = [row[0] for row in sql.cursor.execute(
                "SELECT EXISTS(SELECT 1 FROM {} WHERE insert_date IS NOT NULL)".format(table_name))]
            if records_exist[0] != 1:
                return 0
            portfolio_value = [portfolio_value[0] for portfolio_value in sql.cursor.execute(
                "SELECT portfolio_value from {} order by insert_date desc limit 1".format(table_name))][0]
            portfolio_value = 0 if portfolio_value is None else portfolio_value
            sql.closeDb()
            return portfolio_value

        except sqlite3.Error as error:
            return error.args

    @staticmethod
    def lastUpdated(table_name):
        try:
            sql = CommonSqliteActions()
            records_exist = [row[0] for row in sql.cursor.execute(
                "SELECT EXISTS(SELECT 1 FROM {} WHERE insert_date IS NOT NULL)".format(table_name))]
            if records_exist[0] != 1:
                return "No Records"
            last_modified_date = [datetime[0] for datetime in sql.cursor.execute(
                "select insert_date from {} order by insert_date desc LIMIT 1".format(table_name))][0]
            last_modified_date = Helper.dateTimeFormat(last_modified_date)

            sql.closeDb()

            return last_modified_date

        except sqlite3.Error as error:
            return error.args

    @staticmethod
    def tickers(table_name, index=0):
        try:
            sql = CommonSqliteActions()

            tickers = [ticker[index] for ticker in sql.cursor.execute("SELECT * FROM {}".format(table_name))]
            tickers = Helper.sortAscending(tickers)
            tickers = ",".join(tickers)

            sql.closeDb()

            return tickers

        except sqlite3.Error as error:
            return error.args

    @staticmethod
    def metrics(table_name):
        try:
            sql = CommonSqliteActions()
            records_exist = [row[0] for row in sql.cursor.execute(
                'SELECT EXISTS(SELECT 1 FROM {} WHERE insert_date IS NOT NULL)'.format(table_name))]

            field_names = [field_name[0] for field_name in
                           sql.cursor.execute("select name from PRAGMA_TABLE_INFO('{}');".format(table_name))]

            metrics = {}
            if records_exist[0] != 1:
                for i in range(len(field_names)):
                    metrics[field_names[i]] = 0
                return metrics

            row = [row for row in
                   sql.cursor.execute("select * from {} ORDER by insert_date limit 1".format(table_name))]
            row = row[0]

            for i in range(len(row)):
                metrics[field_names[i]] = metrics[field_names[i]] = 0 if row[i] is None else row[i]

            sql.closeDb()

            return metrics

        except sqlite3.Error as error:
            return error.args
