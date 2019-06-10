import urllib
import pyperclip
import json
from OptionDTO import *
from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://www.etnet.com.hk/www/eng/futures/futures_stockoptions.php?atscode=%STOCK_CODE&month=%MONTH'

TAG_STOCK_CODE = '%STOCK_CODE'
TAG_MONTH = '%MONTH'


def null_to_string(text):
    if text is None:
        return ''
    else:
        return str(text)


def open_site(site):
    try:
        print(site)
        r = urllib.request.Request(site, headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(r)
        soup = BeautifulSoup(page, features="html.parser")
        # pyperclip.copy(str(soup))
        return soup
    except HTTPError as err:
        print(err.msg)
        print(err.code)
        return None


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
        call_vol = columns[0].contents
        call_chg = columns[1].contents
        call_last = columns[2].span.contents
        call_bid = columns[3].contents
        call_ask = columns[4].contents

        strike = columns[6].contents

        put_vol = columns[8].contents
        put_chg = columns[9].contents
        put_last = columns[10].span.contents
        put_bid = columns[11].contents
        put_ask = columns[12].contents

        call = Option(call_vol, call_chg, call_last, call_bid, call_ask, strike)
        put = Option(put_vol, put_chg, put_last, put_bid, put_ask, strike)
        options['call'].append(call)
        options['put'].append(put)
        # print(call)
        # print(put)
        # print('------------------------------------------------------')
    return options


def scrap(code, month):
    scrap_url = url.replace(TAG_STOCK_CODE, code)
    scrap_url = scrap_url.replace(TAG_MONTH, month)
    body = open_site(scrap_url)
    table = body.find("table", id="content")
    if table is not None and table is not '':
        result = get_options(table)
        print(json.dumps(result, indent=4, sort_keys=True, default=lambda x: x.__dict__))
        return result
    else:
        print('no table')
        return []


scrap('CNC', '201906')