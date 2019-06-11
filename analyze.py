from scrap import scrap

TAG_STRIKEPRICE = 'strike_price'
TAG_PRICE = 'price'

VAL_UNLIMIT = 'unlimited'

stock_price = 13.5
call_option = {
    TAG_STRIKEPRICE: 13,
    TAG_PRICE: 0.4
}
call_option2 = {
    TAG_STRIKEPRICE: 14,
    TAG_PRICE: 0.1
}
put_option2 = {
    TAG_STRIKEPRICE: 14,
    TAG_PRICE: 0.7
}
put_option = {
    TAG_STRIKEPRICE: 13,
    TAG_PRICE: 0.2
}


def short_call_w_asset(code, month):
    result = scrap(code, month)
    call_options = result['option']['call']
    stock = result['stock']
    print('stock_price: ' + str(stock.price))
    print('\n---------------------------------------------------------------------------')
    for option in call_options:
        if option.last == '':
            continue
        # loss_at_stock_price = stock_price - call_option[TAG_PRICE]
        loss_max = VAL_UNLIMIT
        even_price = float(stock.price) - float(option.last)
        execute_at = option.strike
        win_max = float(option.last)
        print('call_option: ' + str(option))
        print('even price: ' + str(even_price))
        print('win at: > ' + str(even_price))
        print('max_loss: ' + str(loss_max))
        print('max_win: ' + str(win_max))
        print('execute_at: > ' + str(execute_at))
        print('\n---------------------------------------------------------------------------')


def short_call_spread():
    loss_max = call_option2[TAG_STRIKEPRICE] - call_option[TAG_STRIKEPRICE] + call_option[TAG_PRICE]
    even_price = call_option[TAG_STRIKEPRICE] - call_option2[TAG_PRICE] + call_option[TAG_PRICE]
    # execute_at = call_option[TAG_STRIKEPRICE]
    win_max = call_option[TAG_PRICE] - call_option2[TAG_PRICE]
    print('stock_price: ' + str(stock_price))
    print('short call_option: ' + str(call_option))
    print('long call_option: ' + str(call_option2))
    print('even price: ' + str(even_price))
    print('win at: < ' + str(even_price))
    print('max_loss: ' + str(loss_max))
    print('max_win: ' + str(win_max))
    print('max_loss_to_max_win: ' + str(loss_max / win_max))
    # print('execute_at: > ' + str(execute_at))
    print('\n')


def short_put_spread():
    loss_max = put_option2[TAG_STRIKEPRICE] - put_option[TAG_STRIKEPRICE] + put_option2[TAG_PRICE]
    even_price = put_option2[TAG_STRIKEPRICE] - put_option2[TAG_PRICE] + put_option[TAG_PRICE]
    # execute_at = call_option[TAG_STRIKEPRICE]
    win_max = put_option2[TAG_PRICE] - put_option[TAG_PRICE]
    print('stock_price: ' + str(stock_price))
    print('short put_option: ' + str(put_option))
    print('long put_option: ' + str(put_option2))
    print('even price: ' + str(even_price))
    print('win at: > ' + str(even_price))
    print('max_loss: ' + str(loss_max))
    print('max_win: ' + str(win_max))
    print('max_loss_to_max_win: ' + str(loss_max / win_max))
    print('\n')


# short_put_spread()
#
# short_call_spread()

short_call_w_asset('CNC', '201906')
