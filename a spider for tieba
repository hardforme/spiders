# -*- coding:utf-8 -*-
import urllib2
import re


class Tool:
    def __init__(self):
        self.removeimg = re.compile('<img .*?>')
        self.removeaddr = re.compile('<a href=.*?>|</a>')
        self.replacebr = re.compile('<br>')
        self.removetag = re.compile('<.*?>')

    def replace(self, content):
        content = re.sub(self.removeimg, '', content)
        content = re.sub(self.removeaddr, '', content)
        content = re.sub(self.replacebr, '\n', content)
        content = re.sub(self.removetag, '', content)
        return content.strip()


class BDTB:
    def __init__(self, url, see_lz):
        self.baseurl = url + '?see_lz=' + str(see_lz)
        self.pagenum = 0
        self.title = 'baidu_tieba'
        self.tool = Tool()
        self.file = None

    def get_page_code(self, pagenum=1):
        try:
            url = self.baseurl + '&pn=' + str(pagenum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            pagecode = response.read()
            return pagecode
        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                print 'the reason of error:', e.reason
                return None

    def get_page_num(self, page):
        pattern = re.compile('<span class="red">(.*?)</span>')
        page_num = re.search(pattern, page)
        if page_num:
            self.pagenum = page_num.group(1)
            return page_num.group(1)
        else:
            print "get no pagenum"
            return None

    def get_page_title(self, page):
        pattern = re.compile('title>(.*?)</title', re.S)
        page_title = re.search(pattern, page)
        if page_title:
            self.title = page_title.group(1)
            return page_title.group(1)
        else:
            print "get no pagetitle"
            return None

    def get_page_contents(self, pagenum):
        page_code = self.get_page_code(pagenum)
        pattern = re.compile('id="post_content_.*?>(.*?)</div>', re.S)
        contents = re.findall(pattern, page_code)
        replaced_contents = []
        if contents:
            for i in range(len(contents)):
                replaced_contents.append(self.tool.replace(contents[i]))
            return replaced_contents
        else:
            print "get no contents!"
            return None

    def set_file_name(self, title):
        fulltitle = title + '.txt'
        self.file = open(fulltitle.decode('utf-8'), 'w+')

    def write_in_file(self, contents, num):
        self.file.write(str(num)+'th page:\n')
        floor = 1
        for content in contents:
            self.file.write(str(floor) + 'th floor--------------------------------------------\n')
            self.file.write(content)
            self.file.write('\n\n')
            floor += 1
        self.file.write('\n')

    def start(self):
        page = self.get_page_code()
        self.get_page_num(page)
        self.get_page_title(page)
        self.set_file_name(self.title)
        for i in range(1, int(self.pagenum)+1):
            print 'loading' + str(i) + 'th page\'s contents'
            contents = self.get_page_contents(i)
            self.write_in_file(contents, i)

'''print u'输入百度贴吧帖子的链接:'
url = raw_input()'''
print '输入 1: 只看楼主的帖子\n输入 0: 看所有的帖子'
see_lz = raw_input()
a = BDTB('https://tieba.baidu.com/p/3920771177', see_lz)
a.start()


