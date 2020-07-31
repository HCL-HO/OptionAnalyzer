from datetime import date
from typing import List
from Strategy import Strategy
from StrategyMap import StrategyMap
from OptionDTO import *
import util.common as common
import json
import os

my_path = os.path.abspath(os.path.dirname(__file__))
file = os.path.join(my_path, "stock.json")
date_format = "%m/%d/%Y"

CODE_DATE = 'date'
CODE_PRICE = 'price'
CODE_QY = 'qy'
CODE_STRA = 'strategy'
CODE_OPTS = 'options'


def load_record():
    record = common.get_text_from_file_in_str(file)
    if record != "":
        record = json.loads(record)
    return {} if record == "" else record


#
# def refresh():
#     global stock_json
#     stock_json = load_record()
#     stock_json = {} if stock_json == "" else stock_json


def add_stock(code, price, qy):
    # print("History: " + str(stock_json))
    stock_json = load_record()
    stock_json[code] = [] if code not in stock_json else stock_json[code]
    stock = {CODE_DATE: date.today().strftime(date_format), CODE_PRICE: price, CODE_QY: qy}
    stock_json[code].append(stock)
    common.write_output_to_file(json.dumps(stock_json), file)
    return True


def add_option_strategy(code: str, pair: List, strategy_name: str):
    stock_json = load_record()
    stock_json[code] = [] if code not in stock_json else stock_json[code]
    pair_str = ''
    for opt in pair:
        pair_str += str(opt) + '\n'
    strategy = {CODE_STRA: strategy_name, CODE_DATE: date.today().strftime(date_format), CODE_OPTS: pair_str}
    stock_json[code].append(strategy)
    common.write_output_to_file(json.dumps(stock_json), file)
    return True


def del_stock(code, index):
    stock_json = load_record()
    print("History: " + str(stock_json))
    if code in stock_json:
        stock_list = stock_json[code]
        print('Delete record: ' + code + ' ' + json.dumps(stock_list[int(index) - 1]))
        del stock_list[int(index) - 1]
        common.write_output_to_file(json.dumps(stock_json), file)
        return True
    return False

# add_stock('abc', '123', '1000')
