#coding:utf-8
'''
Created on 2018年2月28日

@author: Liang
'''
def hi():
    print "hello world"
name = "world"
age = 88

def main():
    print "自己运行的"
if __name__ == '__main__':
    main()
else:
    def select():
        print "C(圆),R(矩形),T(三角形),Q(退出)"
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