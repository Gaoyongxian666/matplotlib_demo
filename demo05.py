# encoding: utf-8
'''
@author: gaoyongxian666
@file: demo05.py
@time: 2018/5/26 16:26
'''

# 散点图。散点图通常用于比较两个变量来寻找相关性或分组，如果你在 3 维绘制则是 3 个。
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]

# plt.scatter不仅允许我们绘制x和y，而且还可以让我们决定所使用的标记颜色，大小 25和类型。0代表circle
plt.scatter(x,y, label='skitscat', color='k', s=25, marker="o")
# 多个散点图就再写一个scatter就像多个条形图一样


plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
