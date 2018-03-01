#coding:utf-8
'''
Created on 2018年2月24日

@author: Liang
'''
password = "liang123456"

while True:
    p = raw_input("请输入密码：")
    if p == password:
        print "密码正确",password
        break
    elif len(p)<6:
        print "密码长度错误"
    else:
        print "密码错误"
