#! encoding:utf-8
from tkinter import *
import base64

open_icon = open("favicon.ico", "rb")  # 要放入的图标文件
b64str = base64.b64encode(open_icon.read())  # 以Base64的格式读出
open_icon.close()
write_data = "img=%s" % b64str
f = open("fav.py", "w+")
f.write(write_data)
f.close()