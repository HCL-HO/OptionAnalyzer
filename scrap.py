import urllib
import pyperclip
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
        pyperclip.copy(str(soup))
        return soup
    except HTTPError as err:
        print(err.msg)
        print(err.code)
        return None


def traverse_table(table):
    pass


def scrap(code, month):
    scrap_url = url.replace(TAG_STOCK_CODE, code)
    scrap_url = scrap_url.replace(TAG_MONTH, month)
    body = open_site(scrap_url)
    table = body.find("table", id="content")
    if table is not None and table is not '':
        traverse_table(table)
    else:


scrap('CNC', '201906')
