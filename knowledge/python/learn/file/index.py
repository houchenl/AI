

# open(file_name [, access_mode][, buffering])
# 打开文件，创建file对象，然后使用file对象进行文件操作
# 默认访问模式是只读r
fo = open('index.py', 'r')
print('file name is %s' % fo.name)     # file name is index.py
print('visit mode is %s' % fo.mode)    # visit mode is r
print('is closed: %s' % fo.closed)     # is closed: False


# file object
# file对象的属性包括
# file.closed       返回true如果文件已被关闭，否则返回false。
# file.mode         返回被打开文件的访问模式。
# file.name         返回文件的名称。
# file.softspace    如果用print输出后，必须跟一个空格符，则返回false。否则返回true。


# 关闭文件
# 关闭文件读写后，文件读写对象还存在，但是已关闭
fo.close()
print('file name is %s' % fo.name)     # file name is index.py
print('visit mode is %s' % fo.mode)    # visit mode is r
print('is closed: %s' % fo.closed)     # is closed: True


# write()
# 向打开的文件写入字符串，write()方法不会在字符串末尾添加换行符
# 语法：fileobject.write(string)
# 先以w模式打开文件，然后使用write()方法写入字符串，最后关闭文件对象
fo = open('test.txt', 'w')
fo.write('千里之行，始于足下。hello write()')
fo.close()


# read()
# 从一个打开的文件读取字符串
# 语法：fileobject.read([count])
# 参数是要读取的字符数。该方法从文件开头开始读入，如果没有传入count，会尽可能多地读取内容，可能直到文件末尾。
fo = open('test.txt', 'r+')
str = fo.read(10)
print('read result is %s' % str)    # read result is 千里之行，始于足下。
fo.close()


# tell()
# 返回文件内当前读写位置


# seek(offset[, from])
# 改变当前文件的读写位置。offset表示要移动的字符数；
# from变量指定移动字符的参考位置，0表示以文件开头为参考位置，1表示以当前位置为参考，2表示以文件末尾为参考

# 打开文件
fo = open('test.txt', 'r')
str = fo.read(10)
print('read result is %s' % str)

# 查找当前读写位置
position = fo.tell()
print('当前文件位置：', position)    # 当前文件位置： 30， 一个汉字字符占3个位置

# 把指针设置到文件开头
position = fo.seek(0, 0)
str = fo.read(10)
print('read result is %s' % str)

# 关闭打开的文件
fo.close()


# python内置的os模块提供有多项文件操作，如：重命名、删除文件，创建、删除、更改目录
import os


# rename(current_file_name, new_file_name)
# 重命名文件
os.rename('test.txt', 'test.log')


# remove(file_name)
# 删除文件
# os.remove('hello.log')    # error 删除不存在的文件会报错


# mkdir(dir_name)
# 在当前目录下创建新目录
# os.mkdir('test')    # error 创建已存在的目录会报错


# chdir(dir_name)
# 跳转到新的目录，类似于cd的功能
# os.chdir('/Users/houchen/remote')


# getcwd()
# 获取当前目录路径
# print(os.getcwd())    # /Users/houchen/remote


# rmdir(dir_name)
# 删除空目录
# os.rmdir('test')    # error 删除不存在的目录会报错



