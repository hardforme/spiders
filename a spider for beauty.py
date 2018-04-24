# -*- coding:utf-8 -*-
import requests
import random
from bs4 import BeautifulSoup
import os

class mzitu:
    def __init__(self):
        self.page = 1
        self.homepage = 'http://www.mzitu.com/all/'
        self.useragent_list = [
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'
        ]
        self.header = {'User-Agent': random.choice(self.useragent_list)}
        self.path = 'F:\\mzitu\\'

    def get_url(self):
        code = self.get_pagecode(self.homepage)
        soup = BeautifulSoup(code, 'lxml')
        all_a = soup.find_all('p', class_='url')[1].find_all('a')
        for a in all_a:
            url = a['href']
            print url+'\n'
            self.get_mzt_content_in_file(url)
            '''input = raw_input()
            if input != 'y':
                break'''



    def get_pagecode(self, url):
        try:
            code = requests.get(url, headers=self.header)
            return code.text
        except requests.HTTPError, e:
            if hasattr(e, 'code'):
                print 'could not open the url\nthe error code:', 'e.code'

    def get_mzt_content_in_file(self, url):
        code = self.get_pagecode(url)
        soup = BeautifulSoup(code, 'lxml')
        pagenum = soup.find('div', class_='pagenavi').find_all('span')[6].string
        pagename = soup.find('h2', class_='main-title').string
        fname = self.path + pagename
        if not os.path.exists(fname):
            os.makedirs(fname)
            print '正在写入', str(self.path),pagename,'请稍等'
            for i in range(int(pagenum)+1):
                fullurl = url + '/' +str(i+1)
                img_code = self.get_pagecode(fullurl)
                img_soup = BeautifulSoup(img_code, 'lxml')
                img_url = img_soup.find('div', class_='main-image').find('img')['src']
                #name =str(fname + img_url[-17:-13] + img_url[-12:-10] + img_url[-9:-6] +'\\' +img_url[-6:-4] + '.jpg')
                name = fname + '\\' + img_url[-9:-4] + '.jpg'
                img = requests.get(img_url, headers=self.header)
                f = open(name, 'ab+')
                f.write(img.content)
                f.close()



a = mzitu()
a.get_url()









