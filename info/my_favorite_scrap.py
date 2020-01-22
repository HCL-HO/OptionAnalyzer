import util.common as Common
import model.StockDTO as Stock
import Util
import util.stock as Get_Stock
import os

# from Util import open_site_custom, print_class

fav_file = os.path.abspath("favorites.txt")


def intercept_input(input) -> bool:
    if input.lower().startswith('a '):
        codes = Common.load_array_from_file(fav_file, '\n')
        value = input[2:]
        codes.append(value)
        Common.write_output_to_file('\n'.join(str(x) for x in codes), fav_file)
        return True
    elif input.lower().startswith('d '):
        codes = Common.load_array_from_file(fav_file, '\n')
        value = input[2:]
        codes.remove(value)
        Common.write_output_to_file('\n'.join(str(x) for x in codes), fav_file)
        return True
    elif input.lower().startswith('r'):
        return True
    else:
        return False


def listen_to_selection(result: dict, back_func):
    print('Select stock: ')
    print('D to delete ')
    print('A to add ')
    print('R to refresh ')
    # print('Enter X to quit: ')
    selected_stock = input()
    if not selected_stock:
        print('Exit')
        back_func()
        return
    if intercept_input(selected_stock):
        show_favorite(back_func)
        return
    stock = result.get(selected_stock)
    if not stock:
        print('Try again')
        listen_to_selection(result, back_func)
    else:
        Util.print_class(stock)
        print('Enter X to quit: ')
        print('Press Enter to back: ')
        command = input()
        if command.lower() == 'x':
            print('Exit')
            back_func()
        else:
            show_favorite(back_func)


def print_stocks(result):
    indent = '          '
    for code, stock in result.items():
        print('====================================================================================================')
        print(code)
        print('====================================================================================================')
        print(indent + stock.price)
        print(indent + stock.chg)


def show_favorite(func):
    codes = Common.load_array_from_file(fav_file, '\n')
    result = {}
    for code in codes:
        stock = Get_Stock.get_stock(code)
        result[code] = stock
    print_stocks(result)
    listen_to_selection(result, func)
    #     result[code] = get_stock(code)
    # print_class(result)

# show_favorite()
# print(low)
