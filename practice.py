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