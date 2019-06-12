from scrap import scrap
from Util import *

config = {
    'info': True
}

TAG_STRIKEPRICE = 'strike_price'
TAG_PRICE = 'price'

VAL_UNLIMIT = 'unlimited'


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
        even_price = float(stock.price) - float(option.get_price())
        execute_at = option.strike
        win_max = float(option.get_price())
        print('call_option: ' + str(option))
        print('even price: ' + str(even_price))
        print('win at: > ' + str(even_price))
        print('max_loss: ' + str(loss_max))
        print('max_win: ' + str(win_max))
        print('execute_at: > ' + str(execute_at))
        print('\n---------------------------------------------------------------------------')


def bear_call_spread(code, month):
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
        for num2 in option_index:
            if num2 > num:
                option2 = call_options[num2]
                loss_max = float(option2.strike) - float(option1.strike) - float(option2.get_price())
                even_price = float(option1.strike) + float(option1.get_price()) - float(option2.get_price())
                # execute_at = call_option[TAG_STRIKEPRICE]
                win_max = float(option1.get_price()) - float(option2.get_price())
                print('short call_option: ' + str(option1))
                print('long call_option: ' + str(option2))
                print('even price: ' + str(even_price))
                print('win at: < ' + str(even_price))
                print('max_loss: ' + str(loss_max))
                print('max_win: ' + str(win_max))
                try:
                    print('max_loss_to_max_win: ' + str(loss_max / win_max))
                except ZeroDivisionError:
                    print('no chance to win')
                # print('execute_at: > ' + str(execute_at))
                print('\n')


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
        for num2 in option_index:
            if num2 > num:
                option2 = call_options[num2]
                premium = float(option1.get_price()) - float(option2.get_price())
                loss_max = premium
                even_price = float(option1.strike) + float(option1.get_price()) - float(option2.get_price())
                # execute_at = call_option[TAG_STRIKEPRICE]
                win_max = float(option2.strike) - float(option1.strike) - premium
                print('short call_option: ' + str(option2))
                print('long call_option: ' + str(option1))
                print('even price: ' + str(even_price))
                print('win at: > ' + str(even_price))
                print('premium: ' + str(premium))
                print('max_loss: ' + str(loss_max))
                print('max_win: ' + str(win_max))
                try:
                    print('max_loss_to_max_win: ' + str(loss_max / win_max))
                except ZeroDivisionError:
                    print('no chance to win')
                # print('execute_at: > ' + str(execute_at))
                print('\n')


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
        for num2 in option_index:
            if num2 > num:
                option2 = put_options[num2]
                loss_max = float(option2.strike) - float(option1.strike) - float(option1.get_price())
                even_price = float(option2.strike) - float(option2.get_price()) + float(option1.get_price())
                # execute_at = call_option[TAG_STRIKEPRICE]
                win_max = float(option2.get_price()) - float(option1.get_price())
                print('short put_option: ' + str(option2))
                print('long put_option: ' + str(option1))
                print('even price: ' + str(even_price))
                print('win at: > ' + str(even_price))
                print('max_loss: ' + str(loss_max))
                print('max_win: ' + str(win_max))
                try:
                    print('max_loss_to_max_win: ' + str(loss_max / win_max))
                except ZeroDivisionError:
                    print('no chance to win')
                print('\n')


def bear_put_spread(code, month):
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
        for num2 in option_index:
            if num2 > num:
                option2 = put_options[num2]
                loss_max = float(option2.get_price()) - float(option1.get_price())
                even_price = float(option2.strike) - float(option2.get_price()) + float(option1.get_price())
                # execute_at = call_option[TAG_STRIKEPRICE]
                win_max = float(option2.strike) - float(option1.strike) - float(option2.get_price()) + float(
                    option1.get_price())
                print('short put_option: ' + str(option1))
                print('long put_option: ' + str(option2))
                print('even price: ' + str(even_price))
                print('win at: < ' + str(even_price))
                print('max_loss: ' + str(loss_max))
                print('max_win: ' + str(win_max))
                try:
                    print('max_loss_to_max_win: ' + str(loss_max / win_max))
                except ZeroDivisionError:
                    print('no chance to win')
                print('\n')


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
                        print('long call: ' + str(call))
                        print('short put: ' + str(put))
                        print('premium: ' + str(premium))
                        print('even price: ' + str(even_price))
                        print('win at: > ' + str(even_price))
                        print('max_loss: ' + str(loss_max))
                        print('max_win: ' + str(win_max))
                        print('\n')


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
                        print('short call: ' + str(call))
                        print('long put: ' + str(put))
                        print('premium: ' + str(premium))
                        print('even price: ' + str(even_price))
                        print('win at: < ' + str(even_price))
                        print('max_loss: ' + str(loss_max))
                        print('max_win: ' + str(win_max))
                        print('\n')


# bear_put_spread('CNC', '201906')
# bull_put_spread('CNC', '201906')
# bull_call_spread('CNC', '201906')
# synthetic_long_stock('CNC', '201906')
synthetic_short_stock('CNC', '201906')
