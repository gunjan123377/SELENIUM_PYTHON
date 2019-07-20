#EVEN NUMBER
# for i in range(3,101):
#     for j in range(2,i):
#         flag=0
#         if i%j==0:
#             flag=1
#             break
#     if flag==0:
#         print(i)

# for i in range(3,101):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)

# [1, 0, 3, 2, 5, 4, 7, 6, 9, 8]
# a=list(range(10))
# i=0
# while i<len(a):
#     tmp=a[i]
#     a[i]=a[i+1]
#     a[i+1]=tmp
#     i=i+2
#PANDAS==========================================================
# from pandas import Series
# s = Series(list("abcd"))
# print(s)
# ===============
# 0    a
# 1    b
# 2    c
# 3    d
# dtype: object

# import pandas as pd
# series = pd.Series(list("abcd"),index=["p","q","r","s"])
# print(series)
# print (series["p"])
# print (series[0])#still mantaining original index
# ====================
# p    a
# q    b
# r    c
# s    d
# dtype: object
# a
# a

# import pandas as pd
# series = pd.Series(range(5),index=list("xyzxy"))
# print(series)
# print (series["x"])#It is not recommended, bcz we have two x
# print (series[0])
# x    0
# y    1
# z    2
# x    3
# y    4
# dtype: int64
# x    0
# x    3
# dtype: int64
# 0

# import pandas,numpy
# data = {'a':10, 'b':20, 'c':30}
#
# series = pandas.Series(data)
# print(series)
# a    10
# b    20
# c    30
# dtype: int64

# import requests
# import json
# r=requests.get("https://api.tumblr.com/v2/blog/good.tumblr.com/info?api_key=fuiKNFp9vQFvjLNvx4sUwti4Yb5yGutBN4Xh10LXZhhRKjWlV4").json()
# import pandas as pd
# print(r)
# print(pd.Series(r))
# print(pd.Series(r["response"]["blog"]))
# meta                             {'status': 200, 'msg': 'OK'}
# response    {'blog': {'ask': True, 'ask_anon': False, 'ask...
# dtype: object
# ask                                   True
# ask_anon                             False
# ask_page_title         Ask GOOD a question
# can_chat                             False
# can_subscribe                        False
# description            Live Well. Do Good.
# is_nsfw                              False
# is_optout_ads                        False
# likes                                  430
# name                                  good
# posts                                 2520
# share_likes                           True
# subscribed                           False
# title
# total_posts                           2520
# updated                         1490031650
# url               https://good.tumblr.com/
# uuid              t:Q1kRotmAoWXle1yTJ1UceA
# dtype: object

# import pandas,numpy
# data = {'a':10, 'b':20, 'c':30}
# series = pandas.Series(data,index=list("abcd"))
# print(series)
# a    10.0
# b    20.0
# c    30.0
# d     NaN
# dtype: float64#Datatype has changed due to NaN==>because it is float and series is homogenous.

# import pandas,numpy
# data = {'a':10, 'b':20, 'c':30}
# series = pandas.Series(data,index=range(4))
# print(series)
# 0   NaN
# 1   NaN
# 2   NaN
# 3   NaN
# dtype: float64

# import pandas,numpy
# data = {'a':10, 'b':20, 'c':30}
# series = pandas.Series(data,index=list("abcd"))
# print(series)
# print(series * 6)
# series["d"]=4
# print(series * 6)
# a    10.0
# b    20.0
# c    30.0
# d     NaN
# dtype: float64
# a     60.0
# b    120.0
# c    180.0
# d      NaN
# dtype: float64
# a     60.0
# b    120.0
# c    180.0
# d     24.0
# dtype: float64

# import pandas as pd
# s = pd.Series([10, 20, 30, 40, 50])
# print(s[1:4])
# 1    20
# 2    30
# 3    40
# dtype: int64

# import pandas, numpy
# arr = numpy.array([10, 20, 30, 40, 50])
# series = pandas.Series(arr)
# print(series)
# 0    10
# 1    20
# 2    30
# 3    40
# 4    50
# dtype: int32

###DATAFRAME=============================================
# import pandas as pd
# df1=pd.DataFrame(list("abcde"))
# print (df1)
#    0
# 0  a
# 1  b
# 2  c
# 3  d
# 4  e

# import pandas
# data = [{'a':1, 'b':2}, {'a':2, 'b':4, 'c':8}]#keys of dictionary act as columns of a dataframe.
# table = pandas.DataFrame(data, index=['first', 'second'])
# print(table)
# print (table["a"])
# print (table["a"]["first"])
# print (table["a"][0])
# #print (table[0]["a"])This is wrong, first columns will come than index(row).
#         a  b    c
# first   1  2  NaN
# second  2  4  8.0
# first     1
# second    2
# Name: a, dtype: int64
# 1
# 1

# import pandas
# data = {'one': pandas.Series([1, 2, 3]),
#         'two': pandas.Series([1, 2, 3, 4], index=list("abcd"))}
# table = pandas.DataFrame(data)
# print (table)
#    one  two
# 0  1.0  NaN
# 1  2.0  NaN
# 2  3.0  NaN
# a  NaN  1.0
# b  NaN  2.0
# c  NaN  3.0
# d  NaN  4.0

# import pandas
# data = {'one': pandas.Series([1, 2, 3]),
#         'two': pandas.Series([1, 2, 3, 4])}
# table = pandas.DataFrame(data)
# print (table)
# table["three"]=table["one"]+table["two"]
# print (table)
#    one  two
# 0  1.0    1
# 1  2.0    2
# 2  3.0    3
# 3  NaN    4
#    one  two  three
# 0  1.0    1    2.0
# 1  2.0    2    4.0
# 2  3.0    3    6.0
# 3  NaN    4    NaN

# import pandas
# data = {'one': pandas.Series([1, 2, 3], index=['a', 'b', 'c']),
#         'two': pandas.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
# table = pandas.DataFrame(data)
# table['three'] = pandas.Series([10, 20, 30], index=['a', 'b', 'c'])
# print (table)
# del(table['one'])
# print(table)
# table.pop("two")
# print(table)
#
#    one  two  three
# a  1.0    1   10.0
# b  2.0    2   20.0
# c  3.0    3   30.0
# d  NaN    4    NaN
#    two  three
# a    1   10.0
# b    2   20.0
# c    3   30.0
# d    4    NaN
#    three
# a   10.0
# b   20.0
# c   30.0
# d    NaN


# import pandas
# data = {'one': pandas.Series([1, 2, 3], index=['a', 'b', 'c']),
#         'two': pandas.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
# table = pandas.DataFrame(data)
# table['three'] = pandas.Series([10, 20, 30], index=['a', 'b', 'c'])
# print(table)
# print(table.loc["d"])
# print(table.iloc[2])
#
#    one  two  three
# a  1.0    1   10.0
# b  2.0    2   20.0
# c  3.0    3   30.0
# d  NaN    4    NaN
# one      NaN
# two      4.0
# three    NaN
# Name: d, dtype: float64
# one       3.0
# two       3.0
# three    30.0
# Name: c, dtype: float64

# import pandas
# data = {'one': pandas.Series([1, 2, 3], index=['a', 'b', 'c']),
#         'two': pandas.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
# table = pandas.DataFrame(data)
# row  = pandas.DataFrame([[11,13],[17,19]],columns=['two','three'])
# print (row)
# table = table.append(row)
# print (table)
# table = table.drop('a')
# print(table)
#
#    two  three
# 0   11     13
# 1   17     19
#    one  three  two
# a  1.0    NaN    1
# b  2.0    NaN    2
# c  3.0    NaN    3
# d  NaN    NaN    4
# 0  NaN   13.0   11
# 1  NaN   19.0   17
#    one  three  two
# b  2.0    NaN    2
# c  3.0    NaN    3
# d  NaN    NaN    4
# 0  NaN   13.0   11
# 1  NaN   19.0   17

# import pandas
# data = [{'a':1, 'b':2}, {'a':2, 'b':4, 'c':8}]
# table = pandas.DataFrame(data, index=['first', 'second'])
# print(table)
# row=pandas.DataFrame([[1,2,3]],columns=['a','b','c'],index=['three'])
# table.append(row)
# print (table)
#         a  b    c
# first   1  2  NaN
# second  2  4  8.0
#         a  b    c
# first   1  2  NaN
# second  2  4  8.0

# import pandas
# a=pandas.read_csv("bank-data.csv")
# #print (a)
# #a.to_csv("bank-dataNew.csv")
# print("===============================")
# print (len(a))
# print("===============================")
# print (a[0:5])
# print("===============================")
# print (a.tail())
# print("===============================")
# print (a.head(10))
# print("===============================")
# print (a["job"][0:5])
# print("===============================")
# print (a["age"][0:5])
#
# ===============================
# 447
# ===============================
#    age          job  marital    y     hur
# 0   20      student   single  yes  2010.0
# 1   32   management   single  yes  2011.0
# 2   49   technician  married  yes  2012.0
# 3   32  blue-collar  married  yes  2013.0
# 4   33   management  married  yes  2014.0
# ===============================
#      age            job  marital    y  hur
# 442   26     technician   single  yes  NaN
# 443   60  self-employed  married  yes  NaN
# 444   42    blue-collar   single  yes  NaN
# 445   32         admin.   single  yes  NaN
# 446   46    blue-collar  married  yes  NaN
# ===============================
#    age          job   marital    y     hur
# 0   20      student    single  yes  2010.0
# 1   32   management    single  yes  2011.0
# 2   49   technician   married  yes  2012.0
# 3   32  blue-collar   married  yes  2013.0
# 4   33   management   married  yes  2014.0
# 5   61       admin.   married  yes  2015.0
# 6   45  blue-collar  divorced  yes  2016.0
# 7   34   technician   married  yes  2017.0
# 8   37   management   married  yes  2018.0
# 9   27       admin.  divorced  yes  2019.0
# ===============================
# 0        student
# 1     management
# 2     technician
# 3    blue-collar
# 4     management
# Name: job, dtype: object
# ===============================
# 0    20
# 1    32
# 2    49
# 3    32
# 4    33
# Name: age, dtype: int64


# import pandas
# fo=pandas.read_csv("bank-data.csv")
# print("==============")
# print (fo["job"][5])
# a=fo.values
# b=fo.columns
# print("==============")
# print (a[:5])
# print("==============")
# print (b)
#
# ==============
# admin.
# ==============
# [[20 'student' 'single' 'yes' 2010.0]
#  [32 'management' 'single' 'yes' 2011.0]
#  [49 'technician' 'married' 'yes' 2012.0]
#  [32 'blue-collar' 'married' 'yes' 2013.0]
#  [33 'management' 'married' 'yes' 2014.0]]
# ==============
# Index(['age', 'job', 'marital', 'y', 'hur'], dtype='object')

# import pandas
# a=pandas.read_csv("bank-data.csv")
# print("=========================================")
# print (a.describe())
# print("=========================================")
# print ("SUM==*********\n",a.sum())
# print ("MEAN==*********\n",a.mean())
# print ("STD DEVIATIONS==*********\n",a.std())
# print ("VARIANCE==*********\n",a.var())
# print ("AGE mean is============",a["age"].mean())
# print ("AGE mean is============",a.age.mean())
# print("=============Unique age is============================")
# print (a.age.unique())
# =========================================
#               age         hur
# count  447.000000    10.00000
# mean    39.413870  2014.50000
# std     10.038539     3.02765
# min     19.000000  2010.00000
# 25%     32.000000  2012.25000
# 50%     37.000000  2014.50000
# 75%     47.000000  2016.75000
# max     80.000000  2019.00000
# =========================================
# SUM==*********
#  age                                                    17618
# job        studentmanagementtechnicianblue-collarmanageme...
# marital    singlesinglemarriedmarriedmarriedmarrieddivorc...
# y          yesyesyesyesyesyesyesyesyesyesyesyesyesyesyesy...
# hur                                                    20145
# dtype: object
# MEAN==*********
#  age      39.41387
# hur    2014.50000
# dtype: float64
# STD DEVIATIONS==*********
#  age    10.038539
# hur     3.027650
# dtype: float64
# VARIANCE==*********
#  age    100.772274
# hur      9.166667
# dtype: float64
# AGE mean is============ 39.41387024608501
# AGE mean is============ 39.41387024608501
# =============Unique age is============================
# [20 32 49 33 61 45 34 37 27 52 21 25 55 28 35 29 42 24 50 38 30 48 60 54
#  53 46 44 19 36 47 43 41 58 39 31 26 40 59 63 56 57 51 22 62 23 80]

# import pandas
# a=pandas.read_csv("bank-data.csv")
# print (a.columns)
# a["new col"]=a["age"]
# print (a["new col"].head(4))
# print (a.columns)
# a.columns=map(lambda x:x.replace(" ",""),a.columns)
# print (a.columns)
#
# Index(['age', 'job', 'marital', 'y', 'hur'], dtype='object')
# 0    20
# 1    32
# 2    49
# 3    32
# Name: new col, dtype: int64
# Index(['age', 'job', 'marital', 'y', 'hur', 'new col'], dtype='object')
# Index(['age', 'job', 'marital', 'y', 'hur', 'newcol'], dtype='object')

# import pandas
# a=pandas.read_csv("bank-data.csv")
# for k,v in a.head(3).iteritems():
#     print("====================")
#     print (k,v)====================
# age 0    20
# 1    32
# 2    49
# Name: age, dtype: int64
# ====================
# job 0       student
# 1    management
# 2    technician
# Name: job, dtype: object
# ====================
# marital 0     single
# 1     single
# 2    married
# Name: marital, dtype: object
# ====================
# y 0    yes
# 1    yes
# 2    yes
# Name: y, dtype: object
# ====================
# hur 0    2010.0
# 1    2011.0
# 2    2012.0
# Name: hur, dtype: float64

# import pandas
# a=pandas.read_csv("bank-data.csv")
# b=a.job.unique()[:5]
# print (b)
# b_dict=dict(zip(b,range(len(b))))
# b_dict1=dict(enumerate(b))
# print (b_dict)
# print (b_dict1)
#
# ['student' 'management' 'technician' 'blue-collar' 'admin.']
# {'student': 0, 'management': 1, 'technician': 2, 'blue-collar': 3, 'admin.': 4}
# {0: 'student', 1: 'management', 2: 'technician', 3: 'blue-collar', 4: 'admin.'}

# from pylab import *
# import pandas
# a=pandas.read_csv("bank-data.csv")
# b=a[a.job=="student"]
# print (b.head(5))
# c=a.job.value_counts()
# print("====================================")
# print (c)
# print("====================================")
# print ("max people in one profession is",c[0])
# #print (a.job.isnull())
# c[:5].plot(kind="bar")
# show()
#     age      job marital    y     hur
# 0    20  student  single  yes  2010.0
# 13   21  student  single  yes     NaN
# 14   25  student  single  yes     NaN
# 53   19  student  single  yes     NaN
# 89   27  student  single  yes     NaN
# ====================================
# management       131
# technician        83
# blue-collar       69
# admin.            58
# services          38
# self-employed     20
# student           19
# entrepreneur      15
# housemaid         14
# Name: job, dtype: int64
# ====================================
# max people in one profession is 131

import pandas
data={'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'],
'age': [42, 52, 36, 24, 73],
'preTestScore': [4, 24, 31, ".", "."],
'postTestScore': ["25,000", "94,000", 57, 62, 70]}
table = pandas.DataFrame(data)
table.to_csv("example.csv")
fo=pandas.read_csv("example.csv")
#print (fo)#5.3
print (fo.values)#5.4
d=fo.loc[:,['first_name','last_name']]
print (d)#5.5
print (fo.loc[3:4])#5.7
table.postTestScore=map(lambda x : x.replace(",",""),list(table.postTestScore))
print (table.postTestScore)#5.8
