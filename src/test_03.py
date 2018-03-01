#coding:utf-8
'''
Created on 2018年2月24日

@author: Liang
'''

def circle():
    '''计算圆的面积'''
    r = int(raw_input("请输入圆形的半径:"))
    area = 3.1415 * r ** 2
    print circle.__doc__
    return area

def rectangle():
    '''计算矩形的面积'''
    l = int(raw_input("请输入长:"))
    w = int(raw_input("请输入宽:"))
    area = l * w
    return area

def triangle():
    '''计算三角形的面积'''
    b = int(raw_input("请输入底:"))
    h = int(raw_input("请输入高:"))
    area = h * b * 0.5
    return area

flag = True
print "计算图形的面积"
while flag:
    print "C(圆),R(矩形),T(三角形),Q(退出)"
    s= raw_input("请输入计算的图形:")
    if s == "C" or s == "c":
        areas = circle()
    elif s == "R" or s == "r":
        areas = rectangle()
    elif s == "T" or s == "t":
        areas = triangle()
    elif s == "Q" or s == "q":
        flag = False
    else:
        continue
        
    if flag:
        print "面积是：",areas
    else:
        print "退出程序"
    
