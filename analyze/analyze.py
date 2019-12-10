from typing import List

from scrap import scrap
from Util import *
from OptionDTO import *

config = {
    'info': True
}

TAG_STRIKEPRICE = 'strike_price'
TAG_PRICE = 'price'
VAL_UNLIMIT = 'unlimited'


def print_result(options: List[Option], premium: str, even_price: str, win_at: str, max_loss: str, max_win: str,
                 max_loss_to_max_win: str):
    for option in options:
        print(option.position.value + ' ' + option.m_type.value)
        print(option)
    print('premium: ' + str(premium))
    print('even price: ' + str(even_price))
    print('win at: ' + str(win_at))
    print('max_loss: ' + str(max_loss))
    print('max_win: ' + str(max_win))
    print('max_loss_to_max_win: ' + max_loss_to_max_win)
    print('\n---------------------------------------------------------------------------')
    print('\n')


def short_call_w_asset(code, month):
    result = scrap(code, month)
    call_options = result['option']['call']
    stock = result['stock']
    print('stock_price: ' + str(stock.price))
    print('\n---------------------------------------------------------------------------')
    for option in call_options:
        if option.get_price() == '':
            continue
        # loss_at_stock_price = stock_price - call_option[TAG_PRICE]
        loss_max = VAL_UNLIMIT
        premium = (float(stock.price) - float(option.strike))
        even_price = float(stock.price) - float(option.get_price())
        execute_at = option.strike
        win_max = float(option.get_price()) - (float(stock.price) - float(option.strike))
        print('execute_at: > ' + str(execute_at))
        print_result(option, str(premium), str(even_price), str(even_price), loss_max, str(win_max), VAL_UNLIMIT)


def bear_call_spread(code, month):
    result = scrap(code, month)
    call_options = result['option']['call']
    stock = result['stock']
    print('stock_price: ' + str(stock.price))
    print('bear_call_spread')
    print('\n---------------------------------------------------------------------------')
    option_index = []
    for num in range(len(call_options)):
        if call_options[num].get_price() == '':
            continue
        option_index.append(num)

    for num in option_index:
        option1 = call_options[num]
        option1.position = OptionPosition.SHORT
        for num2 in option_index:
            if num2 > num:
                option2 = call_options[num2]
                option2.position = OptionPosition.LONG
                premium = float(option1.get_price()) - float(option2.get_price())
                loss_max = float(option2.strike) - float(option1.strike) - premium
                even_price = float(option1.strike) + premium
                # execute_at = call_option[TAG_STRIKEPRICE]
                win_max = premium
                options = [option1, option2]
                print_result(options, str(premium), str(even_price), str(-even_price), str(loss_max), str(win_max),
                             str(loss_max / win_max))


def bull_call_spread(code, month):
    result = scrap(code, month)
    call_options = result['option']['call']
    stock = result['stock']
    print('stock_price: ' + str(stock.price))
    print('\n---------------------------------------------------------------------------')
    option_index = []
    for num in range(len(call_options)):
        if call_options[num].get_price() == '':
            continue
        option_index.append(num)

    for num in option_index:
        option1 = call_options[num]
        option1.position = OptionPosition.LONG
        for num2 in option_index:
            if num2 > num:
                option2 = call_options[num2]
                option2.position = OptionPosition.SHORT
                premium = float(option1.get_price()) - float(option2.get_price())
                loss_max = premium
                even_price = float(option1.strike) + float(option1.get_price()) - float(option2.get_price())
                # execute_at = call_option[TAG_STRIKEPRICE]
                win_max = float(option2.strike) - float(option1.strike) - premium
                options = [option1, option2]
                print_result(options, str(premium), str(even_price), str(even_price), str(loss_max), str(win_max),
                             str(loss_max / win_max))


def bull_put_spread(code, month):
    result = scrap(code, month)
    put_options = result['option']['put']
    stock = result['stock']
    print('stock_price: ' + str(stock.price))
    print('\n---------------------------------------------------------------------------')
    option_index = []
    for num in range(len(put_options)):
        if put_options[num].get_price() == '':
            continue
        option_index.append(num)
    for num in option_index:
        option1 = put_options[num]
        option1.position = OptionPosition.LONG
        for num2 in option_index:
            if num2 > num:
                option2 = put_options[num2]
                option2.position = OptionPosition.SHORT
                loss_max = float(option2.strike) - float(option1.strike) - float(option1.get_price())
                even_price = float(option2.strike) - float(option2.get_price()) + float(option1.get_price())
                # execute_at = call_option[TAG_STRIKEPRICE]
                win_max = float(option2.get_price()) - float(option1.get_price())
                options = [option1, option2]
                print_result(options, str('N/A'), str(even_price), str(even_price), str(loss_max), str(win_max),
                             str(loss_max / win_max))


def bear_put_spread(code, month):
    result = scrap(code, month)
    put_options = result['option']['put']
    stock = result['stock']
    print('bear_put_spread')
    print('stock_price: ' + str(stock.price))
    print('\n---------------------------------------------------------------------------')
    option_index = []
    for num in range(len(put_options)):
        if put_options[num].get_price() == '':
            continue
        option_index.append(num)
    for num in option_index:
        option1 = put_options[num]
        option1.position = OptionPosition.SHORT
        for num2 in option_index:
            if num2 > num:
                option2 = put_options[num2]
                option2.position = OptionPosition.LONG
                premium = float(option2.get_price()) - float(option1.get_price())
                loss_max = premium
                even_price = float(option2.strike) - premium
                options = [option1, option2]
                # execute_at = call_option[TAG_STRIKEPRICE]
                win_max = float(option2.strike) - float(option1.strike) - premium
                print_result(options, str(premium), str(even_price), str(-even_price), str(loss_max), str(win_max),
                             str(loss_max / win_max))


def synthetic_long_stock(code, month):
    result = scrap(code, month)
    put_options = result['option']['put']
    call_options = result['option']['call']
    stock = result['stock']
    print('stock_price: ' + str(stock.price))
    print('\n---------------------------------------------------------------------------')
    for call in call_options:
        if call.get_price() != '':
            for put in put_options:
                if put.get_price() != '':
                    if put.strike == call.strike:
                        premium = float(call.get_price()) - float(put.get_price())
                        even_price = float(call.strike) + float(premium)
                        loss_max = 'any below ' + str(even_price)
                        win_max = 'any above ' + str(even_price)
                        call.position = OptionPosition.LONG
                        put.position = OptionPosition.SHORT
                        options = [call, put]
                        print_result(options, str(premium), str(even_price), str(even_price), str(loss_max),
                                     str(win_max),
                                     str('N/A'))


def synthetic_short_stock(code, month):
    result = scrap(code, month)
    put_options = result['option']['put']
    call_options = result['option']['call']
    stock = result['stock']
    print('synthetic_short_stock')
    print('stock_price: ' + str(stock.price))
    print('\n---------------------------------------------------------------------------')
    for call in call_options:
        if call.get_price() != '':
            for put in put_options:
                if put.get_price() != '':
                    if put.strike == call.strike:
                        premium = float(put.get_price()) - float(call.get_price())
                        even_price = float(put.strike) - float(premium)
                        loss_max = 'any above ' + str(even_price)
                        win_max = 'any below ' + str(even_price)
                        call.position = OptionPosition.SHORT
                        put.position = OptionPosition.LONG
                        options = [call, put]
                        print_result(options, str(premium), str(even_price), str(-even_price), str(loss_max),
                                     str(win_max),
                                     str('N/A'))


def get_month(month, param):
    old_month = month[4:]
    old_year = month[:4]
    new_month = int(old_month) + param
    new_year = int(old_year)
    if new_month >= 13:
        new_month = new_month - 12
        new_year += 1
    return str(new_year) + "{:02d}".format(new_month)


# stagnant

def long_put_calendar_spread(code, month):
    month1 = get_month(month, 1)
    month2 = get_month(month, 2)
    result0 = scrap(code, month)
    result1 = scrap(code, month1)
    result2 = scrap(code, month2)
    puts0 = result0['option']['put']
    puts1 = result1['option']['put']
    puts2 = result2['option']['put']
    stock = result0['stock']
    print('long_put_calendar_spread')
    print('stock_price: ' + str(stock.price))
    # print('\n---------------------------------------------------------------------------')
    #
    for put in puts0:
        if put.get_price() != '':
            for put1 in puts1:
                if put1.get_price() != '' and put1.strike == put.strike:
                    long_put_calendar_spread_print(put, put1, month, month1)
            for put2 in puts2:
                if put2.get_price() != '' and put2.strike == put.strike:
                    long_put_calendar_spread_print(put, put2, month, month2)


def long_put_calendar_spread_print(put, put1, month, month1):
    print('Maximum when the stock price is at strike price on the nearby expiry date\n')
    premium = float(put1.get_price()) - float(put.get_price())
    loss_max = 'Time decay (Short put) - time decay (Long put)'
    win_max = premium
    print('long put : ' + month + ': ' + str(put))
    print('short put: ' + month1 + ': ' + str(put1))
    print('premium: ' + str(premium))
    print('max_loss: ' + str(loss_max))
    print('max_win: ' + str(win_max))
    print('\n')


def long_call_calendar_spread(code, month):
    month1 = get_month(month, 1)
    month2 = get_month(month, 2)
    result0 = scrap(code, month)
    result1 = scrap(code, month1)
    result2 = scrap(code, month2)
    calls0 = result0['option']['call']
    calls1 = result1['option']['call']
    calls2 = result2['option']['call']

    stock = result0['stock']
    print('long_call_calendar_spread')
    print('stock_price: ' + str(stock.price))
    print('\n---------------------------------------------------------------------------')
    for call in calls0:
        if call.get_price() != '':
            for call1 in calls1:
                if call1.get_price() != '' and call1.strike == call.strike:
                    long_call_calendar_spread_print(call, call1, month, month1)
            for call2 in calls2:
                if call2.get_price() != '' and call2.strike == call.strike:
                    long_call_calendar_spread_print(call, call2, month, month2)


def long_call_calendar_spread_print(call, call1, month, month1):
    print('Maximum when the stock price is at strike price on the nearby expiry date\n')
    premium = float(call1.get_price()) - float(call.get_price())
    loss_max = premium
    win_max = 'Time decay (Short call) - time decay (Long call)'
    print('short call : ' + month + ': ' + str(call))
    print('long call: ' + month1 + ': ' + str(call1))
    print('premium: ' + str(premium))
    print('max_loss: ' + str(loss_max))
    print('max_win: ' + str(win_max))
    print('\n')


def short_straddle(code, month):
    result = scrap(code, month)
    calls = result['option']['call']
    puts = result['option']['put']

    stock = result['stock']
    print('short_straddle')
    print('stock_price: ' + str(stock.price))
    print('\n---------------------------------------------------------------------------')

    for call in calls:
        if call.get_price() != '':
            for put in puts:
                if put.get_price() != '' and call.strike == put.strike:
                    premium = float(call.get_price()) + float(put.get_price())
                    win_max = premium
                    lower_limit = float(call.strike) - float(premium)
                    upper_limit = float(call.strike) + float(premium)
                    even_price = str(lower_limit) + ' to ' + str(upper_limit)
                    loss_max = 'any below: ' + str(lower_limit) + ' and any above: ' + str(upper_limit)
                    print('short call : ' + str(call))
                    print('short put: ' + str(put))
                    print('premium: ' + str(premium))
                    print('break even: ' + str(even_price))
                    print('max_loss: ' + str(loss_max))
                    print('max_win: ' + str(win_max))
                    print('\n')


def short_strangle(code, month):
    result = scrap(code, month)
    calls = result['option']['call']
    puts = result['option']['put']

    stock = result['stock']
    print('short_strangle')
    print('stock_price: ' + str(stock.price))
    print('\n---------------------------------------------------------------------------')

    for call in calls:
        if call.get_price() != '':
            for put in puts:
                if put.get_price() != '' and call.strike > put.strike:
                    premium = float(call.get_price()) + float(put.get_price())
                    win_max = premium
                    lower_limit = float(put.strike) - float(premium)
                    upper_limit = float(call.strike) + float(premium)
                    even_price = str(lower_limit) + ' to ' + str(upper_limit)
                    loss_max = 'any below: ' + str(lower_limit) + ' and any above: ' + str(upper_limit)
                    print('short call : ' + str(call))
                    print('short put: ' + str(put))
                    print('premium: ' + str(premium))
                    print('break even: ' + str(even_price))
                    print('max_loss: ' + str(loss_max))
                    print('max_win: ' + str(win_max))
                    print('\n')


# volatile
def short_call_calendar_spread(code, month):
    month1 = get_month(month, 1)
    month2 = get_month(month, 2)
    result0 = scrap(code, month)
    result1 = scrap(code, month1)
    result2 = scrap(code, month2)
    calls0 = result0['option']['call']
    calls1 = result1['option']['call']
    calls2 = result2['option']['call']

    stock = result0['stock']
    print('short_call_calendar_spread')
    print('stock_price: ' + str(stock.price))
    print('\n---------------------------------------------------------------------------')

    print('Stock price is further away from strike price on the nearby expiry date\n')
    for call in calls0:
        if call.get_price() != '':
            for call1 in calls1:
                if call1.get_price() != '' and call1.strike == call.strike:
                    short_call_calendar_spread_print(call, call1, month, month1)
            for call2 in calls2:
                if call2.get_price() != '' and call2.strike == call.strike:
                    short_call_calendar_spread_print(call, call2, month, month2)


def short_call_calendar_spread_print(call, call1, month, month1):
    premium = float(call1.get_price()) - float(call.get_price())
    win_max = premium
    loss_max = 'Time decay (Short call) - time decay (Long call)'
    print('long call : ' + month + ': ' + str(call))
    print('short call: ' + month1 + ': ' + str(call1))
    print('premium: ' + str(premium))
    print('max_loss: ' + str(loss_max))
    print('max_win: ' + str(win_max))
    print('\n')


def short_put_calendar_spread(code, month):
    month1 = get_month(month, 1)
    month2 = get_month(month, 2)
    result0 = scrap(code, month)
    result1 = scrap(code, month1)
    result2 = scrap(code, month2)
    puts0 = result0['option']['put']
    puts1 = result1['option']['put']
    puts2 = result2['option']['put']

    stock = result0['stock']
    print('short_put_calendar_spread')
    print('stock_price: ' + str(stock.price))
    print('\n---------------------------------------------------------------------------')

    print('Maximum when the stock price is further away from strike price on the nearby expiry date\n')
    for put in puts0:
        if put.get_price() != '':
            for put1 in puts1:
                if put1.get_price() != '' and put1.strike == put.strike:
                    long_put_calendar_spread_print(put, put1, month, month1)
            for put2 in puts2:
                if put2.get_price() != '' and put2.strike == put.strike:
                    long_put_calendar_spread_print(put, put2, month, month2)


def short_put_calendar_spread_print(put, put1, month, month1):
    premium = float(put1.get_price()) - float(put.get_price())
    win_max = premium
    loss_max = 'Time decay (Short put) - time decay (Long put)'
    print('long put : ' + month + ': ' + str(put))
    print('short put: ' + month1 + ': ' + str(put1))
    print('premium: ' + str(premium))
    print('max_loss: ' + str(loss_max))
    print('max_win: ' + str(win_max))
    print('\n')


def long_straddle(code, month):
    result = scrap(code, month)
    puts = result['option']['put']
    calls = result['option']['call']

    stock = result['stock']
    print('long_straddle')
    print('stock_price: ' + str(stock.price))
    print('\n---------------------------------------------------------------------------')

    for call in calls:
        if call.get_price() != '':
            for put in puts:
                if put.get_price() != '' and call.strike == put.strike:
                    premium = float(call.get_price()) + float(put.get_price())
                    lower_limit = float(call.strike) - float(premium)
                    upper_limit = float(call.strike) + float(premium)
                    even_price = str(lower_limit) + ' to ' + str(upper_limit)
                    win_max = 'any below: ' + str(lower_limit) + ' and any above: ' + str(upper_limit)
                    loss_max = premium
                    # print('long call : ' + str(call))
                    # print('long put: ' + str(put))
                    # print('premium: ' + str(premium))
                    # print('break even: ' + str(even_price))
                    # print('max_loss: ' + str(loss_max))
                    # print('max_win: ' + str(win_max))
                    # print('\n')
                    call.position = OptionPosition.LONG
                    put.position = OptionPosition.LONG
                    options = [call, put]
                    print_result(options, str(premium), str(even_price), str(even_price), str(loss_max),
                                 str(win_max),
                                 str('N/A'))


def long_strangle(code, month):
    result = scrap(code, month)
    calls = result['option']['call']
    puts = result['option']['put']

    stock = result['stock']
    print('long_strangle')
    print('stock_price: ' + str(stock.price))
    print('\n---------------------------------------------------------------------------')

    for call in calls:
        if call.get_price() != '':
            for put in puts:
                if put.get_price() != '' and call.strike > put.strike:
                    premium = float(call.get_price()) + float(put.get_price())
                    lower_limit = float(put.strike) - float(premium)
                    upper_limit = float(call.strike) + float(premium)
                    even_price = str(lower_limit) + ' to ' + str(upper_limit)
                    win_max = 'any below: ' + str(lower_limit) + ' and any above: ' + str(upper_limit)
                    loss_max = premium
                    call.position = OptionPosition.LONG
                    put.position = OptionPosition.LONG
                    options = [call, put]
                    print_result(options, str(premium), str(even_price), str(even_price), str(loss_max),
                                 str(win_max),
                                 str('N/A'))

    # bear_put_spread('CNC', '201906')
    # bull_put_spread('CNC', '201906')
    # bull_call_spread('CNC', '201906')
    # synthetic_long_stock('CNC', '201906')
    # synthetic_short_stock('CNC', '201906')
    # long_call_calendar_spread('CNC', '201906')
    # short_call_calendar_spread('CNC', '201906')
    # long_put_calendar_spread('CNC', '201906')
    # short_put_calendar_spread('CNC', '201906')
    # short_straddle('CNC', '201906')
    # short_strangle('CNC', '201906')
    # short_call_w_asset('CNC', '201906')
    # long_straddle('CNC', '201906')
    # long_strangle('CNC', '201906')
