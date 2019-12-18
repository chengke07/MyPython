import urllib.request
import re
import os

def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0')
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')
#   print(html)
#   html = str(html)
    return(html)



def get_ip(html):
    p = r'(?:(?:[0:1]?\d?\d|2[0-4]\d|25[0-5])\.){3}(?:[0:1]?\d?\d|2[0-4]\d|25[0-5])'
    iplist = re.findall(p,html)

    for each in iplist:
        print(each)



if __name__ == '__main__':
    url = "http://www.89ip.cn/"
#    open_url(url)
    get_ip(open_url(url))
