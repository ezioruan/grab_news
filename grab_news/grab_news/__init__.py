#-* coding:UTF-8 -*      
'''
Created on 2013年11月14日

@author: ezioruan
'''

def get_utf8_str(str):
    utf8_str = ''
    for encoding in ['utf-8','gbk','gb2312','gb18030','iso8859-1']:
        try:
            utf8_str = str.decode(encoding)
        except:
            continue
        else:
            return utf8_str
    return str