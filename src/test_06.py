#coding:utf-8
'''
Created on 2018年2月28日

@author: Liang
'''
import sys as s
import test_07 as t
for i in s.argv:
    print i

t.hi()
print t.name
print t.age

print "计算图形的面积"
while True:
    t.select()
    s= raw_input("请输入计算的图形:")
    if s == "C" or s == "c":
        areas = t.circle()
    elif s == "R" or s == "r":
        areas = t.rectangle()
    elif s == "T" or s == "t":
        areas = t.triangle()
    elif s == "Q" or s == "q":
        print "退出程序"
        break
    else:
        continue
    print "面积是：",areas   
        
    
