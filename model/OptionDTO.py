from enum import Enum


class OptionType(Enum):
    CALL = 'call'
    PUT = 'put'


class OptionPosition(Enum):
    LONG = 'long'
    SHORT = 'short'
    UNDEFINED = 'undefined'


class Option:

    def __init__(self, vol, chg, last, bid, ask, strike, m_type: OptionType, position: OptionPosition):
        self.vol = vol
        self.chg = chg
        self.last = last
        self.bid = bid
        self.ask = ask
        self.strike = strike
        self.m_type = m_type
        self.position = position

    def __str__(self):
        return str({'vol': self.vol, 'chg': self.chg, 'last': self.last, 'bid': self.bid, 'ask': self.ask,
                    'strike': self.strike})

    def get_price(self):
        # if self.last == '' and self.ask != '0.010':
        #     return self.ask
        # else:
        return self.last

    # def toJSON(self):
    #     return json.dumps(self, default=lambda o: o.__dict__,
    #                       sort_keys=True, indent=4)
# class OptionEncoder(JSONEncoder):
#     def default(self, o):
#         return o.__dict__
