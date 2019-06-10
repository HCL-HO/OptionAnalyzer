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
    options = scrap(code, month)
    call_options = options['call']

    # TODO loop to analyse
    for option in call_options:
        break
    # loss_at_stock_price = stock_price - call_option[TAG_PRICE]
    loss_max = VAL_UNLIMIT
    even_price = stock_price - call_option[TAG_PRICE]
    execute_at = call_option[TAG_STRIKEPRICE]
    win_max = call_option[TAG_PRICE]
    print('stock_price: ' + str(stock_price))
    print('call_option: ' + str(call_option))
    print('even price: ' + str(even_price))
    print('win at: > ' + str(even_price))
    print('max_loss: ' + str(loss_max))
    print('max_win: ' + str(win_max))
    print('execute_at: > ' + str(execute_at))
    print('\n')


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


short_put_spread()

short_call_spread()

short_call_w_asset()
