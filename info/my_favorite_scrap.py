import util.common as Common
import model.StockDTO as Stock
import Util
import argparse

# from Util import open_site_custom, print_class

url = 'http://www.etnet.com.hk/www/tc/stocks/realtime/quote.php?code=$CODE'
referer = 'http://www.etnet.com.hk/www/tc/stocks/realtime/'
CODE_REPLACE = '$CODE'
fav_file = 'C:\\workspace\\programs\\OptionAnalyzer\\favorites.txt'


def get_stock(code):
    if code == '':
        return None
    m_url = url.replace(CODE_REPLACE, code)
    body = Util.open_site_custom(m_url, header={'User-Agent': 'Mozilla/5.0',
                                                'Referer': referer})
    container = body.find(id='StkDetailMainBox')
    trs = container.find_all('tr')
    row1 = trs[0]
    row1_tds = row1.find_all('td')
    price = row1_tds[0].find_all('span')[0].text
    change = row1_tds[0].find_all('span')[1].text
    high = row1_tds[1].find_all('span')[1].text
    turnover = row1_tds[2].find_all('span')[1].text
    m_high = row1_tds[4].find('span').text
    row2 = trs[1]
    row2_tds = row2.find_all('td')
    low = row2_tds[1].find_all('span')[1].text
    m_low = row2_tds[4].find('span').text
    stock = Stock.Stock(price, high, low, turnover, change, m_high, m_low)
    return stock


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


def listen_to_selection(result: dict):
    print('Select stock: ')
    print('D to delete ')
    print('A to add ')
    print('R to refresh ')
    # print('Enter X to quit: ')
    selected_stock = input()
    if not selected_stock:
        print('Exit')
        exit()
    if intercept_input(selected_stock):
        show_favorite()
        return
    stock = result.get(selected_stock)
    if not stock:
        print('Try again')
        listen_to_selection(result)
    else:
        Util.print_class(stock)
        print('Enter X to quit: ')
        print('Press Enter to back: ')
        command = input()
        if command.lower() == 'x':
            print('Exit')
            exit()
        else:
            print_stocks(result)


def print_stocks(result):
    indent = '          '
    for code, stock in result.items():
        print('====================================================================================================')
        print(code)
        print('====================================================================================================')
        print(indent + stock.price)
        print(indent + stock.chg)
    listen_to_selection(result)


def show_favorite():
    codes = Common.load_array_from_file(fav_file, '\n')
    result = {}
    for code in codes:
        stock = get_stock(code)
        result[code] = stock
    print_stocks(result)
    #     result[code] = get_stock(code)
    # print_class(result)


show_favorite()
# print(low)
