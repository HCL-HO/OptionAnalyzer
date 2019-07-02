from Util import print_class


class Stock:
    def __init__(self, price: str, high: str, low: str, turnover: str, chg: str, m_high: str, m_low: str):
        self.price = price
        self.high = high
        self.low = low
        self.turnover = turnover
        self.chg = chg
        self.m_high = m_high
        self.m_low = m_low

    def print(self):
        print_class(self)
