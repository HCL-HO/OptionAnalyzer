from analyze import *


def volatile(code, month):
    short_call_calendar_spread(code, month)
    short_put_calendar_spread(code, month)
    long_straddle(code, month)
    long_strangle(code, month)

# code_input = sys.argv[1]
# month_input = sys.argv[2]
# volatile(code_input, month_input)
