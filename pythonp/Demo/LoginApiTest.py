# coding:utf-8

import requests
from urllib import parse
import time

url = 'http://iron.soft.rz/login/Login.aspx?tp=dologin'
username = 'admin@iicon001.com'
password = 'Win.12345'
ss = username + 'ª' + password
payload = ss.encode('utf8')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    'Content-Type': 'text/plain;charset=UTF-8'}

s = requests.session()
req = s.post(url=url, data=payload, headers=headers)
# print(req.cookies.get_dict())

list = []
for a in req.text.split(','):
    list += [a]

resu = list[0].split(':')[1]

if resu != str(0):
    mess = list[1].split(':')[1]
    mess = mess[1:-1]
    print("登录失败！ ")
    print(mess)
else:
    jumpurl = list[2][11:-1]
    print("登录成功！ ")
    # print('跳转到： ', jumpurl)


adduserurl = 'http://iron.soft.rz/custsites/YDJJJGAXCJLYDQ/Security/AddUser.aspx'
addheaders = {
            'Accept':'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding':'gzip, deflate',
            'X-Requested-With':'XMLHttpRequest',
            'Referer': adduserurl,
            'Cookie': '_ir_lusname_=admin@iicon001.com; iiabc_lang=en-us; iiabc_=K4XMqer8k3xMOq2DALQL/XsHTkcORK7hZ3Og2UxT0xYBDixAKg/SV1k92aEe/Rkd; basemap=topo',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'user-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        }

header = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'user-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        }

id = 'admin2@iicon001.com'
displayname = 'admins'
pwd = 'Win.12345'

ClientData = '{"UserInfo":{"ID":"\\%s","DisplayName":"\\%s","TextAddress":"","Mobile":"","BusinessPhone":"","Active":true,"UserType":"2","IsUser":true,"AllowLoginIntoPC":false,"AllowLoginIntoInspectMobile":false,"AllowLoginIntoFleetMobile":false,"AllowMobileBarcodeScanning":false,"ContactType":"100","ManagerIID":"","Notes":"","EmailOptOut":false,"InspectEmailList":false,"TeamIntelligenceUser":false,"FOB":"","HourlyRate":-1,"LandingPage":"MapView.aspx","PreferredLanguage":"","TransPass":"\\%s"},"Subscribe":null,"Features":[{"Key":100,"Value":["0"]},{"Key":220,"Value":["0"]},{"Key":600,"Value":["0"]},{"Key":601,"Value":["0"]},{"Key":602,"Value":["0"]},{"Key":1000,"Value":["0"]}],"Schedule":{"$type":"FI.FIC.EmailSchedule, FICBLC","ScheduleItems":{"$type":"FI.FIC.EmailScheduleItem[], FICBLC","$values":[]}}}' %(id, displayname, pwd)
data = 'MethodID=-1&MethodName=AddUser&ClientData=' + parse.quote(ClientData)

# adduserRes = s.post(url=adduserurl, headers=addheaders, data=data, timeout=5)
# print("\n添加用户: ", adduserRes.text)

time.sleep(6)

logoutUrl = 'http://iron.soft.rz/custsites/YDJJJGAXCJLYDQ/commonpage.aspx'
odata = 'action=logout'
logout = s.post(url=logoutUrl, headers=addheaders, data=odata)
# print(logout.text)
print(logout.status_code)