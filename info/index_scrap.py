from Util import open_site
from IndexDTO import Index

url = 'http://www.etnet.com.hk/www/tc/stocks/indexes_detail.php?subtype=hsi'


def scrap() -> Index:
    body = open_site(url)
    container = body.find('div', {"class": "StkIndexesLeft"})
    details_div = container.find('div', {'class': "StkIndexesOther"})
    details_left = details_div.findAll('div')[0]
    details_right = details_div.findAll('div')[1]

    index = container.find('div', {"class": "StkIndexesNorminal"}).text
    change = container.findAll('div', {'class': "StkIndexesChange"})[0].find('div').text
    last_close = details_left.find('p').text.rstrip()[-9:]
    this_open = details_left.findAll('p')[1].text.rstrip()[-9:]
    this_high = details_right.findAll('p')[0].text.rstrip()[-9:]
    this_low = details_right.findAll('p')[1].text.rstrip()[-9:]
    turnover = container.findAll('div', {'class': "StkIndexesChange"})[1].findAll('div')[1].text

    index = Index(index, this_high, this_low, turnover, change, this_open, last_close)
    return index
    # hsi = Stock()


def show_hsi():
    scrap().print()


show_hsi()