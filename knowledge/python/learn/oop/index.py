
# 在python中，所有数据类型都可以视为对象


# 定义类1
# 使用class关键字定义类，class后跟类名Soldier，类名后跟()，()里面写入父类对象，如果没有特定的父类，使用object，Object是所有类的祖先，最后以:结尾
class Soldier(object):
    pass


# 定义构造函数
# 有时类固定需要某些属性，此时可以为类定义构造函数，在创建实例时执行构造函数，在构造函数中为创建的实例添加属性并绑定值
# 定义构造函数和定义普通函数类似，只是有3点不同：
# 1. 构造函数的函数名固定为__init__，init前后分别有两个下划线
# 2. 构造函数的第1个参数固定为self，表示创建的实例对象
# 3. 在构造函数中为实例添加属性并赋值时，使用self.xxx = yyy
class Car(object):

    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width

    # 定义类的函数和普通函数类似，只是第1个参数固定为self，且调用时不用传
    def print_car_info(self):
        print('method called: car %s length %.1f width %.1f' % (self.name, self.length, self.width))


# 定义私有变量
# 在变量名前加两个下划线，python会把变量名更改为_类名__变量名，外部就不能使用实例.__变量名访问了，类似于私有变量
# 但外部仍可以通过_类名__变量名访问，但强烈不建设这么做，因为不同python版本可能把变量名修改的不同，而且私有变量不应该访问，即使可以通过某种方式曲线访问
# 在变量名前加一个下划线，在外部仍可访问，但尽量不要访问。这种变量约定俗成为：虽然我可以被访问，但是，请把我视为私有变量，不要随意访问
# 在变量名前后分别有两个下划线的，是特殊变量，在外部可以访问。自己不要定义这种变量
class Student(object):
    country = 'cn'
    name = 'Student'

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score


# 类属性
# 上面Student类中定义的country变量为类属性，类的所有实例都可以访问
# 实例和类定义相同名称属性时，实例属性会覆盖类属性，使用del 可以删除实例属性
# 使用实例修改不了类的属性，因为使用实例修改属性时，如果实例不存在这个属性，会为实例创建这个属性
# 修改类属性值，需要使用类名引用变量
# 不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误
ll = Student('ll', 586)
# print('class attr %s, instance attr %s' % (Student.name, ll.name))   # class attr Student, instance attr Student
ll.name = 'll'
# print('class attr %s, instance attr %s' % (Student.name, ll.name))   # class attr Student, instance attr ll
del ll.name    # 删除实例属性
# print('class attr %s, instance attr %s' % (Student.name, ll.name))   # class attr Student, instance attr Student


# 继承和多态
# python是动态语言，在多态调用时，参数不需要必须是Animal类型或其子类型的实例，只是传入实例中有run方法就可以
# 比如：文件操作中需要传入file-like-object，不要求传入对象必须是file-object，只要求传入对象中有read方法就可以
class Animal(object):
    def run(self):
        print('Animal running')

class Dog(Animal):
    def run(self):
        print('Dog running')


# 创建实例1
# 在类名后加上()就可以创建实例
dart = Soldier()

# 创建实例2
# 如果类有带参数的构造函数，创建实例时，就需要传入对应参数，self不用传
bmw = Car('bmw', 5.5, 2.5)
# bmw.print_car_info()    # method called: car bmw length 5.5 width 2.5
# print('car %s length %.1f width %.1f' % (bmw.name, bmw.length, bmw.width))    # car bmw length 5.5 width 2.5


# 实例1
# 和静态语言不同，python的实例对象可以绑定属性，类似js
# 如果实例对象上本身已有name属性，那么这个操作就为name属性赋新值
dart.name = 'houchenl'


# 实例2
# 获取实例类型：type(instance)
# type()返回值是类，可以用==直接判断两个类是否相等
# print(type(123))        # <class 'int'>
# print(type('hello'))    # <class 'str'>
# print(type(bmw))        # <class '__main__.Car'>
# print(type('hello') == str)              # True
# print(type('hello') == type('world'))    # True


# 实例3
# 使用isinstance(obj, class)判断对象是否是类的实例
xiaohua = Dog()
# print(isinstance(xiaohua, Dog))       # True
# print(isinstance(xiaohua, Animal))    # True


# 实例4
# 获取实例的所有属性和方法
# print(dir(bmw))
'''
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
'__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', 
'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
'__weakref__', 'length', 'name', 'print_car_info', 'width']
'''
# 如上可见，对象中有很多特殊用途的属性和方法。__len__()方法返回对象的长度，如果调用len()函数获取一个对象的长度，实际上，在len函数内部，
# 它自动去调用对象的__len__()方法。自己写的类，如果想使用len(my_obj)函数的话，就自己写一个__len__()方法


# 实例5
# 操作属性
# setattr(obj, attr, value)，为对象属性设置值，如果没有这个属性，先添加属性
# getattr(obj, attr)，获取对象指定属性的值，如果没有该属性，会报错
# getattr(obj, attr, default)，可以指定找不到属性时的默认值，这样找不到属性返回默认值，不会报错
# hasattr(obj, attr)和getattr(obj, attr)也可以用来操作对象的方法
# 注意！！可以直接使用obj.attr时，就不要使用xxxattr()，麻烦！
class MyPower(object):
    def __init__(self, num):
        self.x = num

    def power(self):
        return self.x * self.x

my_power = MyPower(5)

# print(dir(my_power))             # ['__getattribute__', '__setattr__', ... , 'power', 'x']
# print(hasattr(my_power, 'x'))    # True
# print(hasattr(my_power, 'y'))    # False
# setattr(my_power, 'y', 9)
# print(hasattr(my_power, 'y'))    # True
# print(getattr(my_power, 'y'))    # 9
# print(getattr(my_power, 'z'))       # ttributeError: 'MyPower' object has no attribute 'z'
# print(getattr(my_power, 'z', 404))  # 404


