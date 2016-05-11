#!/usr/bin/env python
#coding: utf-8

import datetime
import smtplib
from email.mime.image import MIMEImage

import email.MIMEBase
import email.MIMEMultipart
import email.MIMEText
import os


def addimg(src,imgid):
    fp = open(src, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', imgid)
    return msgImage
def send(TO):
    today = datetime.date.today()
    Stoday = str(today.year)+ "_" + str(today.month) + "_" + str(today.day)
    HOST = "smtp.qq.com"
    SUBJECT = u"SHIBOR_BP"
    # TO = "380133194@qq.com"
    FROM = "380133194@qq.com"

    # 构造MIMEBase对象做为文件附件内容并附加到根容器
    contype = 'application/octet-stream'
    maintype, subtype = contype.split('/', 1)

    main_msg = email.MIMEMultipart.MIMEMultipart()
    text_msg = email.MIMEText.MIMEText("FILE IN .CSV TYPE")
    main_msg.attach(text_msg)

    ## 读入文件内容并格式化
    data = open(Stoday+'.csv','rb')
    file_msg = email.MIMEBase.MIMEBase(maintype, subtype)
    file_msg.set_payload(data.read( ))
    data.close( )
    email.Encoders.encode_base64(file_msg)

    ## 设置附件头
    basename = os.path.basename(Stoday + '.csv')

    file_msg.add_header('Content-Disposition',
     'attachment', filename = basename)
    main_msg.attach(file_msg)
    main_msg['Subject'] = SUBJECT
    main_msg['From']=FROM
    main_msg['To']=TO
    main_msg['Date'] = email.Utils.formatdate()

    try:
        server = smtplib.SMTP()
        server.connect(HOST,"25")
        server.starttls()
        server.login("380133194@qq.com","rtfspolpqjdtbgea")
        server.sendmail(FROM, TO, main_msg.as_string())
        server.quit()
        print "邮件发送成功！"
    except Exception, e:
        print "失败："+str(e)
