from Strategy import *


def volatile(code, month):
    ShortCallCalendarSpread(code, month).analyze()
    ShortPutCalendarSpread(code, month).analyze()
    LongStangle(code, month).analyze()
    LongStraddle(code, month).analyze()


# Volatile
class LongStangle(Strategy):

    def __init__(self, code, month):
        super().__init__(code, month)

    def get_pairs(self):
        pair = []
        for call in self.call_options:
            if call.get_price() != '':
                for put in self.put_options:
                    if put.get_price() != '' and call.strike > put.strike:
                        pair.append([call, put])
        return pair

    def get_even_price(self, pair: List):
        call = pair[0]
        put = pair[1]
        lower_limit = float(put.strike) - float(self.get_credit(pair))
        upper_limit = float(call.strike) + float(self.get_credit(pair))
        even_price = str(lower_limit) + ' to ' + str(upper_limit)
        return even_price

    def get_max_win(self, pair: List):
        call = pair[0]
        put = pair[1]
        lower_limit = float(put.strike) - float(self.get_credit(pair))
        upper_limit = float(call.strike) + float(self.get_credit(pair))
        win_max = 'any below: ' + str(lower_limit) + ' and any above: ' + str(upper_limit)
        return win_max

    def get_max_loss(self, pair: List):
        return self.get_credit(pair)

    def get_credit(self, pair: List):
        call = pair[0]
        put = pair[1]
        return float(call.get_price()) + float(put.get_price())

    def get_loss_win_ratio(self, pair):
        return self.default_loss_win_ratio(pair)


class LongStraddle(Strategy):

    def __init__(self, code, month):
        super().__init__(code, month)

    def get_pairs(self):
        pairs = []
        for call in self.call_options:
            if call.get_price() != '':
                for put in self.put_options:
                    if put.get_price() != '' and call.strike == put.strike:
                        pairs.append([call, put])
        return pairs

    def get_even_price(self, pair: List):
        call = pair[0]
        put = pair[1]
        lower_limit = float(call.strike) - float(self.get_credit(pair))
        upper_limit = float(call.strike) + float(self.get_credit(pair))
        even_price = str(lower_limit) + ' to ' + str(upper_limit)
        return even_price

    def get_max_win(self, pair: List):
        call = pair[0]
        put = pair[1]
        lower_limit = float(call.strike) - float(self.get_credit(pair))
        upper_limit = float(call.strike) + float(self.get_credit(pair))
        win_max = 'any below: ' + str(lower_limit) + ' and any above: ' + str(upper_limit)
        return win_max

    def get_max_loss(self, pair: List):
        return self.get_credit(pair)

    def get_credit(self, pair: List):
        call = pair[0]
        put = pair[1]
        return float(call.get_price()) + float(put.get_price())

    def get_loss_win_ratio(self, pair):
        return self.default_loss_win_ratio(pair)


class ShortPutCalendarSpread(CalendarStrategy):

    def get_pairs(self):
        pairs = []
        for put in self.puts0:
            if put.get_price() != '':
                for put1 in self.puts1:
                    if put1.get_price() != '' and put1.strike == put.strike:
                        put.position = OptionPosition.SHORT
                        put1.position = OptionPosition.SHORT
                        pairs.append([put, put1])
                # long_put_calendar_spread_print(put, put1, month, month1)
                for put2 in self.puts2:
                    if put2.get_price() != '' and put2.strike == put.strike:
                        put.position = OptionPosition.SHORT
                        put2.position = OptionPosition.SHORT
                        pairs.append([put, put2])
        return pairs

    def get_even_price(self, pair: List):
        return 'Maximum when the stock price is further away from strike price on the nearby expiry date'

    def get_max_win(self, pair: List):
        return self.get_credit(pair)

    def get_max_loss(self, pair: List):
        return 'Time decay (Short put) - time decay (Long put)'

    def get_credit(self, pair: List):
        put1 = pair[1]
        put = pair[0]
        return float(put1.get_price()) - float(put.get_price())

    def get_loss_win_ratio(self, pair):
        return NA


class ShortCallCalendarSpread(CalendarStrategy):

    def get_pairs(self):
        pairs = []
        for call in self.calls0:
            if call.get_price() != '':
                for call1 in self.calls1:
                    if call1.get_price() != '' and call1.strike == call.strike:
                        call.position = OptionPosition.SHORT
                        call1.position = OptionPosition.SHORT
                        pairs.append([call, call1])
                for call2 in self.calls2:
                    if call2.get_price() != '' and call2.strike == call.strike:
                        call.position = OptionPosition.SHORT
                        call2.position = OptionPosition.SHORT
                        pairs.append([call, call2])
        return pairs

    def get_even_price(self, pair: List):
        return 'Stock price is further away from strike price on the nearby expiry date'

    def get_max_win(self, pair: List):
        return self.get_credit(pair)

    def get_max_loss(self, pair: List):
        return 'Time decay (Short call) - time decay (Long call)'

    def get_credit(self, pair: List):
        call = pair[0]
        call1 = pair[1]
        return float(call1.get_price()) - float(call.get_price())

    def get_loss_win_ratio(self, pair):
        return NA

# code_input = sys.argv[1]
# month_input = sys.argv[2]
# volatile(code_input, month_input)
# ShortPutCalendarSpread('CNC', '202001').analyze()
