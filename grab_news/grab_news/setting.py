#-* coding:UTF-8 -*      
'''
Created on 2013年11月15日

@author: ezioruan
'''

#===============================================================================
# mongodb 相关配置
#===============================================================================
MONGO_URL = 'mongodb://localhost:27017/'
DB_NAME = 'spider_news'

#===============================================================================
# http服务的端口和地址
#===============================================================================
HTTP_HOST  = '0.0.0.0'
HTTP_PORT = 5188

#===============================================================================
# 新闻内容过少忽略的长度
#===============================================================================
NEWS_LENGTH = 100