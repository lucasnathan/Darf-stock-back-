from itertools import groupby
from functools import reduce

class TaxCalculator:
    @staticmethod
    def calculate_tax(financial_operations):
        grouped = [list(g) for k, g in groupby(financial_operations, lambda fo: fo.asset_name)]
        print(grouped)
        x = [ TaxCalculator.calculate_balance(fo) for fo in grouped ]
        return financial_operations


    @staticmethod
    def calculate_balance(asset_financial_operations):   
        buys_balance = TaxCalculator.filter_and_sum(asset_financial_operations)
        sells_balance = TaxCalculator.filter_and_sum(asset_financial_operations, 'V')

        total_balance = sells_balance - buys_balance
        print(total_balance)
        return total_balance

    def filter_and_sum(asset_financial_operations, search_filter='C'):
        buys_operations = list(filter(lambda fo: fo.op_type == search_filter, asset_financial_operations))
        buys_balance = 0.0
        for buy_operation in buys_operations:
            buys_balance += buy_operation.total_price()
        return buys_balance