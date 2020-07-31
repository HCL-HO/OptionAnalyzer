from analyze import *
from Strategy import *
import copy


def bullish(code, month):
    BullCallSpread(code, month).analyze()
    BullPutSpread(code, month).analyze()
    SyntheticLong(code, month).analyze()


class SyntheticLong(Strategy):
    def __init__(self, code, month):
        super().__init__(code, month)

    def get_pairs(self):
        pairs = []
        for call in self.call_options:
            if call.get_price() != '':
                for put in self.put_options:
                    if put.get_price() != '':
                        if put.strike == call.strike:
                            call.position = OptionPosition.LONG
                            put.position = OptionPosition.SHORT
                            pairs.append([call, put])
        return pairs

    def get_even_price(self, pair: List):
        call = pair[0]
        return float(call.strike) - float(self.get_credit(pair))

    def get_max_win(self, pair: List):
        return 'any below ' + str(self.get_even_price(pair))

    def get_max_loss(self, pair: List):
        return 'any above ' + str(self.get_even_price(pair))

    def get_credit(self, pair: List):
        call = pair[0]
        put = pair[1]
        return float(put.get_price())-float(call.get_price())

    def get_loss_win_ratio(self, pair):
        return NA


class BullPutSpread(Strategy):
    def __init__(self, code, month):
        super().__init__(code, month)

    def get_pairs(self):
        pairs = []
        option_index = []
        for num in range(len(self.put_options)):
            if self.put_options[num].get_price() == '':
                continue
            option_index.append(num)
        for num in option_index:
            option1 = self.put_options[num]
            option1.position = OptionPosition.LONG
            for num2 in option_index:
                if num2 > num:
                    option2 = self.put_options[num2]
                    option2.position = OptionPosition.SHORT
                    pairs.append([copy.copy(option1), copy.copy(option2)])
        return pairs

    def get_even_price(self, pair: List):
        option1 = pair[0]
        option2 = pair[1]
        return float(option2.strike) - self.get_credit(pair)

    def get_max_win(self, pair: List):
        option1 = pair[0]
        option2 = pair[1]
        return float(option2.get_price()) - float(option1.get_price())

    def get_max_loss(self, pair: List):
        option1 = pair[0]
        option2 = pair[1]
        return float(option2.strike) - float(option1.strike) - self.get_credit(pair)

    def get_credit(self, pair: List):
        option1 = pair[0]
        option2 = pair[1]
        return float(option2.get_price()) - float(option1.get_price())

    def get_loss_win_ratio(self, pair):
        return self.default_loss_win_ratio(pair)


class BullCallSpread(Strategy):
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
            option1.position = OptionPosition.LONG
            for num2 in option_index:
                if num2 > num:
                    option2 = self.call_options[num2]
                    option2.position = OptionPosition.SHORT
                    pairs.append([copy.copy(option1), copy.copy(option2)])
        return pairs

    def get_even_price(self, pair: List):
        option1 = pair[0]
        option2 = pair[1]
        return float(option1.strike) - self.get_credit(pair)

    def get_max_win(self, pair: List):
        option1 = pair[0]
        option2 = pair[1]
        return float(option2.strike) - float(option1.strike) - self.get_credit(pair)

    def get_max_loss(self, pair: List):
        return abs(self.get_credit(pair))

    def get_credit(self, pair: List):
        option1 = pair[0]
        option2 = pair[1]
        return float(option2.get_price()) - float(option1.get_price())

    def get_loss_win_ratio(self, pair):
        return self.default_loss_win_ratio(pair)


# SyntheticLong('CNC', '202001').analyze()
# BullCallSpread('CNC', '202001').analyze()
# code_input = sys.argv[1]
# month_input = sys.argv[2]
# bullish(code_input, month_input)
