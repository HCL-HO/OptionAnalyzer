from Util import print_class


class Dividend:
    def __init__(self, annouce_date: str, number: str, name: str, financial_year: str, detail: str, ex_date: str,
                 book_close: str,
                 payable: str):
        self.annouce_date = annouce_date
        self.number = number
        self.name = name
        self.financial_year = financial_year
        self.detail = detail
        self.ex_date = ex_date
        self.book_close = book_close
        self.payable = payable

    def print(self):
        print_class(self)

    def pretty_print(self):
        print(self.annouce_date + ' ' + self.number + ' ' + self.name + ' ' + self.financial_year + ' '
              + self.detail + ' ' + self.ex_date + ' ' + self.book_close + ' ' + self.payable)
