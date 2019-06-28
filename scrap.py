import json
from OptionDTO import *
from StockDTO import *
from Util import open_site

url = 'http://www.etnet.com.hk/www/eng/futures/futures_stockoptions.php?atscode=%STOCK_CODE&month=%MONTH'

TAG_STOCK_CODE = '%STOCK_CODE'
TAG_MONTH = '%MONTH'


# body_instance = ''
# site_instance = ''


def print_class(o):
    print(json.dumps(o, indent=4, sort_keys=True, default=lambda x: x.__dict__))


def null_to_string(text):
    if text is None:
        return ''
    else:
        return str(text)


def content_to_str(contents):
    if len(contents) == 0:
        return ''
    else:
        return contents[0]


def get_options(table):
    # print(table)
    trs = table.find_all('tr')
    # print(trs)
    options = {'call': [],
               'put': []}
    # get rows that have data
    target_trs = []
    for i in range(len(trs)):
        if trs[i].get('id') == 'start_pos':
            target_trs = trs[i:]
            break

    for tr in target_trs:
        columns = tr.find_all('td')
        # for td in columns:
        #     print(td.contents)
        call_vol = content_to_str(columns[0].contents)
        call_chg = content_to_str(columns[1].contents)
        call_last = content_to_str(columns[2].span.contents)
        call_bid = content_to_str(columns[3].contents)
        call_ask = content_to_str(columns[4].contents)

        strike = content_to_str(columns[6].contents)

        put_vol = content_to_str(columns[12].contents)
        put_chg = content_to_str(columns[11].contents)
        put_last = content_to_str(columns[10].span.contents)
        put_bid = content_to_str(columns[8].contents)
        put_ask = content_to_str(columns[9].contents)

        call = Option(call_vol, call_chg, call_last, call_bid, call_ask, strike)
        put = Option(put_vol, put_chg, put_last, put_bid, put_ask, strike)
        options['call'].append(call)
        options['put'].append(put)
        # print(call)
        # print(put)
        # print('------------------------------------------------------')
    return options


def get_stock(body):
    div = body.find("div", {"class": "DivFigureContent"})
    price = div.find('span', {'class': 'HeaderTxt'}).contents[0].rstrip()
    chg = div.find('span', {'class': 'boldTxt'}).contents[0][:6].rstrip()
    details_table = div.find_all('table')[1]
    details_table_row1 = details_table.find_all('tr')[0]
    details_table_row2 = details_table.find_all('tr')[1]
    high = details_table_row1.find_all('td')[1].contents[0].rstrip()
    turnover = details_table_row1.find_all('td')[9].contents[0].rstrip()
    low = details_table_row2.find_all('td')[1].contents[0].rstrip()
    m_high = details_table_row1.find_all('td')[13].contents[0].rstrip()
    m_low = details_table_row2.find_all('td')[7].contents[0].rstrip()
    # print(div)
    # print(price)
    # print(chg)
    # print(high)
    # print(turnover)
    # print(low)
    # print(m_high)
    # print(m_low)
    return Stock(price, high, low, turnover, chg, m_high, m_low)


def scrap(code, month):
    scrap_url = url.replace(TAG_STOCK_CODE, code)
    scrap_url = scrap_url.replace(TAG_MONTH, month)
    body = open_site(scrap_url)
    table = body.find("table", id="content")
    options_result = ''
    if table is not None and table is not '':
        options_result = get_options(table)
    else:
        print('no table')
    stock_result = get_stock(body)
    result = dict()
    result['option'] = options_result
    result['stock'] = stock_result
    # print_class(result)
    return result

# scrap('CNC', '201906')
