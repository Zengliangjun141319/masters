# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     AdduserTest.py
   Description :
   Author :        曾良均
   QQ:             277099728
   Date：          8/13/2021 4:35 PM
-------------------------------------------------
   Change Activity:
                   8/13/2021:
-------------------------------------------------
"""
__author__ = 'ljzeng'

import unittest
import requests
from urllib import parse
import time
import ddt
import os
from excel import excel

# site = '5ZSAMRFPL4YAWA'
site = 'GUYG95YLHMXW'    # 正式087站点
loginuser = 'admin@iicon004.com'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

file_path = r"D:\Mydoc\pythonp\demo\userlist.xlsx"
testData = excel.get_list(file_path)

s = requests.session()
global iiabc

@ddt.ddt
class AdduserTest(unittest.TestCase):

    def setup(self):
        pass

    def login(self):
        global iiabc
        # url = 'http://iron.soft.rz/login/Login.aspx?tp=dologin'
        url = 'https://fleet.foresightintelligence.com/Login.aspx?tp=dologin'
        # username = 'admin@iicon004.com'
        password = 'Win.12345'
        loginuser = 'zljun8210@live.cn'
        ss = loginuser + 'ª' + password
        payload = ss.encode('utf8')
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
            'Content-Type': 'text/plain;charset=UTF-8'}

        req = s.post(url=url, data=payload, headers=headers)
        # print(req.cookies.get_dict())
        iiabc = str(req.cookies.get_dict()).split("'")[3]
        # print(iiabc)
        # print(req.text)

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
            print('跳转到： ', jumpurl)

    def tearDown(self):
        pass

    def addusergroup(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'user-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        }
        ugroup = 'http://iron.soft.rz/custsites/' + site + '/Security/UserGroup.aspx'

        saveM = 'MethodID=-1&MethodName=SaveGroup&ClientData='
        groupname = 'testgroup01'
        groupdata = '{"GroupInfo":{"Name":"%s","Notes":"","Users":[{"IID":"CABBC300-91F2-4B9A-82AF-AD302167EFE3"},{"IID":"CEA262A8-B055-40E4-861A-892BA52E380E"}]},"Features":[]}' %groupname
        savegdata = saveM + parse.quote(groupdata)    # 对参数内容进行URL编码
        addgr = s.post(url=ugroup, headers=header, data=savegdata)
        print("\n添加用户组: ", addgr.text)

        getug = s.post(url=ugroup, headers=header, data='MethodID=-1&MethodName=GetGroups&ClientData=')
        print("\n用户组： ", getug.text)



    def adduser(self, data):
        global iiabc
        # print(iiabc)
        adduserurl = 'http://iron.soft.rz/custsites/' + site + '/Security/AddUser.aspx'

        addheaders = {
            'Accept':'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With':'XMLHttpRequest',
            'Cookie': 'ir_lusname_=%s; iiabc_lang=en-us; iiabc_=%s; basemap=topo;' %(loginuser,iiabc),
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'user-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        }

        header = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'user-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        }

        id = 'admin4@iicon004.com'
        displayname = 'admins'
        pwd = 'Win.12345'


        ClientData = '{"UserInfo":{"ID":"%s","DisplayName":"%s","TextAddress":"","Mobile":"","BusinessPhone":"","Active":true,"UserType":"2","IsUser":true,"AllowLoginIntoPC":false,"AllowLoginIntoInspectMobile":false,"AllowLoginIntoFleetMobile":false,"AllowMobileBarcodeScanning":false,"ContactType":"100","ManagerIID":"","Notes":"","EmailOptOut":false,"InspectEmailList":false,"TeamIntelligenceUser":false,"FOB":"","HourlyRate":-1,"LandingPage":"MapView.aspx","PreferredLanguage":"","TransPass":"%s"},"Subscribe":null,"Features":[{"Key":100,"Value":["0"]},{"Key":220,"Value":["0"]},{"Key":600,"Value":["0"]},{"Key":601,"Value":["0"]},{"Key":602,"Value":["0"]},{"Key":1000,"Value":["0"]}],"Schedule":{"$type":"FI.FIC.EmailSchedule, FICBLC","ScheduleItems":{"$type":"FI.FIC.EmailScheduleItem[], FICBLC","$values":[]}}}' %(id, displayname, pwd)
        data = 'MethodID=-1&MethodName=AddUser&ClientData=' + parse.quote(ClientData)    # 对参数内容进行URL编码

        # print("\n请求头： \n", addheaders)

        # print(data)
        time.sleep(1)
        adduserRes = s.post(url=adduserurl, headers=addheaders, data=data)
        print("\n添加用户: ", adduserRes.text)

        usermanurl = 'http://iron.soft.rz/custsites/' + site + '/Security/UserManage.aspx'
        getuserres = s.post(url=usermanurl, headers=header, data='MethodID=-1&MethodName=GetUsers&ClientData=')
        # print("\n用户列表： \n", getuserres.text)

    def addAssets(self):
        url = 'http://iron.soft.rz/custsites/' + site + '/MachineDeviceManagement/AddMachine.aspx'
        header = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'user-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        }
        methods = 'MethodID=-1&MethodName=SaveMachine&ClientData='
        assetInfo = '{"VIN":"20210816N003","Name":"20210816N003","Name2":"20210816N003","MakeYear":"2009","MakeID":"506","MakeName":" _TEST","ModelID":"15087","ModelName":"0000","TypeID":-1,"EngineHours":-1,"ContractorID":"","ODOMeter":-1,"OdometerUnits":"","UnderCarriageHours":-1,"OnSiteJobsiteIDs":[],"ContactIDs":[],"MachineGroupIDs":[],"AquisitionType":"","Hidden":false,"OnRoad":false,"TelematicsEnabled":false,"Attachment":false,"CostCenter":"","EQClass":"","Description":"","ID":-1,"MachineAttributes":[{"ID":67,"DisplayText":"Always On","Format":"VARCHAR(30)","Description":"Select Yes to notify that asset has been turned off.  Must subscribe to alert.","DataType":0,"Multiline":false,"Length":30,"Precision":0,"Value":"No","Dropdown":true,"DataSource":"No;Yes"},{"ID":93,"DisplayText":"Current Jobsite Completion","Format":"DATETIME2","Description":"Jobsite Complete Date","DataType":4,"Multiline":false,"Length":100,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":69,"DisplayText":"Next Jobsite Assignment","Format":"VARCHAR(100)","Description":"Next Jobsite Assignment","DataType":0,"Multiline":false,"Length":100,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":70,"DisplayText":"Future Assignment Date","Format":"DATETIME2","Description":"Future Assignment Date","DataType":4,"Multiline":false,"Length":100,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":71,"DisplayText":"Custom Status","Format":"VARCHAR(100)","Description":"Custom Status","DataType":0,"Multiline":false,"Length":100,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":31,"DisplayText":"Fuel Cost","Format":"DECIMAL(18,2)","Description":"GENERAL ATTRIBUTES","DataType":3,"Multiline":false,"Length":18,"Precision":2,"Value":"","Dropdown":false,"DataSource":""},{"ID":32,"DisplayText":"Fuel Cost UOM","Format":"VARCHAR(10)","Description":"GENERAL ATTRIBUTES","DataType":0,"Multiline":false,"Length":10,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":33,"DisplayText":"Machine Rate","Format":"DECIMAL(18,2)","Description":"GENERAL ATTRIBUTES","DataType":3,"Multiline":false,"Length":18,"Precision":2,"Value":"","Dropdown":false,"DataSource":""},{"ID":36,"DisplayText":"Work Type","Format":"VARCHAR(100)","Description":"GENERAL ATTRIBUTES","DataType":0,"Multiline":false,"Length":100,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":58,"DisplayText":"Fuel Type","Format":"VARCHAR(50)","Description":"GENERAL ATTRIBUTES","DataType":0,"Multiline":false,"Length":50,"Precision":0,"Value":"Diesel","Dropdown":true,"DataSource":"Diesel;Gas"},{"ID":61,"DisplayText":"Fuel Card ID","Format":"VARCHAR(20)","Description":"GENERAL ATTRIBUTES","DataType":0,"Multiline":false,"Length":20,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":68,"DisplayText":"Fuel Tank Size","Format":"DECIMAL(18,2)","Description":"GENERAL ATTRIBUTES","DataType":3,"Multiline":false,"Length":18,"Precision":2,"Value":"","Dropdown":false,"DataSource":""},{"ID":74,"DisplayText":"Load Capacity (tons)","Format":"int","Description":"GENERAL ATTRIBUTES","DataType":1,"Multiline":false,"Length":100,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":39,"DisplayText":"Lease Start Date","Format":"datetime2","Description":"LEASE MANAGEMENT","DataType":4,"Multiline":false,"Length":100,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":40,"DisplayText":"Lease End Date","Format":"datetime2","Description":"LEASE MANAGEMENT","DataType":4,"Multiline":false,"Length":100,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":42,"DisplayText":"Lease Term","Format":"int","Description":"LEASE MANAGEMENT","DataType":1,"Multiline":false,"Length":100,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":59,"DisplayText":"Lease Term UOM","Format":"VARCHAR(50)","Description":"LEASE DETAILS","DataType":0,"Multiline":false,"Length":50,"Precision":0,"Value":"Hours","Dropdown":true,"DataSource":"Hours;Miles;Kilometers"},{"ID":60,"DisplayText":"Overage per unit","Format":"DECIMAL(18,2)","Description":"LEASE DETAILS","DataType":3,"Multiline":false,"Length":18,"Precision":2,"Value":"","Dropdown":false,"DataSource":""},{"ID":1,"DisplayText":"Acquisition Cost","Format":"DECIMAL(18,2)","Description":"THIS IS CAPTURE ACQUISITION COST FOR MACHINES FOR LIFECYCLE MANAGEMENT","DataType":3,"Multiline":false,"Length":18,"Precision":2,"Value":"","Dropdown":false,"DataSource":""},{"ID":2,"DisplayText":"Vendor","Format":"VARCHAR(100)","Description":"CAPTURE VENDOR EQUIPMENT WAS AQUIRED FROM ","DataType":0,"Multiline":false,"Length":100,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":3,"DisplayText":"Acquisition Date","Format":"DATETIME2","Description":"CAPTURE AQUISITION DATE","DataType":4,"Multiline":false,"Length":100,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":37,"DisplayText":"Retirement Hours","Format":"DECIMAL(18,2)","Description":"LIFECYCLE MANAGEMENT","DataType":3,"Multiline":false,"Length":18,"Precision":2,"Value":"","Dropdown":false,"DataSource":""},{"ID":5,"DisplayText":"Sale Value","Format":"DECIMAL(18,2)","Description":"CAPTURE SALE VALUE","DataType":3,"Multiline":false,"Length":18,"Precision":2,"Value":"","Dropdown":false,"DataSource":""},{"ID":7,"DisplayText":"Sold To","Format":"VARCHAR(100)","Description":"CAPTURE WHO EQUIPMENT WAS SOLD TO","DataType":0,"Multiline":false,"Length":100,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":8,"DisplayText":"Sale Date","Format":"DATETIME2","Description":"CAPTURE SALE DATE","DataType":4,"Multiline":false,"Length":100,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":9,"DisplayText":"Acquisition Hours","Format":"DECIMAL(18,2)","Description":"CAPTURE HOURS AT TIME OF ACQUISITION","DataType":3,"Multiline":false,"Length":18,"Precision":2,"Value":"","Dropdown":false,"DataSource":""},{"ID":10,"DisplayText":"Acquisition Odometer","Format":"DECIMAL(18,2)","Description":"CAPTURE ODOMETER READING AT TIME OF ACQUISITION","DataType":3,"Multiline":false,"Length":18,"Precision":2,"Value":"","Dropdown":false,"DataSource":""},{"ID":64,"DisplayText":"Hourly Cost of Idle","Format":"DECIMAL(18,2)","Description":"Hourly Cost of Idle","DataType":3,"Multiline":false,"Length":18,"Precision":2,"Value":"","Dropdown":false,"DataSource":""},{"ID":65,"DisplayText":"Target Idle Percent","Format":"DECIMAL(18,2)","Description":"Target Idle Percent","DataType":3,"Multiline":false,"Length":18,"Precision":2,"Value":"","Dropdown":false,"DataSource":""},{"ID":87,"DisplayText":"Error Message","Format":"VARCHAR(300)","Description":"Error Message","DataType":0,"Multiline":false,"Length":300,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":90,"DisplayText":"Telematic Comments","Format":"VARHCAR(300)","Description":"Telematics Comments","DataType":0,"Multiline":false,"Length":1000,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":51,"DisplayText":"License Tag","Format":"VARCHAR(30)","Description":"OTR ATTRIBUTES","DataType":0,"Multiline":false,"Length":30,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":52,"DisplayText":"License Tag Date","Format":"DATETIME2","Description":"OTR ATTRIBUTES","DataType":4,"Multiline":false,"Length":100,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":53,"DisplayText":"Inspection Date","Format":"DATETIME2","Description":"OTR ATTRIBUTES","DataType":4,"Multiline":false,"Length":100,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":54,"DisplayText":"DOT ID 1","Format":"VARCHAR(30)","Description":"OTR ATTRIBUTES","DataType":0,"Multiline":false,"Length":30,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":55,"DisplayText":"DOT ID 2","Format":"VARCHAR(30)","Description":"OTR ATTRIBUTES","DataType":0,"Multiline":false,"Length":30,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":56,"DisplayText":"GVWR","Format":"DECIMAL(18,2)","Description":"Gross Vehicle Weight Rating","DataType":3,"Multiline":false,"Length":18,"Precision":2,"Value":"","Dropdown":false,"DataSource":""},{"ID":57,"DisplayText":"Toll Pass","Format":"VARCHAR(20)","Description":"OTR ATTRIBUTES","DataType":0,"Multiline":false,"Length":20,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":63,"DisplayText":"Asset Size","Format":"VARCHAR(20)","Description":"This determines classification for thresholds for Driver Behavior alerts/charts.","DataType":0,"Multiline":false,"Length":20,"Precision":0,"Value":"","Dropdown":true,"DataSource":";Passenger;Small Truck/Van;Large Truck"},{"ID":95,"DisplayText":"Sales Tax","Format":"DECIMAL(18,2)","Description":"Sales Tax","DataType":3,"Multiline":false,"Length":18,"Precision":2,"Value":"","Dropdown":false,"DataSource":""},{"ID":96,"DisplayText":"Property Tax","Format":"DECIMAL(18,2)","Description":"Property Tax","DataType":3,"Multiline":false,"Length":18,"Precision":2,"Value":"","Dropdown":false,"DataSource":""}],"IgnoreDuplicate":false}'
        data = methods + parse.quote(assetInfo)

        res = s.post(url, headers=header, data=data)
        print("\n添加机器: ", res.text)

    def resetpw(self):
        global iiabc
        url = 'http://iron.soft.rz/custsites/' + site + '/Security/UserManage.aspx'
        header = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'ir_lusname_=%s; iiabc_lang=en-us; iiabc_=%s; basemap=topo;' %(loginuser,iiabc),
            'user-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        }
        userid = '313746C7-6D75-4A6B-A15D-700869B8C151'
        resetpw = 'Win.123456'
        data = 'MethodID=-1&MethodName=ResetPassword&ClientData=' + userid + '%C2%AA' + resetpw


        result = s.post(url=url, headers=header, data=data)
        print("重置密码： ", result.text)

    def test01_group(self):
        self.login()
        # self.addusergroup()

    def test02_something(self):
        # self.adduser()
        pass

    @ddt.data(*testData)
    def test02_adduser(self, data):
        global iiabc
        adduserurl = 'https://fleetportal1.foresightintelligence.com/custsites/' + site + '/Security/AddUser.aspx'

        addheaders = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'Cookie': 'ir_lusname_=%s; iiabc_lang=en-us; iiabc_=%s; basemap=topo;' % (loginuser, iiabc),
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'user-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        }

        header = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'user-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        }

        '''正式站点IICON261'''
        uid = data["UID"]
        displayname = data["Dname"]
        FOB = data["FOB"]
        ClientData = '{"UserInfo":{"ID":"%s","DisplayName":"%s","TextAddress":"","Mobile":"","BusinessPhone":"","Active":true,"UserType":"1","IsUser":true,"AllowLoginIntoPC":true,"AllowLoginIntoInspectMobile":true,"AllowLoginIntoFleetMobile":true,"AllowMobileBarcodeScanning":true,"ContactType":"6","ManagerIID":"","Notes":"","AssignedWorkOrders":false,"EmailOptOut":false,"InspectEmailList":false,"TeamIntelligenceUser":false,"FOB":"%s","HourlyRate":-1,"LandingPage":"Maintenance/Maintenance.aspx#nav_workorder","PreferredLanguage":"en-us","TransPass":"Welcome1"},"Subscribe":null,"Features":[{"Key":100,"Value":["0"]},{"Key":210,"Value":["99999"]},{"Key":235,"Value":["0"]},{"Key":237,"Value":["0"]},{"Key":245,"Value":["0"]},{"Key":600,"Value":["0"]},{"Key":601,"Value":["0"]},{"Key":602,"Value":["0"]},{"Key":1100,"Value":["0"]},{"Key":1101,"Value":["99999"]}],"Schedule":{"$type":"FI.FIC.EmailSchedule,+FICBLC","ScheduleItems":{"$type":"FI.FIC.EmailScheduleItem[],+FICBLC","$values":[]}}}' % (
        uid, displayname, FOB)

        data = 'MethodID=-1&MethodName=AddUser&ClientData=' + parse.quote(ClientData)  # 对参数内容进行URL编码

        time.sleep(1)
        adduserRes = s.post(url=adduserurl, headers=addheaders, data=data)
        print("\n添加用户: ", adduserRes.text)


    def test03_AssetManage(self):
        # self.addAssets()
        pass

    def test04_Resetpw(self):
        # self.resetpw()
        pass


if __name__ == '__main__':
    unittest.main()
