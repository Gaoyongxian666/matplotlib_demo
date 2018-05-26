# encoding: utf-8
'''
@author: gaoyongxian666
@file: demo10.py
@time: 2018/5/26 19:40
'''

# 子图操作
# 自定义操控图表

import matplotlib.pyplot as plt


def graph_data(stock):
    # 为了修改图表，我们需要引用它，所以我们将它存储到变量fig。
    fig = plt.figure()
    # 将ax1定义为图表上的子图。 我们在这里使用subplot2grid，这是获取子图的两种主要方法之一。
    # 我们将深入讨论这些东西，但现在，你应该看到我们有2个元组，它们提供了(1, 1)和(0, 0)。
    # 1, 1表明这是一个1×1网格。 然后0, 0表明这个子图的『起点』将为0, 0。
    ax1 = plt.subplot2grid((1,1), (0,0))


    # 现在，由于我们正在绘制日期，我们可能会发现，如果我们放大，日期会在水平方向上移动。但是，我们可以自定义这些刻度标签，像这样：
    ax1.plot_date(date, closep, '-', label='Price')

    # 这将使标签转动到对角线方向。 接下来，我们可以添加一个网格：
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)

    ax1.grid(True)
    # 然后，其它东西我们保留默认，但我们也可能需要略微调整绘图，因为日期跑到了图表外面。 记不记得我们在第一篇教程中讨论的configure
    # subplots按钮？ 我们不仅可以以这种方式配置图表，我们还可以在代码中配置它们，以下是我们设置这些参数的方式：

    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)

