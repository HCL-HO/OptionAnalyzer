import util.common as Common
import model.StockDTO as Stock
import Util
import util.stock as Get_Stock
import logbook.CRUD as Logbook
from datetime import date
import os


def is_float(number):
    try:
        float(number)
        return True
    except ValueError:
        return False


##TODO add entry
def show_add_menu(back_func):
    valid_code = False
    valid_qy = False
    valid_price = False
    code = ''
    qy = ''
    price = ''
    while not valid_code:
        print('Enter Code Number: ')
        code = input()
        if code.isdigit():
            valid_code = True
    while not valid_qy:
        print('Enter quantity: ')
        qy = input()
        if qy.isdigit():
            valid_qy = True
    while not valid_price:
        print('Enter price: ')
        price = input()
        if is_float(price):
            valid_price = True
    Logbook.add_stock(code, price, qy)
    show_holdings(back_func)


def show_del_menu(back_func):
    valid_code = False
    valid_index = False
    code = ''
    index = ''
    while not valid_code:
        print('Enter Code Number: ')
        code = input()
        if code.isdigit():
            valid_code = True
    while not valid_index:
        print('Enter index: ')
        index = input()
        if index.isdigit():
            valid_index = True
    if Logbook.del_stock(code, index):
        show_holdings(back_func)
    else:
        print('Delete Failed')


def listen_to_selection(back_func):
    print('D to delete ')
    print('A to add ')
    print('R to refresh ')
    command = input()
    if command.upper() == "A":
        show_add_menu(back_func)
    elif command.upper() == "D":
        show_del_menu(back_func)
    elif command.upper() == "R":
        show_holdings(back_func)
    elif command == "":
        back_func()
    else:
        print("Please check your input")


def print_stocks(code, result):
    stock = Get_Stock.get_stock(code)
    print(code)
    print('====================================================================================================')
    indent = '          '
    for record in result:
        net_gain = (float(stock.price) - float(record[Logbook.CODE_PRICE])) * float(record[Logbook.CODE_QY])
        print(str(record) + '| net gain: ' + str(net_gain))
        # print(indent + stock.price)
        # print(indent + stock.chg)
    stock.print()
    print('====================================================================================================')


def show_holdings(func):
    stocks = Logbook.stock_json
    print(stocks)
    for code in stocks:
        print_stocks(code, stocks[code])
    listen_to_selection(func)
    #     result[code] = get_stock(code)
    # print_class(result)

# show_holdings()
# show_add_menu()
# show_favorite()
# print(low)
