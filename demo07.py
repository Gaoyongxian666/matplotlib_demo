# encoding: utf-8
'''
@author: gaoyongxian666
@file: demo07.py
@time: 2018/5/26 16:38
'''

# 饼图
# 饼图很像堆叠图，只是它们位于某个时间点。
# 通常，饼图用于显示部分对于整体的情况，通常以％为单位。
# 幸运的是，Matplotlib 会处理切片大小以及一切事情，我们只需要提供数值。


import matplotlib.pyplot as plt

slices = [7,2,2,13]
activities = ['sleeping','eating','working','playing']
cols = ['c','m','r','b']

patches,l_text,p_text=plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow= True,
        explode=(0,0.1,0,0),
        autopct='%1.1f%%')
# 在plt.pie中，我们需要指定『切片』，这是每个部分的相对大小。 然后，我们指定相应切片的颜色列表。
# 接下来，我们可以选择指定图形的『起始角度』。
# 这使你可以在任何地方开始绘图。
# 在我们的例子中，我们为饼图选择了 90 度角，这意味着第一个部分是一个竖直线条。
# 接下来，我们可以选择给绘图添加一个字符大小的阴影，然后我们甚至可以使用explode拉出一个切片。

# 我们总共有四个切片，所以对于explode，如果我们不想拉出任何切片，
# 我们传入0,0,0,0。 如果我们想要拉出第一个切片，我们传入0.1,0,0,0。
#将某部分爆炸出来， 使用括号，将第一块分割出来，数值的大小是分割出来的与其他两块的间隙

# 最后，我们使用autopct，选择将百分比放置到图表上面。圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数。

#labeldistance，文本的位置离远点有多远，1.1指1.1倍半径的位置

#shadow，饼是否有阴影

#patches, l_texts, p_texts，为了得到饼图的返回值，p_texts饼图内部文本的，l_texts饼图外label的文本



#改变文本的大小
#方法是把每一个text遍历。调用set_size方法设置它的属性
for t in l_text:
    t.set_size=(30)
for t in p_text:
    t.set_size=(20)


# 设置x，y轴刻度一致，这样饼图才能是圆的
plt.axis('equal')

plt.title('Interesting Graph\nCheck it out')
plt.show()

