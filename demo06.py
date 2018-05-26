# encoding: utf-8
'''
@author: gaoyongxian666
@file: demo06.py
@time: 2018/5/26 16:32
'''


# 堆叠图。 堆叠图用于显示『部分对整体』随时间的关系。 堆叠图基本上类似于饼图，只是随时间而变化。
#
# 让我们考虑一个情况，我们一天有 24 小时，我们想看看我们如何花费时间。 我们将我们的活动分为：睡觉，吃饭，工作和玩耍。
#
# 我们假设我们要在 5 天的时间内跟踪它，因此我们的初始数据将如下所示：
import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sleeping = [7,8,6,11,7]
eating =   [2,3,4,3,2]
working =  [7,8,7,2,2]
playing =  [8,5,7,8,13]

# 因此，我们的x轴将包括day变量，即 1, 2, 3, 4 和 5。
# 然后，日期的各个成分保存在它们各自的活动中。
plt.stackplot(days, sleeping,eating,working,playing, colors=['m','c','r','k'])

# 至少在颜色上看到，我们如何花费我们的时间。 问题是，如果不回头看代码，我们不知道什么颜色是什么。
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.show()


# 优化
days = [1,2,3,4,5]

sleeping = [7,8,6,11,7]
eating =   [2,3,4,3,2]
working =  [7,8,7,2,2]
playing =  [8,5,7,8,13]


plt.plot([],[],color='m', label='Sleeping', linewidth=5)
plt.plot([],[],color='c', label='Eating', linewidth=5)
plt.plot([],[],color='r', label='Working', linewidth=5)
plt.plot([],[],color='k', label='Playing', linewidth=5)
# plot的.plot方法绘制直线，根据一些坐标。

plt.stackplot(days, sleeping,eating,working,playing, colors=['m','c','r','k'])
# 我们在这里做的是画一些空行，给予它们符合我们的堆叠图的相同颜色，和正确标签。
# 我们还使它们线宽为 5，使线条在图例中显得较宽。
# 现在，我们可以很容易地看到，我们如何花费我们的时间。
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
