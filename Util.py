import urllib
import json
from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup


def print_class(o):
    print(json.dumps(o, indent=4, sort_keys=True, default=lambda x: x.__dict__))


def open_site(site):
    # global body_instance, site_instance
    # if site_instance == site and body_instance != '':
    #     return body_instance
    try:
        print(site)
        r = urllib.request.Request(site, headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(r)
        soup = BeautifulSoup(page, features="html.parser")
        # body_instance = soup
        # site_instance = site
        # pyperclip.copy(str(soup))
        return soup
    except HTTPError as err:
        print(err.msg)
        print(err.code)
        return None
