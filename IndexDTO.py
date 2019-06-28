from Util import print_class


class Index:
    def __init__(self, price: str, high: str, low: str, turnover: str, chg: str, open: str, close: str):
        self.price = price
        self.high = high
        self.low = low
        self.turnover = turnover
        self.chg = chg
        self.open = open
        self.close = close

    def print(self):
        print_class(self)
