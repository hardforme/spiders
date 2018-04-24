import urllib2
import re

class QSBK:
    def __init__(self):
        self.url = 'https://www.qiushibaike.com/hot/page/'
        self.page = 0
        self.enable = 1
        self.useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'
        self.header = {'User-Agent': self.useragent}
        self.stories = []

    def get_page_code(self, page):
        url = self.url + str(page)
        request = urllib2.Request(url, headers= self.header)
        response = urllib2.urlopen(request)
        content = response.read().decode('utf-8')
        return content

    def get_page_item(self, page):
        content = self.get_page_code(page)
        if not content:
            print 'page load error!'
            return None
        pattern = re.compile('<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<span>(.*?)</span>.*?number">(.*?)</i', re.S)
        items = re.findall(pattern, content)
        for item in items:
            self.stories.append(item)
            return self.stories

    def get_one_item(self):
        if self.enable == 1:
            if len(self.stories) > 0:
                print "username:%s/t thump up:%s/n content:%s" % (self.stories[0][0], self.stories[0][2], self.stories[0][1])
                del self.stories[0]
            else:
                self.page += 1
                self.get_page_item(self.page)
                print "username:%s\t thump up:%s\ncontent:%s" % (self.stories[0][0].strip(), self.stories[0][2].strip(), self.stories[0][1].strip())
                del self.stories[0]

    def start(self):
        print r"input 'y' to get a story and 'Q' to exit!"
        while self.enable == 1:
            enter = raw_input()
            if enter == 'Q':
                print 'thanks for your using!'
                break
            elif  enter == 'y':
                self.enable = 1
                self.get_one_item()
            else :
                print 'wrong input!\nPlease input again!'

spider = QSBK()
spider.start()









