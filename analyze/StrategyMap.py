from bearish import *
from stagnant import *
from volatile import *
from bullish import *

StrategyMap = {
    'ShortCallCalendarSpread': ShortCallCalendarSpread,
    'ShortPutCalendarSpread': ShortPutCalendarSpread,
    'LongStangle': LongStangle,
    'LongStraddle': LongStraddle,
    'BullCallSpread': BullCallSpread,
    'BullPutSpread': BullPutSpread,
    'SyntheticLong': SyntheticLong,
    'LongCallCalendarSpread': LongCallCalendarSpread,
    'LongPutCalendarSpread': LongPutCalendarSpread,
    'ShortStraddle': LongPutCalendarSpread,
    'ShortStrangle': ShortStrangle
}
