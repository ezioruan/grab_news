#-* coding:UTF-8 -*      
'''
Created on 2013年11月15日

@author: ezioruan
'''
# -*- coding: utf-8 -*-


import bs4
import requests
from grab_news import get_utf8_str



class BaseSpider(object):
    
    def __init__(self,index_page):
        self.index_page = index_page
        self.reset()
        
    def run(self):
        pass
    
    
    def get_news(self):
        return self.news
    
    def reset(self):
        self.news = {}
    


INDEX_PAGE_163 = 'http://news.163.com/rank'

class NeteaseNewsSpider(BaseSpider):
    
    def __init__(self):
        super(NeteaseNewsSpider, self).__init__(INDEX_PAGE_163)
        
    
    def run(self):
        try:
            r = requests.get(self.index_page)
        except:
            print('Could not connect to %s' % self.index_page)
            return

        html = r.text
        soup = bs4.BeautifulSoup(html)
        tabs = soup.find_all('div',{'class':'tabContents active'})
        if not tabs:
            print 'not tabs find'
            return
        hot_tab = tabs[0]
        news_list = hot_tab.find_all('a')
        self.news = {get_utf8_str(news.text):news.attrs.get('href') for news in news_list}
        
    
INDEX_PAGE_SOHU = 'http://comment.news.sohu.com/djpm/'    
class SOHONewsSpider(BaseSpider):
    
    def __init__(self):
        super(SOHONewsSpider, self).__init__(INDEX_PAGE_SOHU)
        
    
    def run(self):
        try:
            r = requests.get(self.index_page)
        except:
            print('Could not connect to %s' % self.index_page)
            return

        html = r.text
        soup = bs4.BeautifulSoup(html)
        tabs = soup.find_all('div',{'class':'cake01'})
        if not tabs:
            print 'not tabs find'
            return
        hot_tab = tabs[0]
        news_list = hot_tab.find_all('a')
        self.news = {get_utf8_str(news.text):news.attrs.get('href') for news in news_list}
        
INDEX_PAGE_QQ = 'http://news.qq.com/paihang.htm'    
class QQNewsSpider(BaseSpider):
    
    def __init__(self):
        super(QQNewsSpider, self).__init__(INDEX_PAGE_QQ)
        
    
    def run(self):
        try:
            r = requests.get(self.index_page)
        except:
            print('Could not connect to %s' % self.index_page)
            return

        html = r.text
        soup = bs4.BeautifulSoup(html)
        tabs = soup.find_all('td',{'class':'f14 pl18'})
        if not tabs:
            print 'not tabs find'
            return
        hot_tab = tabs[20:30]
        news_list = [hot_news.find_all('a')[0]  for hot_news in hot_tab]
        self.news = {get_utf8_str(news.text):news.attrs.get('href') for news in news_list}
        


all_spider = [NeteaseNewsSpider(),SOHONewsSpider(),QQNewsSpider()]



if __name__ == '__main__':
    for spider in all_spider:
        spider.run()
        print  spider.get_news()
    
    
    
    
    
    
    
    
