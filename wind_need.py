import pandas as pd
import numpy as np
data_x=pd.read_csv('wind_need_1.csv',usecols=[1],encoding='gbk')
'''
将csv文件读成数据表，用的是什么文件，第几行，编码是gbk（中文字符）；
按照道理UTF－8也可以，但是这里不知道为什么不可以
'''
train_data=np.array(data_x)
'''将数据表转化为数组'''
train_x_list=train_data.tolist()
'''数组转化为列表，这里列表里的每一个元素都是list'''
import cx_Oracle
conn=cx_Oracle.connect("wind_read_only", "wind_read_only", "192.168.0.223:1521/orcl")
'''建立Oracle连接，账户＋密码＋host地址＋port'''
#cursor=conn.cursor()
'''建立cursor光标，之后对光标进行操作，如cursor.execute;cursor.fetchall等等'''
result_container=[]
#建立一个list，储存迭代得到的数据表；数据表名称来自列表中的索引
for i in train_x_list:
    a=i[0]
    sql="select max(OPDATE) from wind."+a
    result_container.append(pd.read_sql(sql,conn))
#利用pandas每次运行sql，运行后加入到列表中；此时列表每一个元素为数据表
df=pd.DataFrame()
for i in result_container:
    df=pd.concat([df,i])
#将数据表结合起来
#cursor.execute(sql)
#r=cursor.fetchall()
#print (type(result_container[2]))
print (df)
