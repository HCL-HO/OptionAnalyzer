from analyze import *


def bearish(code, month):
    bear_put_spread(code, month)
    bear_call_spread(code, month)
    synthetic_short_stock(code, month)


# code_input = sys.argv[1]
# month_input = sys.argv[2]
# bearish(code_input, month_input)
