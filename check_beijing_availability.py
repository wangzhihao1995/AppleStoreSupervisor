import urllib2
import json
import time
import random
import webbrowser

def check_status():
    url = 'https://reserve.cdn-apple.com/CN/zh_CN/reserve/iPhone/availability.json'
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
        print '|      Please try again later        |'
        print '--------------------------------------'
    else:
        beijing_stores = {'R320':'sanlitun', 'R645':'chaoyang', 'R448':'wangfujing', 'R388':'xidan', 'R479':'huamao'}

        beijing_availability = dict()

        for k, v in beijing_stores.items():
            beijing_availability[v] = availability[k]

        for k, v in beijing_availability.items():
            for key in v.keys():
                if key != target:
                    v.pop(key)

        slt = beijing_availability.get('sanlitun').get(target)
        hm = beijing_availability.get('huamao').get(target)
        cy = beijing_availability.get('chaoyang').get(target)
        wfy = beijing_availability.get('wangfujing').get(target)
        xd = beijing_availability.get('xidan').get(target)

        print '------------------------------------'
        print ' BEIJING IPHONE7+ BLACK AVALABILITY'
        print '  Last Updated Time: {now_time}'.format(now_time=now_time)
        print '------------------------------------'
        print '   SANLITUN:     {status}'.format(status=slt)
        print '   HUAMAO:       {status}'.format(status=hm)
        print '   CHAOYANG:     {status}'.format(status=cy)
        print '   WANGFUJING:   {status}'.format(status=wfy)
        print '   XIDAN:        {status}'.format(status=xd)
        print '------------------------------------'

        available_stores = []
        urls = []
        order_url = 'https://reserve.cdn-apple.com/CN/zh_CN/reserve/iPhone/availability?channel=&returnURL=&store={store_num}&partNumber=MNFP2CH%2FA'
        if slt == 'ALL':
            available_stores.append('sanlitun')
            urls.append(order_url.format(store_num='R320'))
        if hm == 'ALL':
            available_stores.append('huamao')
            urls.append(order_url.format(store_num='R479'))
        if cy == 'ALL':
            available_stores.append('chaoyang')
            urls.append(order_url.format(store_num='R645'))
        if wfy == 'ALL':
            available_stores.append('wangfujing')
            urls.append(order_url.format(store_num='R448'))
        if xd == 'ALL':
            available_stores.append('xidan')
            urls.append(order_url.format(store_num='R388'))
        return available_stores, urls

flag = True
while flag:
    available_stores, urls = check_status()
    if len(available_stores) > 0:
        flag = 0
        stores = str(available_stores).replace('\'','').replace('[','').replace(']','')
        print '* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *'
        print '     iPhone7+ is available in {stores} now!'.format(stores=stores)
        print '         Directing to the apple.com.cn...'
        print '             Thanks for using!'
        print '* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *'
        for url in urls:
            webbrowser.open(url)
        flag = False
    sleep_time = random.randint(5, 10)
    time.sleep(sleep_time)
