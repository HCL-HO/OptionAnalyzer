from analyze import *


def bullish(code, month):
    bull_call_spread(code, month)
    bull_put_spread(code, month)
    synthetic_long_stock(code, month)


# code_input = sys.argv[1]
# month_input = sys.argv[2]
# bullish(code_input, month_input)
