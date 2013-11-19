#-* coding:UTF-8 -*      
'''
Created on 2013年11月15日

@author: ezioruan
'''
import gevent.monkey
gevent.monkey.patch_all()
from datetime import datetime
import gevent
import signal
from grab_news import storage
from grab_news.spider import all_spider
from grab_news.grab import get_content
from grab_news.web_server import run_web_server
from grab_news.setting import NEWS_LENGTH



def grap_news():
    news_list = []
    for spider in all_spider:
        spider.reset()
        spider.run()
        news = spider.get_news()
        news_list.append(news)
    begin_job(news_list)

def on_hour():
    grap_news()
 
def add_news(title,link):
    content = get_content(link)
    if len(content) < NEWS_LENGTH:
        return
    storage.add_news(title, content)
    

def begin_job(news_list):
    jobs = []
    for news in news_list:
        for title,link in news.items(): 
            jobs.append(gevent.spawn(add_news,title,link))
    gevent.joinall(jobs, timeout=2)    



def run_forever():
    while True:
        now =  datetime.now()
        print now
        if now.minute == 0 and now.second == 0:
            on_hour()
        gevent.sleep(1)


if __name__ == '__main__':
    gevent.signal(signal.SIGQUIT, gevent.shutdown)
    event_thread = gevent.spawn(run_forever)
    http_thread = gevent.spawn(run_web_server)
    grap_news()
    event_thread.join()
   
    
    
    
    
    
    
    