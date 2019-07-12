from typing import List

from Util import open_site, print_class
from DividendDTO import Dividend

url = 'http://www.etnet.com.hk/www/tc/stocks/ci_div_exdate.php?page='


def row_to_dividend(row):
    # print(row)
    tds = row.find_all('td')
    if len(tds) > 7:
        annonce = tds[0].text
        code = tds[1].text
        name = tds[2].text
        finance = tds[3].text
        details = tds[4].text
        exdate = tds[5].text
        book_close = tds[6].text
        payable = tds[7].text
        return Dividend(annonce, code, name, finance, details, exdate, book_close, payable)
    else:
        return None


def scrap():
    page = 1
    has_data = True
    dividends = []
    while has_data:
        body = open_site(url + str(page))
        table = body.find('table', {'class': "figureTable"})
        rows = table.find_all('tr')
        if len(rows) > 3:
            for i in range(len(rows)):
                if i > 0:
                    row = rows[i]
                    try:
                        dividend = row_to_dividend(row)
                        if dividend is not None:
                            dividend.pretty_print()
                            dividends.append(dividend)
                    except IndexError as e:
                        print(e)
                        print(row)
            page += 1
        else:
            has_data = False
    return dividends


# page += 1

scrap()