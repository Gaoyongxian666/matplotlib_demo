# encoding: utf-8
'''
@author: gaoyongxian666
@file: demo09.py
@time: 2018/5/26 19:26
'''

# 从网络加载数据
import matplotlib.pyplot as plt
import numpy as np
import urllib
# 导入了matplotlib.dates作为mdates，它对于将日期戳转换为 matplotlib 可以理解的日期很有用。
import matplotlib.dates as mdates



# 时间戳的转换，此函数接受数据，基于编码来解码数据，然后返回它。
def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter


# stock_data，这是我们加载的数据
def graph_data(stock):
    stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10y/csv'
    # read读的是二进制数据要decode一下
    source_code = urllib.request.urlopen(stock_price_url).read().decode()

    stock_data = []

    # split_source变量拆分数据，以换行符拆分。
    split_source = source_code.split('\n')

    for line in split_source:
        split_line = line.split(',')
        # 但有一些头信息我们需要过滤掉。为此，我们使用一些基本的过滤，
        # 检查它们来确保每行有6个数据点，然后确保术语values不在行中。
        if len(split_line) == 6:
            if 'values' not in line:
                stock_data.append(line)

    date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data,
                                                          delimiter=',',
                                                          unpack=True,
                                                          # %Y = full year. 2015
                                                          # %y = partial year 15
                                                          # %m = number month
                                                          # %d = number day
                                                          # %H = hours
                                                          # %M = minutes
                                                          # %S = seconds
                                                          # 12-06-2014
                                                          # %m-%d-%Y
                                                          # 我们使用可选的converters参数来指定我们要转换的元素（0），
                                                          # 以及我们打算要怎么做。
                                                          converters={0: bytespdate2num('%Y%m%d')})

    plt.plot_date(date, closep, '-', label='Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.show()


graph_data('TSLA')


