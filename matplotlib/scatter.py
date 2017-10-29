#coding:utf-8
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
#前面四行中的三行是为了避免matplotlib中的图像不能显示中文
import numpy as np
N = 1000
x = np.random.randn(N)
y = np.random.randn(N)

color = ['r','y','k','g','m']
#散点图
plt.scatter(x,y,c=color,marker='o',alpha=0.9,edgecolors='w')
#分析scatter函数：
#scatter(x,y,s=None,maker=None,cmap=None,
    # norm=None,vmin=None,vmax=None,alpha=None
    #linewidths=None,verts=None,edgecolors=None,
    #hold=None,data=None,**kwargs)
#x,y形如shape(n,)的数组，可选值,s点面积默认20，c点颜色或颜色序列默认蓝色
#其他如r/g/k--black/y
#maker形状./,-pixel/o-circle/v/^/</>/1/2/3/4/8/s/p/P-不行/*/h/H/+/x/X/D
#alpha透明程度 0-1之间
#edgecolors边缘颜色或颜色序列，可选颜色

plt.show()
