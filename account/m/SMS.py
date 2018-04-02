# coding:utf-8
import time
import hashlib
import requests
import random

URL_SENT_SMS = "https://api.miaodiyun.com/20150822/industrySMS/sendSMS"



def verification(phone, veri_code):
    accountSid = "efc5367358d24c10aa1791cec162d63a"
    AUTH_TOKEN = "de58cd8eb19846d2abd4f52b1e872663"
    #smsContent = ""
    # 模板代码
    templateid = 124649773

    # 随机生成验证码
    param = ("%4d" % veri_code) + "%2C10"
    to = phone
    timestamp = time.strftime('%Y%m%d%H%M%S')
    context = accountSid + AUTH_TOKEN + timestamp
    sig = hashlib.md5(context.encode('utf-8')).hexdigest()
    respDataType = "JSON"
    #print (context)
    #print (sig)

    url = URL_SENT_SMS

    payload = "accountSid=%s&templateid=%d&param=%s&to=%s&timestamp=%s&sig=%s&respDataType=%s" \
              % (accountSid, templateid, param, to, timestamp, sig, respDataType)
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    return response.text
    #print(payload)