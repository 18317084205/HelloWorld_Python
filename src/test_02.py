#coding:utf-8
'''
Created on 2018年2月24日

@author: Liang
'''
a=2.3e5
b=1.25e-3
c=5
print a+5
print a+c
print a+b

inx= input("请输入数量：")
f1 = 0
f2 = 1

for i in range(inx):
    if i == 0:
        print 0
    elif i == 1:
        print 1
    else:
        fn = f1 + f2
        f1 = f2
        f2 = fn
        print fn