# -*- coding: utf-8 -*-
import requests
import re
import sys
import datetime
reload(sys)
sys.setdefaultencoding('utf-8')

def file():
    html = requests.get('http://www.shibor.org/shibor/web/html/shibor.html')
    html.encoding = 'GBK'
    classinfo = []
    head = re.findall('<font color=blue>(.*?)</font></a></td>',html.text,re.S)
    shibor = re.findall('<td width="30%" align="center">(.*?)</td> ',html.text,re.S)
    BP = re.findall('<td width="30%" align="left">&nbsp;&nbsp;(.*?)</td> ',html.text,re.S)
    today = datetime.date.today()
    Stoday = str(today.year) + "_" + str(today.month)+ "_" +str(today.day)
    f = open(Stoday+'.csv','a')
    for x in range(8):
        f.writelines(head[x]+","+shibor[x]+","+BP[x]+"\n")
    f.close()
