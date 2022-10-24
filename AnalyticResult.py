import OptionDTO


class AnalyticResult():
    def __init__(self, options: list[OptionDTO] = [], premium: str = "", breakeven: str = "", maximum_win: str = "",
                 maximum_loss: str = ""):
        self.options = options
        self.premium = premium
        self.breakeven = breakeven
        self.maximum_win = maximum_win
        self.maximum_loss = maximum_loss

    def print(self):
        result = ''
        for option in self.options:
            # result = result + option.position.value + ' ' + option.m_type.value
            result = result + option.__str__() + '\n'
        result = result + 'premium: ' + str(self.premium) + '\n'
        result = result + 'even price: ' + str(self.breakeven) + '\n'
        # result = result + 'win at: ' + str(self.win_at) + '\n'
        result = result + 'max_loss: ' + str(self.maximum_loss) + '\n'
        result = result + 'max_win: ' + str(self.maximum_win) + '\n'
        # result = result + 'max_loss_to_max_win: ' + str(self.max_loss_to_max_win) + '\n'
        result = result + '\n---------------------------------------------------------------------------' + '\n'
        result = result + '\n'
        print(result)
