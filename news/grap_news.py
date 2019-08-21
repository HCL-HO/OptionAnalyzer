from typing import List

import feedparser


# import Util


class Feed(object):
    def __init__(self, title: str, title_detail: str, id: str, guidislink: str, link: str, summary: str,
                 summary_detail: str, published: str, published_parsed: str):
        self.title = title
        self.title_detail = title_detail
        self.id = id
        self.guidislink = guidislink
        self.link = link
        self.summary = summary
        self.summary_detail = summary_detail
        self.published = published
        self.published_parsed = published_parsed


def get_feed(params) -> Feed:
    return Feed(params['title'], params['title_detail'], params['id'], params['guidislink'], params['link'],
                params['summary'], params['summary_detail'], params['published'], params['published_parsed'])


local_rss_url = "https://rthk.hk/rthk/news/rss/e_expressnews_elocal.xml"
finance_rss_url = 'https://rthk.hk/rthk/news/rss/e_expressnews_efinance.xml'
selected_news_cate = ''


def get_feeds(url: str):
    feed = feedparser.parse(url)
    news = feed['items']
    feeds = []
    for new in news:
        feeds.append(get_feed(new))
    return feeds
    # Util.print_class(feeds)


def read_details(feeds: List, selected_feed: int):
    feed = feeds[selected_feed]
    print('====================================================================================================')
    print('title: ' + feed.title_detail.value)
    print('====================================================================================================')
    print(feed.summary_detail.value)
    print('====================================================================================================')
    print('Press enter to back: ')
    print('Press X to quick: ')
    command = input()
    if command.lower() == 'x':
        print('Exit')
    else:
        read_news()


def listen_to_feed_selection(feeds: List):
    print('select a feed: ')
    selected_feed = input()
    if selected_feed.isdigit() and int(selected_feed) < len(feeds):
        read_details(feeds, int(selected_feed))
    else:
        print('Exit')


def read_news():
    global selected_news_cate
    if selected_news_cate == '':
        print('1) local, 2) finance')
        selected_news_cate = input()
    if selected_news_cate == '1':
        read_selected_news(get_feeds(local_rss_url))
    elif selected_news_cate == '2':
        read_selected_news(get_feeds(finance_rss_url))
    elif selected_news_cate.lower() == 'x':
        print('Exit')
    else:
        print('Try again')
        read_news()


def read_selected_news(feeds):
    num = 0
    for feed in feeds:
        print(str(num) + ') ' + feed.title)
        num += 1
    listen_to_feed_selection(feeds)


read_news()
