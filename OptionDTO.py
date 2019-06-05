from json import JSONEncoder


class Option:
    def __init__(self, vol, chg, last, bid, ask, strike):
        self.vol = vol
        self.chg = chg
        self.last = last
        self.bid = bid
        self.ask = ask
        self.strike = strike


class OptionEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
