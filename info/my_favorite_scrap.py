import util.common as Common
import model.StockDTO as Stock
from Util import open_site_custom, print_class

url = 'http://www.etnet.com.hk/www/tc/stocks/realtime/quote.php?code=$CODE'
referer = 'http://www.etnet.com.hk/www/tc/stocks/realtime/'
CODE_REPLACE = '$CODE'


def get_stock(code):
    if code == '':
        return None
    m_url = url.replace(CODE_REPLACE, code)
    body = open_site_custom(m_url, header={'User-Agent': 'Mozilla/5.0',
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


def show_favorite():
    codes = Common.load_array_from_file('C:\\workspace\\programs\\OptionAnalyzer\\favorites.txt', '\n')
    result = {}
    for code in codes:
        result[code] = get_stock(code)
    print_class(result)


# show_favorite()
# print(low)
