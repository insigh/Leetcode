import urllib.request
from bs4 import BeautifulSoup
import re
import time
import sys
import numpy as np 

def getPage(url):
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'
    headers = {'User-Agent': user_agent}
    request = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(request)
    return response.read().decode("utf-8")

def get_url(url):
    html = getPage(url)
    # print(html)
    soup = BeautifulSoup(html,"lxml")
    # print(soup.prettify())
    return_links = []
    links = soup.find_all("a",href=re.compile("realtime"))
    for each in links:
        return_links.append(each['href'])
    return return_links

def get_title_and_content(url):
    html = getPage(url)
    soup = BeautifulSoup(html, "lxml")
    title = soup.title.string
    news_time = str(soup.find(class_="datestamp"))
    date = re.match('<span class="datestamp">(.*?)<em>(.*?)</em></span>',news_time).group(1)
    ttime = re.match('<span class="datestamp">(.*?)<em>(.*?)</em></span>',news_time).group(2)
    news_content = ''
    for content in soup.find_all('p'):
        if not content.has_attr('class'):
            news_content = news_content+content.string
    # print(news_content)
    return title,date,ttime,news_content



if __name__=='__main__':
    weblist = []
    done_list = []
    page = "http://www.zaobao.com/"
    while(True):
        links = get_url(page)
        for each in links:
            if(each not in weblist):
                weblist.append(each)
        for each in weblist:
            time.sleep(np.random.rand()*3)
            if each not in done_list:
                url = "http://www.zaobao.com" + each
                print(url)
                try:
                    title, date, ttime, news_content = get_title_and_content(url)
                    print(title)
                    news_path = r'D:\zaobao_news.txt'
                    title_path = r'D:\zaobao_titles.txt'
                    f = open(news_path,'a',encoding='utf-8')
                    f.write(news_content+'\n')
                    f.close()
                    g = open(title_path,'a',encoding='utf-8')
                    g.write(title+'\n')
                    g.close()
                    done_list.append(each)
                except:
                    print('error')
                finally:
                    new_links = get_url(url)
                    for link in new_links:
                        if (link not in weblist):
                            weblist.append(link)
            else:
                continue

