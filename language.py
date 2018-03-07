import requests,re,os
import string
import csv
import sys,io
from lxml import html    #这里我们用lxml，也就是xpath的方法
#2017年20th Editor 前26 ISO 639-3
ISO=['cmn','eng','hin','urd','spa',#hin和urd和为Hindustani 
'ara','aao','arq','bbz','abv','shu','acy','adf','avl','arz','afb','ayh',
'acw','ayl','acm','ary','ars','apc','ayp','lraq','acx','aec','ayn','ssh',
'ajp','arb','pga','apd','acq','abh','aeb','auz',#ara包括如上的语言
'msa','btj','mfb','bjn','bve','kxd','bvu','pse','coa','liw','dup','hji',
'ind','jak','jax','vkk','meo','kvr','mqg','kvb','lcf','zlm','xmm','min',
'mui','zmi','max','orn','ors','mfa','pel','msi','lce','zsm','tmw','vkt',
'urk',#msa包括如上的语言
'rus','ben','por','fra','hau',
'pan','pnb',#pan包括左侧两种
'deu','gmh','goh','gct','bar','cim','geh','ksh','nds','sli','ltz','vmf',
'mhn','pfl','pdc','pdt','swg','swg','gsw','uln','sxu','wae','wep','hrx',
'yec',#deu包括如上的语言
'jpn',
'fas','prs','pes','tgk','aiq','bhh','haz','jpr','phv','deh','jdt',
'ttt',#fas包括如上的语言
'swa','swc','swh','ymk','wmw',#swa包括左侧语言
'tel','jav','wuu','kor','tam','mar','yue','vie','ita']
#文件夹名称
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
flag='17'
LangRoot='https://www.ethnologue.com/17/language/'
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
    parent=tree.xpath('//*[@id="block-system-main"]/div/div/div/div[1]/div/div/div')
    for son in parent:
        #找到人口数据
        if son.xpath('div[1]/text()')==['Population']:
            target=son.xpath('div[2]/div/p/text()')
            for got in target:
                writer.writerow([code,lang,got])

    # for n in raw:
    #     population=n
    # print([lang,population])
    # writer.writerow([code,lang,population])
    # print('loaded '+thisAddr+' finally')

def main():
    baseAddr='https://www.ethnologue.com/browse/names/'
    # for root in string.ascii_lowercase:
    for root in [flag]:
        nowAddr=baseAddr+root
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

def SelectedLang():
    for base in ISO:
        readLang(base)

# main()
SelectedLang()
# readLang('hin')