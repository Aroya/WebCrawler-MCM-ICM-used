import requests,re,os
import string
import csv
import sys,io
from lxml import html    #这里我们用lxml，也就是xpath的方法
#文件夹名称
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
flag='e'
LangRoot='https://www.ethnologue.com/language/'
f=open('output-'+flag+'.csv','w',newline='',encoding='utf-8')
writer=csv.writer(f)

def readLang(code):
    thisAddr=LangRoot+code
    page=requests.get(thisAddr)
    page.encoding='utf-8'
    tree=html.fromstring(page.text)
    #读取语言名
    raw=tree.xpath('//*[@id="page-title"]/text()')
    lang=''
    for n in raw:
        lang=n
    #读取population
    population=''
    raw=tree.xpath('//*[@id="block-system-main"]/div/div/div/div[1]/div/div/div[4]/div[2]/div/p/text()')
    for n in raw:
        population=n
    # print([lang,population])
    writer.writerow([lang,population])
    # print('loaded '+thisAddr+' finally')

def main():
    baseAddr='https://www.ethnologue.com/browse/names/'
    # for root in string.ascii_lowercase:
    for root in [flag]:
        nowAddr=baseAddr+root
        # nowAddr='http://blog.csdn.net/u013533810/article/details/54849230'
        #请求页面
        page=requests.get(nowAddr)
        # print(page.text)
        elemList=re.findall('href="/language/(.*?)"',page.text)
        i=0
        for n in elemList:
            #前面有3个连接到ISO标准的链接
            if(i<3):
                i=i+1
                continue
            readLang(n)
            
        print('loaded '+nowAddr+' finally')

main()