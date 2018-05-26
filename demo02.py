# encoding: utf-8
'''
@author: gaoyongxian666
@file: demo02.py
@time: 2018/5/26 16:16
'''

# Matplotlib 数据可视化模块的多个方面。
# Matplotlib :
# 能够创建多数类型的图表，如条形图，散点图，条形图，饼图，堆叠图，3D 图和地图图表。

import matplotlib.pyplot as plt
# 这一行是导入集成的pyplot，我们将在整个系列中使用它。
# 我们将pyplot导入为plt，这是使用pylot的 python 程序的传统惯例。

plt.plot([1,2,3],[5,7,4])
# plot的.plot方法绘制一些坐标。
# 这个.plot需要许多参数，但前两个是'x'和'y'坐标，我们放入列表。
# 这意味着，根据这些列表我们拥有 3 个坐标：1,5 2,7和3,4。

plt.show()

