# coding:utf-8

import json
import requests
url = 'http://iatc.soft.rz/portal/Login.aspx'

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'iatcg5session=IuZHbEdnnODbaC9w2DqsdVkYMNKCxy5a1HKVUGIEwUHSKoYNIx7DcdquGFewOHeQ',
    'Proxy-Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

username = 'zlj@iatc.com'
password = 'Zljun8210'

data = {
    'tp':'Dologin',
    'uid':username,
    'pwd':password,
    'termid':-1,
    'rememberme':0,
    'jumpto':''
}

req = requests.post(url=url, data=data, headers=headers)
list = []
for a in req.text.split(','):
    list += [a]

resu = list[0].split(':')[1]

if resu !=str(0):
    mess = list[1].split(':')[1]
    mess = mess[1:-1]
    print("登录失败！ ")
    print(mess)
else:
    jumpurl = list[2][11:-1]
    print("登录成功！ ")
    print('跳转到： ', jumpurl)
