# -*- coding:utf-8 -*-
# __Author__ = 曾良均

import urllib.request
from bs4 import BeautifulSoup as bs
import math
import tkinter
from tkinter import *
import tkinter.font as tf
import os
import base64
from fav import img

tl = []
root = None

class DobBallFI():
    def __init__(self, rt):
        di = DobBallFI.getdatas(self)
        redball = di['red']
        fullper = di['period']
        blueball = di['blue']

        if rt is None:
            self.t = tkinter.Tk()
        else:
            self.t = tkinter.Toplevel(rt)

        self.t.title("双色球预测")
        # 设置窗口图标
        self.setIcon()
        self.t.geometry('600x400')

        self.lab_input = Label(self.t, text="最新中奖：  ", font=('黑体', 12))
        self.lab_input.place(x=2, y=20)
        self.txt = Text(self.t, bd=1)
        ft = tf.Font(family='黑体', size=10)
        ft2 = tf.Font(family='黑体', size=11)
        self.txt.tag_add('tag', '1.0')
        self.txt.tag_config('tag', foreground='black', font=ft2)

        self.txt.tag_add('tag1', '2.0')
        self.txt.tag_config('tag1', foreground='blue', font=ft2)
        self.txt.tag_add('tag11', '2.5')
        self.txt.tag_config('tag11', foreground='black', font=ft)
        self.txt.tag_add('tag2', '3.0')
        self.txt.tag_config('tag2', foreground='red', font=ft2)

        self.txt.insert('1.0', "第" + fullper + " 期：", 'tag')
        self.txt.insert('2.0', redball, 'tag1')
        self.txt.insert('2.5', '  +  ', 'tag11')
        self.txt.insert('3.0', blueball, 'tag2')
        self.txt.place(x=5, y=50, width=300, height=25)

        self.btn_exe = Button(self.t, text="  下期预测  ", command=self.basedata)
        self.btn_exe.place(x=450, y=20)

        self.st = Text(self.t, wrap='word', font=('宋体', 10))
        self.st.place(x=5, y=80, width=560, height=240)
        self.st.configure(state=tkinter.DISABLED)


        self.labinfo = Label(self.t, text="  双色球预测工具 \n  作者：曾良均 \n  Ver: 0.1 (20210726) ")
        self.labinfo.place(x=420, y=340)

    def getdatas(self):

        url = "http://kaijiang.500.com/shtml/ssq/"
        html = urllib.request.urlopen(url, timeout=20).read().decode('gbk')
        # print(html)
        soup = bs(html, "html.parser")
        num = []
        for data in soup.find_all('li', class_='ball_red'):
            number = data.get_text
            number = str(number)[-8:-6]
            # print(number)
            number = int(number)
            num += [number]

        for data in soup.find_all('li', class_='ball_blue'):
            blue = data.get_text
            blue = str(blue)[-8:-6]
            blue = int(blue)

        for nums in soup.find_all('a', class_='iSelect'):
            period = nums.get_text
            period = str(period)[-10:-5]
            # print("第 %s 期 " %period)

        # print(num, blue)
        di = {'period':period, 'red':num, 'blue':blue}
        # print("第 %s 期中奖号码：" %period, end='')
        # print(num[0], num[1], num[2], num[3], num[4], num[5], end='')
        # print(" +", blue)
        return di

    def setIcon(self):
        tmp = open("tmp.ico", "wb+")
        tmp.write(base64.b64decode(img))
        tmp.close()
        self.t.iconbitmap("tmp.ico")
        os.remove("tmp.ico")

    def basedata(self):
        global current,redball,blueball,baseda,sums,fullper

        di = DobBallFI.getdatas(self)
        redball = di['red']
        per = di['period']
        fullper = int(di['period'])
        per = str(per)[-3:]
        current = int(per)
        blueball = di['blue']
        # 计算红球和值
        S = 0
        for i in range(0, 6):
            S = S + redball[i]
        # print("\n红球和值为： %d\n" % S)
        sums = S

        # 通过公式计算基数数字： （S-num(i))/num(i)
        Basedata = []
        based = ['']
        for i in range(0, 6):
            da = (S - redball[i]) / (redball[i])
            # print("计算出的数值为：%f" % da)
            # 截取小数点后一位
            da = math.floor(da * 10) / 10.0
            dd = str(da)[0] + str(da)[-1]
            Basedata += [dd]

            leng = len(dd)
            targ = dd
            for j in range(0, leng):
                tem = targ[j]
                if tem != '.':
                    bl = len(based)
                    k = 0
                    while tem != based[k]:
                        k += 1
                        if k == bl:
                            based += [tem]
                            break

        # 去除不是数字的元素
        based = [i for i in based if(len(str(i))!=0)]

        # 数组元素按升序排列
        based = sorted(based)
        datas = []
        for i in range(0, len(based)):
            temp = int(based[i])
            while temp < 34:
                if temp > 0:
                    datas += [temp]
                temp += 10

        datas = sorted(datas)
        nex = fullper + 1
        self.st.configure(state=tkinter.NORMAL)
        self.st.delete(1.0, tkinter.END)
        self.st.insert(tkinter.END, "第 %d 期红球预测： " % nex + '\n')
        for d in datas:
            self.st.insert(tkinter.END, str(d) + '  ')
        self.st.insert(tkinter.END, '\n')
        self.requireN()
        self.blueBallData()
        self.st.see(tkinter.END)
        self.st.update()
        self.st.configure(state=tkinter.DISABLED)


    def requireN(self):
        global redball,blueball,sums,current,fullper

        # 方法1： 蓝尾+红3尾=胆尾
        r3 = redball[2]
        r3 = str(r3)[-1]
        bl = str(blueball)[-1]
        m1 = int(r3) + int(bl)
        if m1 > 10:
            m1 = m1-10
        mf1 = []
        for i in range(0,4):
            tem = i * 10 + m1
            if tem < 34:
                if tem > 0:
                    mf1 += [tem]
        # print("胆码1： ", mf1)
        self.st.insert(tkinter.END, '\n')
        self.st.insert(tkinter.END, "胆码1： ")
        for mf in mf1:
            self.st.insert(tkinter.END, str(mf) + '  ')
        self.st.insert(tkinter.END,'\n')

        # 方法2：上期和值数值之和，如和值为113，则1+1+3=5，胆码数为 5+-1，即 4、5、6
        m2 = 0
        l = len(str(sums))
        for i in range(1, l + 1):
            sumnum = str(sums)[i-1]
            m2 += int(sumnum)
        # print("胆码2： ", m2-1, m2, m2+1)
        self.st.insert(tkinter.END, "胆码2： ")
        self.st.insert(tkinter.END, str(m2-1) + '  ' + str(m2) + '  ' + str(m2+1))
        self.st.insert(tkinter.END, '\n')

        # 方法3：上期红5-红1+2
        m3 = redball[4] - redball[0] + 2
        # print("胆码3： ", m3-1, m3, m3+1)
        self.st.insert(tkinter.END, "胆码3： ")
        self.st.insert(tkinter.END, str(m3-1) + '  ' + str(m3) + '  ' + str(m3+1))
        self.st.insert(tkinter.END, '\n')


        # 方法4：上期红5-红1 - 2
        m4 = redball[4] - redball[0] - 2
        # print("胆码4： ", m4-1, m4, m4+1)
        self.st.insert(tkinter.END, "胆码4： ")
        self.st.insert(tkinter.END,  str(m4-1) + '  ' + str(m4) + '  ' + str(m4+1))
        self.st.insert(tkinter.END, '\n')

        # 方法5：上上期期数 - 上期蓝号，作为尾码
        try:
            m5 = current -2 -blueball
            mf5 = []
            l = len(str(m5))
            for i in range(1, l + 1):
                n = str(m5)[i-1]
                for j in range(0,4):
                    k = j * 10 + int(n)
                    if k > 0:
                        if k < 34:
                            mf5 += [k]

            mf5 = list(set(mf5))    # 去重
            mf5 = sorted(mf5)    # 排序
            # print("胆码5：", mf5)
        except:
            self.st.insert(tkinter.END, "取胆码5方法异常")
        else:
            self.st.insert(tkinter.END, "胆码5： ")
            for m5 in mf5:
                self.st.insert(tkinter.END, str(m5) + '  ')
            self.st.insert(tkinter.END, '\n')

    def blueBallData(self):
        global redball,blueball,current,neneblue,fullper
        num = redball
        baseBlue = []
        bq = blueball

        # 方法1： 17-蓝
        b1 = 17 - bq
        baseBlue += [b1]
        # print("方法1过滤： %d" %b1)

        # 方法2： 19-蓝
        b2 = 19 - bq
        if b2 > 16:
            b2 = b2 -16
        baseBlue += [b2]
        # print("方法2过滤： %d" % b2)

        # 方法3： 21-蓝
        b3 = 21 - bq
        if b3 > 16:
            b3 = b3 -16
        baseBlue += [b3]
        # print("方法3过滤： %d" % b3)

        # 方法4：红3尾+蓝尾
        r3w = str(num[2])
        r3w = r3w[-1]
        bw = str(bq)[-1]
        b4 = int(r3w) + int(bw)
        if b4 > 16:
            b4 = b4 - 16
        baseBlue += [b4]
        # print("方法4过滤： %d" % b4)

        # 方法5： 红5-红2
        b5 = num[4] - num[1]
        if b5 > 16:
            b5 = b5 - 16
        baseBlue += [b5]
        # print("方法5过滤： %d" % b5)

        # 方法6： 红4-红1
        b6 = num[3] - num[0]
        if b6 > 16:
            b6 = b6 -16
        baseBlue += [b6]
        # print("方法6过滤： %d" % b6)

        # 方法7：红6尾+红1尾+5
        r6w = str(num[5])
        r6w = r6w[-1]
        r1w = str(num[0])
        r1w = r1w[-1]
        b7 = int(r6w) + int(r1w) + 5
        if b7 > 16:
            b7 = b7 - 16
        baseBlue += [b7]
        # print("方法7过滤： %d" % b7)

        # 方法8： 红4尾+1
        r4w = str(num[3])
        r4w = r4w[-1]
        b8 = int(r4w) + 1
        baseBlue += [b8]
        # print("方法8过滤： %d" % b8)

        # 方法9： 红1*2+6
        b9 = num[0] * 2 + 6
        if b9 > 16:
            b9 = b9 - 16
        baseBlue += [b9]
        # print("方法9过滤： %d" % b9)

        # 方法10： 红1+7
        b10 = num[0] + 7
        if b10 > 16:
            b10 = b10 - 16
        baseBlue += [b10]
        # print("方法10过滤： %d" % b10)

        # 方法11：期尾 + 5
        # inp = input("\n请输入当前期次： ")
        inpt = str(current)[-1]
        b11 = int(inpt) + 5
        baseBlue += [b11]
        # print("方法11过滤： %d" %b11)

        '''
        # 方法12： 上两期蓝尾之和
        try:
            s2 = str(neneblue)[-1]
        except:
            lasts = int(current) - 2
            neneblue = input("\n请输入 %d 期蓝球号： " %lasts)
            s2 = str(neneblue)[-1]
    
        s1q = str(bq)[-1]
        b12 = int(s2) + int(s1q)
        if b12 > 16:
            b12 = b12 -16
        baseBlue += [b12]
        # print("方法12过滤： %d" %b12)
        '''

        bluedata = list(set(baseBlue))
        bluedata = sorted(bluedata)
        # print("要过滤的蓝球号有：", end='')
        # print(bluedata)
        blueba = []
        for i in range(1,16):
            if i not in bluedata:
                blueba += [i]
        ne = fullper + 1
        # print("\n第 %d 期蓝球备选号有： " %ne,blueba)
        self.st.insert(tkinter.END, "\n第 %d 期蓝球预测： " %ne)
        for bb in blueba:
            self.st.insert(tkinter.END, str(bb) + '  ')




if __name__ == '__main__':
    tl.append(DobBallFI(root))
    root = tl[0].t
    root.mainloop()
