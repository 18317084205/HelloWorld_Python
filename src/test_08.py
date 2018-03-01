#coding:utf-8
'''
Created on 2018年2月28日

@author: Liang
'''
lists=["liang","jian","bo"]
print "lists 的 长度为:", len(lists)

lists.append("object")
print "新的lists为",lists

for item in lists:
    print "item ：",item

lists.sort()
print "排序后的lists为",lists

del lists[2]
print "del后的lists为",lists

num = 20
a = "apple"
name = "liang"
print "%s have %d %s" %(name,num,a)

print name[2:]
if "a" in name:
    print "yes"
if name.startswith("li"):
    print "yes"
if name.find("an") != -1:
    print "yes"
delimiter = "^@_@^"
country = ["中国","韩国","英国"]
print delimiter.join(country)
