#encoding:utf-8
import urllib.request
import re
from collections import deque

queue=deque()
visited=set()

url='http://news.dbanotes.net/'
headers={'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36'}
queue.append(url)
cnt=0

while queue:
    url=queue.popleft()
    visited|={url}
    print('已经抓取:%s\t正在抓取: %s'%(cnt,url))
    try:
        request=urllib.request.Request(url,headers=headers)
        data=urllib.request.urlopen(request,timeout=2)
    except:
        continue
    if 'html' not in data.getheader('Content-Type'):
        continue
    if data.status !=200:
        continue
    try:
        url_html=data.read().decode('utf-8')
    except:
        continue
    for i in re.findall(r'class="title".+?href="(.+?)"',url_html):
        if i not in visited and 'http' in i:
            queue.append(i)
            cnt+=1
            print('%s 加入队列'%i)
    
