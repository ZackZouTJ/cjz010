# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 07:20:00 2019

@author: ZJ
"""

from matplotlib.pylab import date2num
import tushare as ts
from datetime import datetime
import matplotlib.pyplot as plt
import mpl_finance as mpf
import pandas as pd


ts.set_token('3d86ce37200505496b7cef7a97ee5b1cc275b5d914e81fb6a3b5634b') #设置访问令牌
pro = ts.pro_api()

today=datetime.now().date().strftime('%Y%m%d')
t=datetime.now().date()
fig = plt.figure(figsize=(12,6),dpi=300)

num = date2num(t)

# 对tushare获取到的数据转换成candlestick_ohlc()方法可读取的格式
def plot_k_bar(df):
    alist = []
    for idx,row in df.iterrows():
        date,open,high,low,close= row[1:6]
        # 将日期转换为数字
        n= -idx+ num
        data = (n,open,high,low,close)
        alist.append(data)
    
        
    ax = fig.gca()
    ax.xaxis_date()
    plt.xticks(rotation=45) #日期显示的旋转角度
    plt.title(df["ts_code"][0])
    plt.xlabel("Date")
    plt.ylabel("K-Bar")
    mpf.candlestick_ohlc(ax,alist,width=0.7,colorup='red',colordown='green')
    fig.savefig("stockimg\\"+df["ts_code"][0]+".png", format = 'png')
    plt.clf()
 


##stocklists = pro.query('stock_basic', exchange='', list_status='L', fields='ts_code,name,list_date')

##for i in range(len(stocklists)):
    
df = ts.pro_bar(ts_code="601010.SH", asset='E', adj='qfq', start_date="20140829", end_date="20141219",freq ="5min" ) 
plot_k_bar(df)

