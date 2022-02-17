#! encoding:utf-8
import os, base64
import time
import logging
import xlrd
from fav import img

try:
    from lxml import etree
except ImportError:
    import xml.etree.cElementTree as etree
import tkinter
from tkinter import messagebox
from tkinter import filedialog
from tkinter import *

t1 = []
root = None
# 获取当前有时间，用于输出日志
fmt = time.strftime("%m/%d %H:%M:%S", time.localtime()) + '>> '

__author__ = {
    'name': '曾良均',
    'QQ':'277099728',
    'Email':'zlj-316731@163.com',
    'Blog':'https://blog.csdn.net/zljun8210',
    'Created':'2017-07-03'}

# 设置logger配置
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='./test.log',
                    filemode='w')


class Converter():
    path = "./"

    def __init__(self, rt):
        if rt is None:
            self.t = tkinter.Tk()
        else:
            self.t = tkinter.Toplevel(rt)

        self.t.title("xls2xml转换器")
        # 设置窗口图标
        self.setIcon()
        self.t.geometry('600x400')

        self.lab_input = Label(self.t, text=" 源文件：  ")
        self.lab_input.place(x=2, y=20)
        self.ent = Entry(self.t, bd=1)
        self.ent.place(x=80, y=20, width=300)
        self.btn = Button(self.t, text="  打开 ", command=self.callback)
        self.btn.place(x=460, y=20)

        self.btn_exe = Button(self.t, text="  转换  ", command=self.tcConvert)
        self.btn_exe.place(x=520, y=20)

        self.st = Text(self.t, wrap='word')
        self.st.place(x=5, y=80, width=560, height=260)
        self.st.configure(state=tkinter.DISABLED)
        sb = Scrollbar(self.st, orient=VERTICAL)
        sb["command"] = self.st.yview()
        self.st["yscrollcommand"] = sb.set
        sb.pack(side=RIGHT, fill='both')
        # sl = Scrollbar(self.st, orient=HORIZONTAL)
        # sl["command"] = self.st.xview()
        # self.st["xscrollcommand"] = sl.set
        # sl.pack(side=BOTTOM, fill='both')

        self.labinfo = Label(self.t, text="  Testlink软件之XLS转XML工具 \n  作者：曾良均 \n  Ver: 0.6 (20210604) ")
        self.labinfo.place(x=420, y=350)

    def setIcon(self):
        tmp = open("tmp.ico", "wb+")
        tmp.write(base64.b64decode(img))
        tmp.close()
        self.t.iconbitmap("tmp.ico")
        os.remove("tmp.ico")

    # 选取文件路径
    def callback(self):
        self.ent.delete(0, END)
        # 清空entry里面的内容
        # 调用filedialog模块的askdirectory()函数去打开文件夹
        # filepath = tkFileDialog.askdirectory()
        filepath = filedialog.askopenfilename()
        if filepath:
            self.ent.insert(0, filepath)  # 将选择好的路径加入到entry里面

    @staticmethod
    def openfilename():
        filename = filedialog.asksaveasfilename(filetypes=[("打开文件", "*.xls")])

        if filename:
            return open(filename, 'w', encoding='utf8')

    # 转换函数
    def tcConvert(self):
        path = self.ent.get()
        print(self.ent.get())
        logging.debug('转换的Excel文件为 ' + path)
        self.st.configure(state=tkinter.NORMAL)
        self.st.insert(tkinter.END, '转换的Excel文件为 ' + path + '\n')
        tfn = path.split("/")[-1]
        ofn = tfn.split(".")[0]
        # print("文件名是： " + ofn)
        self.st.insert(tkinter.END, '转换后的文件名是： ' + ofn + '.xml')
        logging.debug('转换后的文件名： ' + ofn + '.xml')
        if path == "":
            tkinter.messagebox.showinfo("Messages", "请打开有效的xls文件！")

        f_in = xlrd.open_workbook(path)
        if f_in:
            logging.debug("    ----  开始转换  ----  ")
            self.st.insert(tkinter.END, "\n    ----  开始转换  ----  \n" + '\n')
            self.st.update()

        sheet = f_in.sheet_by_index(0)
        # create XML
        testcases = etree.Element('testcases')

        # print("row = %d" % sheet.nrows)
        cases = int(sheet.nrows) - 1
        logging.debug('一共有 %d 个用例' % cases)
        self.st.insert(tkinter.END, fmt + '一共有 %d 个用例' % cases + '\n')
        # self.st.see(tkinter.END)
        self.st.update()

        def format_str(rawstr):
            rawstr = "<p>" + rawstr + "</p>"
            return rawstr

        for seq in range(1, sheet.nrows):
            print(seq)
            self.st.insert(tkinter.END, fmt + '第 %d 个用例 ' % seq + '\n')
            self.st.update()

            logging.debug('第 %d 个用例 ' % seq)
            try:
                name_ = sheet.row_values(seq)[0]
                summary_ = sheet.row_values(seq)[1]
                pre_ = sheet.row_values(seq)[2]
                importance_ = sheet.row_values(seq)[3]
                step_ = sheet.row_values(seq)[4]
                expect_ = sheet.row_values(seq)[5]
                exe_type_ = sheet.row_values(seq)[6]

                test_case = etree.SubElement(testcases, 'testcase', name=name_)
                logging.debug('测试用例名: ' + name_)
                self.st.insert(tkinter.END, fmt + '测试用例名: ' + name_ + '\n')
                self.st.update()

                summary = etree.SubElement(test_case, 'summary')
                summary.text = format_str(summary_)
                # print(summary.text)
                # logging.debug('summary.text====' + summary.text)

                preconditions = etree.SubElement(test_case, 'preconditions')
                # print(pre_)
                # preconditions.text = u'"{0}"'.format(pre_)
                pre_ = pre_.replace("\n", "</br>")
                # print(pre_)
                preconditions.text = format_str(pre_)
                # print(preconditions.text)

                # <importance><![CDATA[2]]></importance>
                importance_level = etree.SubElement(test_case, 'importance')
                importance_level.text = str(int(importance_))
                # print(importance_level.text)

                steps = etree.SubElement(test_case, 'steps')
                step = etree.SubElement(steps, 'step')
                step_number = etree.SubElement(step, 'step_number')
                step_number.text = str(1)

                # Transform the steps
                actions = etree.SubElement(step, 'actions')
                # actions.text = u'"{0}"'.format(step_)
                step_ = step_.replace("\n", "</br>")
                # print(step_)
                actions.text = format_str(step_)
                # print(actions.text)
                expectedresults = etree.SubElement(step, 'expectedresults')

                # expectedresults.text = u'"{0}"'.format(expect_)
                expect_ = expect_.replace("\n", "</br>")
                # print(expect_)
                expectedresults.text = format_str(expect_)
                # print(expectedresults.text)

                execution_type = etree.SubElement(step, 'execution_type')
                execution_type.text = str(int(exe_type_))
                # print(execution_type.text)

                try:
                    keyword_ = sheet.row_values(seq)[7]
                    keywords = etree.SubElement(test_case, 'keywords')
                    # logging.info('开始提取关键字到临时文件')
                    tmpf = open("tmp.txt", 'w', encoding='utf-8')
                    tmpf.write(keyword_)
                    tmpf.close()
                    outf = open("tmp.txt", 'r', encoding='utf-8')
                    for line in outf.readlines():
                        keyword = etree.SubElement(keywords, 'keyword', name=line)
                        # line = line.replace("\n", "</br>")
                        # print(line)
                        keyword.text = format_str(line)
                        # print(keyword.text)

                    outf.close()
                    os.remove("tmp.txt")

                except Exception as e:
                    print("没有关键字属性！！")

            except Exception as e:
                print("line:", seq)
                print(str(e))
                for item in sys.exc_info():
                    print(item())

        # s = etree.tostring(testcases, pretty_print=True)
        s = etree.tostring(testcases)
        pathlist = path.split("/")
        pathlist.pop()
        newpath = '/'.join(pathlist)
        f_out = open(newpath + "/" + ofn + ".xml", 'w')
        f_out.write(s.decode("utf-8"))
        logging.debug('测试用例转换完成！！')
        self.st.insert(tkinter.END, '\n' + '测试用例转换完成！！' + '\n')
        self.st.see(tkinter.END)
        self.st.update()
        self.st.configure(state=tkinter.DISABLED)

        tkinter.messagebox.showinfo("Messages", "Convert Successfully.\n Save file to " + ofn + ".xml .")


if __name__ == '__main__':
    root = None
    t1.append(Converter(root))
    root = t1[0].t
    root.mainloop()
