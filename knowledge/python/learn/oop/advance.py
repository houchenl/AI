

# __slots__
# 限制类的实例允许绑定的属性，相当于列一个白名单
# 限制只对本类的实例起作用，对子类的实例不起作用
# 想对子类的实例做此限制，需要在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上所有父类的__slots__
class Animal(object):
    __slots__ = ('name', 'age')   # 用tuple定义允许绑定的属性名称

class Dog(Animal):
    __slots__ = ('weight')

class BigDog(Dog):
    __slots__ = ('size')

animal = Animal()
animal.name = 'ss'
animal.age = 22

dog = Dog()
dog.weight = 43.2
dog.name = 'dog'
dog.age = 12

big_dog = BigDog()
big_dog.weight = 43.2
big_dog.name = 'big_dog'
big_dog.age = 12
big_dog.size = 3.5


# @property
# python内置@property装饰器，负责把一个getter方法变成属性调用
# 同时，@property会生成@attr.setter装饰器，负责把一个setter方法变成属性调用
# 此时，getter和setter方法名就是属性名
# 另外，如果只定义getter方法，就是只读属性，如年龄，可以通过id失算
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100')
        self._score = value

a = Student()
a.score = 33
print(a.score)


# python允许多重继承


# 定制类1
# __str__
# 直接打印实例对象会打印内存地址，如果要自定义打印实例时的输出的内容，就在类中自定义__str__()方法


