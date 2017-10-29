#coding:utf-8
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

data=[547,360,178,81,477,504,2241]
labels=[u'一',u'二',u'三',u'四',u'五',u'六',u'七']
cols=['c','m','red','blue','yellowgreen','gold','lightskyblue']
plt.axis('equal')
#饼图
plt.pie(data,labels=labels,autopct='%1.1f%%',colors=cols)
plt.title(u'top7关注分布图')

plt.savefig("pie_7.png")
plt.show()
