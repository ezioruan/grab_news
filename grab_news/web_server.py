#-* coding:UTF-8 -*      
'''
Created on 2013年11月14日

@author: ezioruan
'''

from grab_news.storage import get_news
from setting import HTTP_HOST,HTTP_PORT
from flask import  Flask,jsonify
from gevent.pywsgi import WSGIServer


app = Flask(__name__)

@app.route('/news')
def news():
    news = get_news()
    return jsonify(news)


def run_web_server():
    server = WSGIServer((HTTP_HOST, HTTP_PORT), app,)
    server.serve_forever()


