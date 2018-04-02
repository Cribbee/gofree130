# coding: utf-8
import os, sys
import smtplib
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText

mailInfo = {
    "from": "gofree@nanmuduo.com",
    "to": "zouwx2cs@foxmail.com",
    "hostname": "smtp.exmail.qq.com",
    "username": "gofree@nanmuduo.com",
    "password": "123QWe->0808",
    "mailsubject": u'GoFree注册成功',
    "mailtext": u"感谢您的注册，祝您使用愉快！",
    "mailencoding": "utf-8"
}

def welecome(rece, name):
    smtp = SMTP_SSL(mailInfo["hostname"])
    smtp.set_debuglevel(1)
    smtp.ehlo(mailInfo["hostname"])
    smtp.login(mailInfo["username"], mailInfo["password"])

    msg = MIMEText(name + ", " + mailInfo["mailtext"], _subtype='plain', _charset=mailInfo["mailencoding"])
    msg["Subject"] = Header(mailInfo["mailsubject"], mailInfo["mailencoding"])
    msg["from"] = mailInfo["from"]
    msg["to"] = rece # mailInfo["to"]
    smtp.sendmail(mailInfo["from"], mailInfo["to"], msg.as_string())
    smtp.quit()