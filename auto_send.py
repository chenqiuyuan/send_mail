#-*- encoding:utf-8 -*-
import qq_mail
import shibor_csv_file

def exe():
    shibor_csv_file.file()
    qq_mail.send('380133194@qq.com')
    qq_mail.send('henry.duye@gmail.com')
    qq_mail.send('ycbillows@qq.com')#
    # print 123
# exe()