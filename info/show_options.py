from scrap import scrap
from Util import print_class


def show_options(code, month):
    result = scrap(code, month)
    options = result['option']
    print_class(options)
