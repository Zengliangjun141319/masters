from RequestData import getdatas

datas = {}
datas = getdatas()
# print(datas)
reds = []

per = datas['period']
reds = datas['red']
blue = datas['blue']

print("当期： ", per)
print("红球： ", reds[0], reds[1], reds[2], reds[3], reds[4], reds[5])
print("蓝球： ", blue)

