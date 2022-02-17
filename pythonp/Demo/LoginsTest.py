# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     LoginsTest.py
   Description :
   Author :        曾良均
   QQ:             277099728
   Date：          8/11/2021 3:46 PM
-------------------------------------------------
   Change Activity:
                   8/11/2021:
-------------------------------------------------
"""
__author__ = 'ljzeng'

import unittest
from urllib import parse
import requests
import uuid
import random
import time
import ddt

sn = random.uniform(0,1)  # 用于生成随机浮点数
uid = str(uuid.uuid4())
uid = ''.join(uid.split('-'))  # 用于生成UUID（通用唯一识别码）


url = 'http://192.168.25.105/T02/FIC5/fic/Host.ashx?SN=%s' %sn
testdata = (('ad','1',''),       # 正确的用户名及密码
            ('x','a','Invalid Username or Password.'),      # 不存在的用户
            ('ficro','2','Invalid Username or Password.'),
            ('ficro','3','Invalid Username or Password.'),
            ('unactive','Win.12345','User account is not currently active.'),       # 未激活的用户
            ('ficro','d','The user account has been locked.')      # 用户已锁定
)
@ddt.ddt
class LoginsTest(unittest.TestCase):

    @ddt.data(*testdata)
    @ddt.unpack
    def test_login(self, user, pw, mess):
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': uid,
            'Proxy-Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        headerout = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': uid
        }

        datas = '{"LanguageID":"en-us","UtcOffset":-480,"Flag":0,"AppName":"","ServiceType":"","MethodName":"LoginSystem",' \
                '"Parameters":["%s","%s",""],"RequestTime":633687529425210000}' % (user, pw)

        datat = parse.quote(datas)
        req = requests.post(url=url, data=datat, headers=headers)

        res = req.text.split('{')[-1:]
        res = res[0]
        print("\n当前登录用户： ",user)
        code = res.split(':')[1][0]
        expms = mess
        time.sleep(1)
        if code == "0":
            print("Test Pass! ")
            # G5项目中用户如已登录，之后须退出，否则下次再用此账号登录会提示 已在其他地方登录
            time.sleep(5)
            outdata = {'logout': 'logout'}
            logout = requests.post(url='http://192.168.25.105/T02/FIC5/loginSession.ashx', data=outdata,
                                   headers=headerout)
            print(logout.text)
        elif expms in res:
            print("Test Pass! ")
        else:
            print("Test Fail !")

if __name__ == '__main__':
    unittest.main()