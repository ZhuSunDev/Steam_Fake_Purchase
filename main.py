# encoding:utf-8
import os
import re
import time
import requests
import random


retry = 0
retry_max = 10

hosturl = "http://192.168.1.233:1242"
botnames = ["BotName1","BotName2"]
subs = [
    ["111","222","333"],["444","555","666"]
]
bundles = [
    ["11","22","33"],["44","55","66"]
]
sleeptime = 36000

request_headers = {
"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Mobile Safari/537.36","Content-Type":"application/json"
}


def fakepurchase(botname,uid):
    retry = 0
    retry_max = 10
    for sub in subs[uid]:
        while retry < retry_max:
            try:
                url = hosturl + '/Api/ASFEnhance/'+ str(botname) +'/Purchase'
                r = requests.post(url, headers=request_headers,data='{"SubIds": ["'+ sub +'"], "SkipOwned": true, "FakePurchase": true}')
                retry = 0
                set_log(time.asctime(time.localtime(time.time())) + r.text)
                time.sleep(random.randint(30,60))
                break
            except:
                retry = retry + 1
                print("Error at fakepurchase(), Retrying... (%(retry)s/%(max)s)" % {'retry': retry, 'max': retry_max})
                continue
    for bundle in bundles[uid]:
        while retry < retry_max:
            try:
                url = hosturl + '/Api/ASFEnhance/'+ str(botname) +'/Purchase'
                r = requests.post(url, headers=request_headers,data='{"BundleIds": ["'+ bundle +'"], "SkipOwned": true, "FakePurchase": true}')
                retry = 0
                set_log(time.asctime(time.localtime(time.time())) + r.text)
                time.sleep(random.randint(30,60))
                break
            except:
                retry = retry + 1
                print("Error at fakepurchase(), Retrying... (%(retry)s/%(max)s)" % {'retry': retry, 'max': retry_max})
                continue
def set_log(text):
    logger = open(botname + '.txt','a+')
    print(text)
    print(text,file=logger)
    logger.close()

if __name__ == '__main__':
    while True:
        uid = 0
        for botname in botnames:
            fakepurchase(botname,uid)
            uid = uid + 1
        print(time.asctime(time.localtime(time.time())),'待机中，等待下次采集。')
        time.sleep(sleeptime)
