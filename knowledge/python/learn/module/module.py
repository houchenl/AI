
# 为避免函数名重复，复用其它python文件中方法，python提供了模块
# 每个python文件都是一个模块，文件名就是模块名。如文件名为xxx.py，那么模块名就是xxx


# 导入模块，有两种办法：


# 1. 直接导入方法。不推荐！因为如果同时导入多个模块的同名方法，会无法区分
# from module import function
from module1 import foo
foo()

from module2 import foo
foo()


# 2. 导入模块，使用模块调用方法。模块在导入时可以起别名。推荐！可以避免同名冲突问题
# import module [as alias]
import module1 as m1
import module2 as m2
m1.foo()
m2.foo()


# 如果我们导入的模块除了定义函数之外还有可以执行代码，那么Python解释器在导入这个模块时就会执行这些代码
# 事实上我们可能并不希望如此，因此如果我们在模块中编写了执行代码，最好是将这些执行代码放入如下所示的条件中
# 这样的话除非直接运行该模块，if条件下的这些代码是不会执行的，因为只有直接执行的模块的名字才是“\_\_main\_\_”
# if __name__ == '__main__':
#     pass

import module3
# module3中上面if条件中的代码不会执行，因为不是直接执行，而是Import的。但是普通的print语句仍会执行


"""
Python常用模块
    - 运行时服务相关模块: copy / pickle / sys / ...
    - 数学相关模块: decimal / math / random / ...
    - 字符串处理模块: codecs / re / ...
    - 文件处理相关模块: shutil / gzip / ...
    - 操作系统服务相关模块: datetime / os / time / logging / io / ...
    - 进程和线程相关模块: multiprocessing / threading / queue
    - 网络应用相关模块: ftplib / http / smtplib / urllib / ...
    - Web编程相关模块: cgi / webbrowser
    - 数据处理和编码模块: base64 / csv / html.parser / json / xml / ...
"""

