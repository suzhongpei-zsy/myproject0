import random
import requests
import time
import json
import hashlib

#url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
#content="我和你"

class Youdao():
    def __init__(self, content):
        self.content=content
        self.url='http://fanyi.youdao.com/translate'
        self.ts=self.get_ts()
        self.salt=self.get_salt()
        self.sign=self.get_sign()


    def get_salt(self):
        return self.ts + str(random.randint(0, 10))


    def get_md5(self, value):
        m = hashlib.md5()
        m.update(value.encode("utf-8"))
        return m.hexdigest()

    def get_sign(self):
        s = "fanyideskweb" + self.content + self.salt + "Nw(nmmbP%A-r6U3EUn]Aj"
        return self.get_md5(s)

    def get_ts(self):
        t = time.time()
        return str(int(round(t * 1000)))


    def yield_form_data(self):
        form_data = {
            'i': self.content,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': self.salt,
            'sign': self.sign,
            'ts': self.ts,
            'bv': 'f0ece28f714caaf3c6cee92884b1a685',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME',
        }
        return form_data

    def yield_headers(self):
        return {
            'Cookie':'OUTFOX_SEARCH_USER_ID=197877919@10.108.160.18; OUTFOX_SEARCH_USER_ID_NCOO=1965624091.2843742; JSESSIONID=aaaTbrdBhXH9'
            'Referer: http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.9 Safari/537.36'
        }


    def fanyi(self):
        response = requests.post(self.url, data=self.yield_form_data(), headers=self.yield_headers())
        content=json.loads(response.text)
        return content['translateResult'][0][0]['tgt']

if __name__ =='__main__':
    while(True):
        i=input("please input : ")
        youdao=Youdao(i)
        print("fanyi result : ",youdao.fanyi())
