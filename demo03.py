# encoding: utf-8
'''
@author: gaoyongxian666
@file: demo03.py
@time: 2018/5/26 16:20
'''


# 图例、标题和标签
# 注：轴域（Axes）即两条坐标轴围城的区域。
import matplotlib.pyplot as plt

x = [1,2,3]
y = [5,7,4]

x2 = [1,2,3]
y2 = [10,14,12]


# 画两条线条
plt.plot(x, y, label='First Line')
plt.plot(x2, y2, label='Second Line')

# 使用plt.xlabel和plt.ylabel，我们可以为这些相应的轴创建标签。
plt.xlabel('Plot Number')
plt.ylabel('Important var')

# 创建图的标题
plt.title('Interesting Graph\nCheck it out')

# 生成默认图例
plt.legend()

# 展示
plt.show()