#!/usr/bin/env python3
# coding:utf-8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def welecome(rece, name):
    sender = 'gofree@nanmuduo.com'
    receiver = 'zouwx2cs@foxmail.com'
    #receiver = rece
    subject = 'python email test'
    smtpserver = 'smtp.exmail.qq.com'
    username = 'gofree@nanmuduo.com'
    password = '123QWe->0808'

    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = u'GoFree注册成功'

    msgText = MIMEText((u'%s，感谢您的注册，祝您使用愉快' % name), 'html', 'utf-8')
    msgRoot.attach(msgText)

    #fp = open('h:\\python\\1.jpg', 'rb')
    #msgImage = MIMEImage(fp.read())
    #fp.close()

    #msgImage.add_header('Content-ID', '<image1>')
    #msgRoot.attach(msgImage)

    smtp = smtplib.SMTP()
    smtp.connect('smtp.exmail.qq.com', 465)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    smtp.quit()
welecome('zouwx2cs@foxmail.com', "test4")