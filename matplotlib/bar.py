#coding:utf-8
import matplotlib.pyplot as plt
#柱状图
#为了输出汉语 u'汉语'
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
#from matplotlib.font_manager import FontProperties

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2.,1.03*height, "%s" % float(height))

#title标题/Axis轴/label坐标轴标注/tick刻度线/tick label刻度标注

plt.xlabel(u"性别")
plt.ylabel(u"人数")
plt.xticks((0,1),(u"男",u"女"))
plt.title(u"性别比例分析")
rect=plt.bar(left=(0,1),height=(1,0.5),width=0.35,align="center",yerr = 0.000001)
#yerr为了使柱状图不是顶到顶

plt.legend((rect,),(u"图例",))
autolabel(rect)
plt.show()
