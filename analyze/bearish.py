from Strategy import *
from copy import copy


def bearish(code, month):
    BearPutSpread(code, month).analyze()
    BearCallSpread(code, month).analyze()
    SyntheticShortStock(code, month).analyze()


# def bearish_out(code, month) -> str:
#     out = ""
#     out += BearPutSpread(code, month).output()
#     out += BearCallSpread(code, month).output()
#     out += SyntheticShortStock(code, month).output()
#     return out


# Bearish
class SyntheticShortStock(Strategy):

    def get_pairs(self):
        pairs = []
        for call in self.call_options:
            if call.get_price() != '':
                for put in self.put_options:
                    if put.get_price() != '':
                        if put.strike == call.strike:
                            call.position = OptionPosition.SHORT
                            put.position = OptionPosition.LONG
                            pairs.append([call, put])
        return pairs

    def __init__(self, code, month):
        super().__init__(code, month)

    def get_even_price(self, pair: List):
        put = pair[1]
        call = pair[0]
        return float(put.strike) + float(self.get_credit(pair))

    def get_max_win(self, pair: List):
        return 'any below ' + str(self.get_even_price(pair))

    def get_max_loss(self, pair: List):
        return 'any above ' + str(self.get_even_price(pair))

    def get_credit(self, pair: List):
        put = pair[1]
        call = pair[0]
        return float(call.get_price()) - float(put.get_price())

    def get_loss_win_ratio(self, pair):
        return NA


class BearCallSpread(Strategy):

    def __init__(self, code, month):
        super().__init__(code, month)

    def get_pairs(self):
        pairs = []
        option_index = []
        for num in range(len(self.call_options)):
            if self.call_options[num].get_price() == '':
                continue
            option_index.append(num)
        for num in option_index:
            option1 = self.call_options[num]
            option1.position = OptionPosition.SHORT
            for num2 in option_index:
                if num2 > num:
                    option2 = self.call_options[num2]
                    option2.position = OptionPosition.LONG
                    pairs.append([copy(option1), copy(option2)])
        return pairs

    def get_even_price(self, pair: List):
        return float(pair[0].strike) + self.get_credit(pair)

    def get_max_win(self, pair: List):
        return self.get_credit(pair)

    def get_max_loss(self, pair: List):
        return float(pair[1].strike) - float(pair[0].strike) - self.get_credit(pair)

    def get_credit(self, pair: List):
        return float(pair[0].get_price()) - float(pair[1].get_price())

    def get_loss_win_ratio(self, pair):
        if self.get_max_win(pair) > 0:
            return str(self.get_max_loss(pair) / self.get_max_win(pair))
        else:
            return NA


class BearPutSpread(Strategy):

    def __init__(self, code, month):
        super().__init__(code, month)

    def get_pairs(self):
        option_index = []
        pair = []
        for num in range(len(self.put_options)):
            if self.put_options[num].get_price() == '':
                continue
            option_index.append(num)
        for num in option_index:
            option1 = self.put_options[num]
            option1.position = OptionPosition.SHORT
            for num2 in option_index:
                if num2 > num:
                    option2 = self.put_options[num2]
                    option2.position = OptionPosition.LONG
                    pair.append([copy(option1), copy(option2)])
        return pair

    def get_even_price(self, pair: List):
        return float(pair[1].strike) - self.get_credit(pair)

    def get_max_win(self, pair: List):
        return float(pair[1].strike) - float(pair[0].strike) - self.get_credit(pair)

    def get_max_loss(self, pair: List):
        return self.get_credit(pair)

    def get_credit(self, pair: List):
        return float(pair[1].get_price()) - float(pair[0].get_price())

    def get_loss_win_ratio(self, pair):
        if self.get_max_win(pair) == 0:
            return ""
        return str(self.get_max_loss(pair) / self.get_max_win(pair))

# code_input = sys.argv[1]
# month_input = sys.argv[2]
# bearish(code_input, month_input)
