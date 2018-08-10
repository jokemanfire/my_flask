# -*- coding:utf-8 -*-
import requests


def my_crawl(froms,tos,date):
    s = requests.session()
    s.headers = {'Host': 'trains.ctrip.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',

'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2' ,
'Accept-Encoding': 'gzip, deflate',

'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
'If-Modified-Since': 'Thu, 01 Jan 1970 00:00:00 GMT',
'Connection': 'keep-alive' }
    url = "http://trains.ctrip.com/TrainBooking/Ajax/SearchListHandler.ashx?Action=searchColudTickets"
    post_date = "value={\"dname\":\"上海\",\"aname\":\"重庆\",\"ddate\":\"2018-08-03\"}".encode("utf-8")
    get_html = s.post(url, post_date)
   
    print(get_html.text)


if __name__ == '__main__':
    my_crawl('北京','上海','2018-08-03')