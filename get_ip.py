from urllib.request import Request,urlopen
from urllib.error import URLError,HTTPError
import re


def open_url(url):
    req = Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0')
    try:
        page = urlopen(req)
    except HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code:',e.code)
        return 0
    except URLError as e:
        print('We failed to reach a server.')
        print('Reason:',e.reason)
        return 0
    else:
        html = page.read().decode('utf-8')
#   print(html)
#   html = str(html)
        return(html)


def get_ip(html):
    p = r'(?:(?:[0:1]?\d?\d|2[0-4]\d|25[0-5])\.){3}(?:[0:1]?\d?\d|2[0-4]\d|25[0-5])'
    if html != 0:
        iplist = re.findall(p,html)
    
        for each in iplist:
            print(each)
    else:
        exit
     


if __name__ == '__main__':
    url = "http://www.89ip.cn/"

#    open_url(url)
    get_ip(open_url(url))
