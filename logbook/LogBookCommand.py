from typing import Optional

from StrategyMap import StrategyMap
from Strategy import Strategy
from scrap import scrap
from CRUD import *


def entry():
    strategy_cls = input_strategy()
    while strategy_cls is None:
        strategy_cls = input_strategy()
    print('Enter Code: ')
    code = input()
    while code is None:
        code = input()
    print('Enter Month: ')
    month = input()
    while month is None:
        month = input()
    strategy = strategy_cls(code, month)
    pairs = strategy.get_pairs()
    if len(pairs) > 0:
        print('Select Options')
        for i, pair in enumerate(pairs):
            # print(pair)
            print(str(i+1) + '\n' + strategy.get_analytic_str(pair))

        options = input()
        while options is None:
            options = input()

        pair = pairs[int(options) - 1]
        add_option_strategy(code, pair, strategy.__class__.__name__)


# Option(None, None, 'price', None, None, 'strike', OptionType.CALL, OptionPosition.SHORT)

def input_strategy() :
    print('Select Strategy: ')
    key_names = list(StrategyMap.keys())
    key_names_str = ''
    for i in range(len(key_names)):
        key_names_str = key_names_str + str(i) + ': ' + key_names[i] + ', '
    print(key_names_str)
    selection = input()
    try:
        strategy = StrategyMap[key_names[int(selection)]]
    except ValueError:
        return None
    return strategy
    # print(strategy)


def get_put_options(code: str, month: str) -> List[Option]:
    data = scrap(code, month)
    return data['option']['put']


def get_call_options(code: str, month: str) -> List[Option]:
    data = scrap(code, month)
    return data['option']['call']


entry()
