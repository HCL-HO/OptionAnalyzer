from abc import ABC, abstractmethod
from typing import List
from scrap import scrap
from OptionDTO import *
from stock import get_stock
from common import dict_prettify

NA = 'N/A'


# Abstract Class of Trading Strategies
class Strategy(ABC):
    # Parms: month, stock code
    # Web Scrap Options Listing in constructor
    @abstractmethod
    def __init__(self, code, month=None):
        self.code = code
        self.month = month
        if month is None:
            self.stock = get_stock(code)
        else:
            result = scrap(code, month)
            self.put_options = result['option']['put']
            self.call_options = result['option']['call']
            self.stock = result['stock']
            self.pairs = self.get_pairs()

    @abstractmethod
    def get_pairs(self):
        pass

    @abstractmethod
    def get_even_price(self, pair: List):
        pass

    @abstractmethod
    def get_max_win(self, pair: List):
        pass

    @abstractmethod
    def get_max_loss(self, pair: List):
        pass

    @abstractmethod
    def get_credit(self, pair: List):
        pass

    # Net Cash Inflow
    def get_premium(self, pair: List):
        return float(self.stock.price) - float(self.get_even_price(pair))

    @staticmethod
    def format_analytic_str(options: List[Option], premium: str, even_price: str, win_at: str, max_loss: str,
                            max_win: str, max_loss_to_max_win: str) -> str:
        result = ''
        for option in options:
            # result = result + option.position.value + ' ' + option.m_type.value
            result = result + option.__str__() + '\n'
        result = result + 'premium: ' + str(premium) + '\n'
        result = result + 'even price: ' + str(even_price) + '\n'
        result = result + 'win at: ' + str(win_at) + '\n'
        result = result + 'max_loss: ' + str(max_loss) + '\n'
        result = result + 'max_win: ' + str(max_win) + '\n'
        result = result + 'max_loss_to_max_win: ' + max_loss_to_max_win + '\n'
        result = result + '\n---------------------------------------------------------------------------' + '\n'
        result = result + '\n'
        return result

    @staticmethod
    def format_analytic_str2(trade_position: dict):
        result = ''
        result = result + dict_prettify(trade_position)
        result = result + '\n---------------------------------------------------------------------------' + '\n'
        result = result + '\n'
        return result

    def get_analytic_str(self, pair) -> str:
        trade_positions = self.get_trade_position(pair)
        return Strategy.format_analytic_str2(trade_positions)
        # return Strategy.format_analytic_str(pair, str(self.get_credit(pair)), str(self.get_even_price(pair)),
        #                                     str(self.get_even_price(pair)),
        #                                     str(self.get_max_loss(pair)), str(self.get_max_win(pair)),
        #                                     str(self.get_loss_win_ratio(pair)))

    def get_trade_position(self, pair) -> dict:
        trade_position = dict()
        options = dict()
        for option in pair:
            options[option.position.value + '_' + option.m_type.value] = option.__str__()
        trade_position['options'] = options
        trade_position['even_price'] = self.get_even_price(pair)
        trade_position['max_loss'] = self.get_max_loss(pair)
        trade_position['max_win'] = self.get_max_win(pair)
        trade_position['loss_to_win'] = self.get_loss_win_ratio(pair)
        print('trade_position')
        print(trade_position)
        return trade_position

    def default_loss_win_ratio(self, pair):
        return str(self.get_max_loss(pair) / self.get_max_win(pair))

    def analyze(self):
        print(self.__class__.__name__ + '\n')
        for pair in self.pairs:
            self.analyze_single(pair)
        return self.get_pairs()

    def analyze_single(self, pair):
        print(self.__class__.__name__ + '\n')
        print(self.get_analytic_str(pair))

    def output(self) -> str:
        out_text = ""
        out_text += self.__class__.__name__ + '\n'
        for pair in self.pairs:
            out_text += self.get_analytic_str(pair)
        return out_text

    @abstractmethod
    def get_loss_win_ratio(self, pair):
        pass


class CalendarStrategy(Strategy, ABC):

    def __init__(self, code, month):
        self.month0 = month
        self.month1 = self.get_month(month, 1)
        self.month2 = self.get_month(month, 2)
        result0 = scrap(code, month)
        result1 = scrap(code, self.month1)
        result2 = scrap(code, self.month2)
        self.puts0 = result0['option']['put']
        self.puts1 = result1['option']['put']
        self.puts2 = result2['option']['put']
        self.calls0 = result0['option']['call']
        self.calls1 = result1['option']['call']
        self.calls2 = result2['option']['call']
        super().__init__(code, month)

    @staticmethod
    def get_month(month, param):
        old_month = month[4:]
        old_year = month[:4]
        new_month = int(old_month) + param
        new_year = int(old_year)
        if new_month >= 13:
            new_month = new_month - 12
            new_year += 1
        return str(new_year) + "{:02d}".format(new_month)

# BearCallSpread('CNC', '202001').analyze()
# BearPutSpread('CNC', '202001').analyze()
