#-* coding:UTF-8 -*      
'''
Created on 2013年11月15日

@author: ezioruan
'''

from grab_news.db import news
import random
from copy import deepcopy
import time

#title:content
big_data = {}

def reset():
    global big_data
    print 'big data is begin to be reset'
    big_data = {}


def add_news(title,content):
    news_data = {'title':title,'content':content,'add_time':time.time()}
    big_data.update({title:news_data})
    print 'add_news content ',content
    news.insert(deepcopy(news_data))
    

def delete_news(title):
    big_data.pop(title)
    

def get_news():
    random_key = big_data.keys()[random.randint(0,len(big_data)-1)]
    random_news =  big_data.get(random_key)
    print 'random_news',random_news
    return random_news
    
    
    
    
    
    
    
    
    
    
    