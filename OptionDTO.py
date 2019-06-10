import json


class Option:
    def __init__(self, vol, chg, last, bid, ask, strike):
        self.vol = vol
        self.chg = chg
        self.last = last
        self.bid = bid
        self.ask = ask
        self.strike = strike

    def __str__(self):
        return str({'vol': self.vol, 'chg': self.chg, 'last': self.last, 'bid': self.bid, 'ask': self.ask,
                    'strike': self.strike})

    # def toJSON(self):
    #     return json.dumps(self, default=lambda o: o.__dict__,
    #                       sort_keys=True, indent=4)
# class OptionEncoder(JSONEncoder):
#     def default(self, o):
#         return o.__dict__
