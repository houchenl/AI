a = 'hello '
b = 'world '

# method 1
c = a + b
print(c)

# method 2
d = 'hello %s' % b
print(d)

# 字符串与数字直接用+号连接时异常

开始时，我用
str = 'hello' + 5
拼接字符串，报异常错误
查询后，发现python不会对int值自动类型转换，需要手动类型转换，所以，代码应如下写法
str = 'hello' + str(5)
