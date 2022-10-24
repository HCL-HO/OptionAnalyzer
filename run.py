from bearish import *
from bullish import bullish
from index_scrap import show_hsi
from stagnant import stagnant
from volatile import volatile
from show_options import show_options

# code = 'CLK'
code = 'TCH'
# code = 'HKB'
# code = 'MET'
# code = 'SAN'
# code = 'CNC'
# code = 'BYD'
month = '202112'
# month = '201907'bear_put_spread

# volatile(code, month)
# show_options(code, month)
# show_options(code, month)
# show_hsi()
# bearish(code, month)
# stagnant(code, month)
# bearish(code, month)
# bearish(code, month)
print(bearish_out(code, month))
