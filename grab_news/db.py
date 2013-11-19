#-* coding:UTF-8 -*      
'''
Created on 2013年11月15日

@author: ezioruan
'''
from grab_news.setting import MONGO_URL,DB_NAME
from pymongo import MongoClient 


client = MongoClient('localhost', 27017)
db = client[DB_NAME]


news = db.news


