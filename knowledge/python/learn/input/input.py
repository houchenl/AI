#-*- coding:utf-8 -*-

x = input("x: ")
y = input("y: ")
z = x + y
print(z)
a = x + y
print(a)

# python2中输入字符串用raw_input
name = raw_input("请输入姓名")
print('name is %s' % name)

# python2中input是把输入的内容当做代码执行
# python3中input是把输入内容当做字符串，与python2中raw_input相同
