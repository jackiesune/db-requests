import requests
import time 
from lxml import etree

from bs4 import BeautifulSoup
url='https://book.douban.com/top250?start=0'
def get_one_page(url):
    headers={
        'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0',
        'Host':'book.douban.com'
    }
    response=requests.get(url,headers=headers)
    html=response.text
    return html

def parse_page_xpath(html):
    html=etree.HTML(html)
    results=html.xpath('//body//div[@id="content"]//div[@class="indent"]/table')
#    for result in results:
#            print(result.xpath('//div[@class="pl2"]/a/text()'))
#            print(result.xpath('//p[@class="pl"]/text()'))
#    for result in results:
    for i in range(len(results)):

        bhtml=etree.tostring(results[i],encoding = "utf-8", pretty_print = True, method = "html")
        st=str(bhtml,'utf-8')
        print(st)

        print("="*(150))
        print(results[i].xpath('//p[@class="pl"]/text()'))



def parse_page_beautifulsoup_base(html):
    soup=BeautifulSoup(html,'lxml')
    result=soup.html.body.find(name='div',class_='indent')
    firststep=result.find_all(name="table")
    book={}
    for item in firststep:
        sedstep=item.tr.find(name="div",attrs={"class":"pl2"})
        book["title"]=sedstep.a.get_text()
        book["author"]=item.find(name="p",attrs={'class':'pl'}).string
        book["rating"]=item.find(class_="rating_nums").string
        book["notes"]=item.find(class_="inq").string 
        print(book)


    

def main():
    html=get_one_page(url)
    parse_page_beautifulsoup_base(html)




main()


    


