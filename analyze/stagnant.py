from analyze import *
import sys


def stagnant(code, month):
    long_call_calendar_spread(code, month)
    long_put_calendar_spread(code, month)
    short_straddle(code, month)
    short_strangle(code, month)
    short_call_w_asset(code, month)


# code_input = sys.argv[1]
# month_input = sys.argv[2]
# stagnant(code_input, month_input)
