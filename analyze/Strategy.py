from abc import ABC, abstractmethod
from typing import List
from scrap import scrap
from OptionDTO import *

NA = 'N/A'


class Strategy(ABC):
    @abstractmethod
    def __init__(self, code, month):
        self.code = code
        self.month = month
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

    def get_premium(self, pair: List):
        return float(self.stock.price) - float(self.get_even_price(pair))

    @staticmethod
    def print_result(options: List[Option], premium: str, even_price: str, win_at: str, max_loss: str,
                     max_win: str, max_loss_to_max_win: str):
        for option in options:
            print(option.position.value + ' ' + option.m_type.value)
            print(option)
        print('premium: ' + str(premium))
        print('even price: ' + str(even_price))
        print('win at: ' + str(win_at))
        print('max_loss: ' + str(max_loss))
        print('max_win: ' + str(max_win))
        print('max_loss_to_max_win: ' + max_loss_to_max_win)
        print('\n---------------------------------------------------------------------------')
        print('\n')

    def default_loss_win_ratio(self, pair):
        return str(self.get_max_loss(pair) / self.get_max_win(pair))

    def analyze(self):
        print(self.__class__.__name__ + '\n')
        for pair in self.pairs:
            self.print_result(pair, str(self.get_credit(pair)), str(self.get_even_price(pair)),
                              str(self.get_even_price(pair)),
                              str(self.get_max_loss(pair)), str(self.get_max_win(pair)),
                              str(self.get_loss_win_ratio(pair)))

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
