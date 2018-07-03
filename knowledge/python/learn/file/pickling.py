
# 序列化
# 把变量从内存中变成可存储或传输的过程称为序列化，在python中叫pickling
# 反过来，把变量内容从序列化的对象重新读到内存里叫做反序列化

# python提供了两个模块实现序列化，cPickle和pickle。
# 这两个模块功能是一样的，区别在于cPickle是C语言写的，速度快，pickle是纯Python写的，速度慢
# 用的时候，先尝试导入cPickle，如果失败，再导入pickle
try:
    import cPickle as pickle
except ImportError:
    import pickle

d = dict(name='Bob', age=23, score=88.5)    # {'name': 'Bob', 'age': 23, 'score': 88.5}

# pickle.dumps方法把任意对象序列化成一个str(二进制字符串)，然后可以把str写入文件
# 或者使用pickle.dump方法直接把对象序列化后写入一个文件对象
# b'\x80\x03}q\x00(X\x04\x00\x00\x00nameq\x01X\x03\x00\x00\x00Bobq\x02X\x03\x00\x00\x00ageq\x03K\x17X\x05\x00\x00\x00scoreq\x04G@V \x00\x00\x00\x00\x00u.'
result = pickle.dumps(d)

fo = open('dump.txt', 'wb')
pickle.dump(d, fo)
fo.close()
# 8003 7d71 0028 5804 0000 006e 616d 6571
# 0158 0300 0000 426f 6271 0258 0300 0000
# 6167 6571 034b 1758 0500 0000 7363 6f72
# 6571 0447 4056 2000 0000 0000 752e 

# 反序列化时，可以先从文件中读取出str，然后使用pickle.loads()方法反序列化出对象
# 也可以直接使用pickle.load()方法从文件对象中加载出对象
# 序列化时的对象和反序列化得到的对象是两个不同的对象，只是内容相同
fo = open('dump.txt', 'rb')
d = pickle.load(fo)    # {'name': 'Bob', 'age': 23, 'score': 88.5}
fo.close()


# pickle只能用在python语言内部。想与其它语言交互时，需要序列化成通用格式，如json
# python内置了json模块用于将python对象转换成json
# json.dumps()方法返回str，内容是标准的json
import json

result = json.dumps(d)    # {"name": "Bob", "age": 23, "score": 88.5}

# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
json.loads(json_str)
