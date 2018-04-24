# -*- coding:utf-8 -*-


import requests
from bs4 import BeautifulSoup
import os

class qidian():
    def __init__(self, url):
        self.url = url + '#Catalog'
        self.path = 'F:\\qidian\\'
        self.soup = BeautifulSoup(requests.get(self.url).text, 'lxml')
        self.count = 1
        self.title = 'bcd'


    def get_pagecode(self, url):
        try:
            code = requests.get(url)
            return code.text
        except requests.HTTPError, e:
            if hasattr(e, 'code'):
                print 'could not open the url\nthe error code:', 'e.code'

    def get_title(self):
        self.title = self.soup.find('div', class_='book-info').find('h1').find('em').string

    def get_url(self):
        for ul in self.soup.find_all('ul', class_='cf'):
            for li in ul.find_all('li'):
                print '正在写入第'+str(self.count)+'章\n'
                url = 'http:'+li.find('a')['href']
                self.save_in_file(url)
                self.count += 1

    def save_in_file(self, url):
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        os.chdir(self.path)
        code = self.get_pagecode(url)
        soup = BeautifulSoup(code, 'lxml')
        textname = self.title+'.txt'
        file = open(unicode(textname, 'utf-8'), 'a+')
        chaptername = soup.find('h3', class_='j_chapterName').string+'\n'
        file.write(chaptername.encode('utf-8'))
        for line in soup.find('div', class_='read-content j_readContent').find_all('p'):
            l = line.string+'\n'
            file.write(l.encode('utf-8'))
        file.close()

    def start(self):
        #self.get_title()
        self.get_url()

a = qidian('http://book.qidian.com/info/8361')
a.start()
