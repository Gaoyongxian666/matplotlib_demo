# encoding: utf-8
'''
@author: gaoyongxian666
@file: demo08.py
@time: 2018/5/26 16:58
'''

# 从文件加载数据
# 很多时候，我们想要绘制文件中的数据。 有许多类型的文件，以及许多方法，
# 你可以使用它们从文件中提取数据来图形化。
# 在这里，我们将展示几种方法。
# 首先，我们将使用内置的csv模块加载CSV文件，然后我们将展示如何使用 NumPy（第三方模块）加载文件。



import matplotlib.pyplot as plt
import csv
# csv文件格式是一种通用的电子表格和数据库导入导出格式。
# 是一个存储数据的文件，里面以逗号作为分割进行存储（当然也可以用制表符进行分割）。
# csv的规则
#
# 1 开头是不留空，以行为单位。
#
# 2 可含或不含列名，含列名则居文件第一行。
#
# 3 一行数据不跨行，无空行。
#
# 4 以半角逗号（即,）作分隔符，列为空也要表达其存在。
#
# 5列内容如存在半角引号（即"），替换成半角双引号（""）转义，即用半角引号（即""）将该字段值包含起来。
#
# 6文件读写时引号，逗号操作规则互逆。
#
# 7内码格式不限，可为 ASCII、Unicode 或者其他。
#
# 8不支持特殊字符
import numpy as np

x = []
y = []

with open('gyx.csv','r') as csvfile:
    # 默认的情况下, 读和写使用逗号做分隔符(delimiter)，用双引号作为引用符(quotechar)，
    # 当遇到特殊情况是，可以根据需要手动指定字符, 例如:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(row[0])
        y.append(row[1])

# 使用numpy读取数据
# np.loadtxt()用于从文本加载数据。
# 文本文件中的每一行必须含有相同的数据。
# 作用是把文本文件（*.txt）读入并以矩阵或向量的形式输出。

# loadtxt(fname, dtype=<class 'float'>, comments='#', delimiter=None, converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0)
# fname要读取的文件、文件名、或生成器。
# dtype数据类型，默认float。
# comments注释。
# delimiter分隔符，默认是空格。
# skiprows跳过前几行读取，默认是0，必须是int整型。
# usecols：要读取哪些列，0是第一列。例如，usecols = （1,4,5）将提取第2，第5和第6列。默认读取所有列。
# unpack如果为True，将分列读取。默认为flase它将会以整个数组返回。

# 在默认情况下是通过空格来分割列的，如果想通过其他来分割列则需要通过delimiter来设置。
# 如果你想跳过几列来读取则需要用usecoles来设置。
# 正常情况下该返回的是二维矩阵，若设置了unpack=True将返回各列

x, y = np.loadtxt('example.txt', delimiter=',', unpack=True)


plt.plot(x,y, label='Loaded from file!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()


import csv
with open('passwd', 'rb') as f:
    reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
    for row in reader:
        print(row)
# 上述示例指定冒号作为分隔符，
# 并且指定quote方式为不引用。这意味着读的时候都认为内容是不被默认引用符(")包围的。
# quoting的可选项为: QUOTE_ALL, QUOTE_MINIMAL, QUOTE_NONNUMERIC, QUOTE_NONE.
# 有点需要注意的是:当用writer写数据时， None 会被写成空字符串，浮点类型会被调用 repr() 方法转化成字符串。
# 所以非字符串类型的数据会被 str() 成字符串存储。
# 所以当涉及到unicode字符串时，可以自己手动编码后存储或者使用csv提供的 UnicodeWriter。

