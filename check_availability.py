# coding: utf-8

import urllib2
import json
import time
import random
import webbrowser
from enum import Enum

class ResponseStatus(Enum):
    TARGET_AVAILABLE = 1
    TARGET_NOT_AVAILABLE = 2
    STORE_NOT_OPEN = 3

def check_status(target=None):
    url = 'https://reserve.cdn-apple.com/CN/zh_CN/reserve/iPhone/availability.json'
    if not target:
        target = 'MNFP2CH/A'

    req = urllib2.Request(url)
    f = urllib2.urlopen(req)
    lines = ''
    for line in f:
        lines = lines + line

    availability = json.loads(lines)
    now_time = time.strftime("%H:%M:%S")
    if not availability:
        print '--------------------------------------'
        print '|  Apple Store is not available now  |'
        print '|    Automatically refersh later     |'
        print '|     Last Updated: {now_time} |'.format(now_time=now_time)
        print '--------------------------------------'
        return dict(status=ResponseStatus.STORE_NOT_OPEN)
    else:
        beijing_stores = {'R320':'三里屯', 'R645':'朝阳大悦城', 'R448':'王府井', 'R388':'西单大悦城', 'R479':'华贸'}

        beijing_availability = dict()

        for k, v in beijing_stores.items():
            beijing_availability[k] = availability[k].get(target)

        print '------------------------------------'
        print ' Beijing iPhone 7 Plus Availability'
        print '  Last Updated Time: {now_time}'.format(now_time=now_time)
        print '------------------------------------'
        for k, v in beijing_availability.items():
            print '   {store_name}: \t\t{status}'.format(store_name=beijing_stores.get(k), status=v)
        print '------------------------------------'

        available_stores = []
        urls = []
        order_url = 'https://reserve.cdn-apple.com/CN/zh_CN/reserve/iPhone/availability?channel=&returnURL=&store={store_num}&partNumber={target}'


        for k, v in beijing_availability.items():
            if 'ALL' == v:
                available_stores.append(beijing_stores.get(k))
                urls.append(order_url.format(store_num=k, target=target.replace('/','%2F')))

        if len(available_stores) > 0:
            return dict(status=ResponseStatus.TARGET_AVAILABLE,
                        stores=available_stores, urls=urls)
        else:
            return dict(status=ResponseStatus.TARGET_NOT_AVAILABLE)
flag = True
while flag:
    response = dict(status=None)
    try:
        response = check_status()
    except:
        print ' {time} Ooops! Exception! Refresh later...'.format(time=time.strftime("%H:%M:%S"))
        pass
    if response.get('status')==ResponseStatus.TARGET_AVAILABLE:
        available_stores = response.get('stores')
        urls = response.get('urls')
        flag = 0
        stores = ', '.join(available_stores)
        target_name = 'iPhone 7 Plus'
        print '* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *'
        print '    {target_name} is available in the following Apple Stores:'.format(target_name=target_name)
        print '             {stores}'.format(stores=stores)
        print '* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *'
        print '                Directing to the apple.com.cn...'
        print '                      Thanks for using!'
        print '* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *'
        for url in urls:
            webbrowser.open(url)
        flag = False
    sleep_time = random.randint(1,3)
    time.sleep(sleep_time)

