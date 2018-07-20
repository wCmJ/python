#   __call__
class Student(object):
    def __init__(self, name):
        self.name=name
    def __call__(self):
        print('anything')
s=Student('lyou')
s()

#   Callable and callable(): whether object can be invoked.
callable(int)
#True

#   __getattr__
#   when invoking attribute that does not exist, the interpreter in PYTHON will try to invoke __getattr__(self, 'attr') to get attribute.
class Student(object):
    def __init__(self):
        self.name='Michael'
    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda:25    #return function
s=Student()
s.score
s.age()     

#   __iter__    ：   always exist with __next__
#   class can bu used for loop(for...in)
class Fib(object):
    def __init__(self):
        self.a, self.b = 0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration()
        return self.a
for n in Fib():
    print(n)

#   __getitem__ :   get the specified element. Fib()[5]
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a+b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for n in range(stop):
                if n >= start:
                    L.append(a)
                a, b = b, a + b
            return L
f = Fib()
f[0:5]
f[:10]

#   enum
from enum import Enum
Month = Enum('M',('Jan','Feb','Mar','Apr'))
for name, member in Month.__members__items():
    print(name, member, member.value)

from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
day1 = Weekday.Mon
type(day1)  #   <enum 'Weekday'>    

class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, Gender):
        self.name = name
        self.gender = Gender

#   custom Metaclasses
class Foo():
    pass

f = Foo()
#   the expression Foo() creates a new instance of class Foo.
#   when the interpreter encounters Foo()
#   the __call__() method of Foo's parent class is called
#   the __call__() method in turn invokes the following
#   __new__()
#   __init__()
#   if Foo does not define __new__() and __init__(), default methods are inherited from Foo's ancestry
#   if Foo does define these methods, they override those from the ancestry, which allows for customized behavior when instantiating Foo

class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
class MyList(list, metaclass=ListMetaclass):
    pass
L=MyList()
L.add(1)
#   cls:    当前准备创建的类的对象
#   name:   类的名字
#   bases:  类继承的父类的集合
#   attrs:  类的方法集合

#   ORM:    object relational mapping   对象关系映射
class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')
u = User(id = 12345, name = 'Michael', email = 'test@orm.org', password='my-pwd')
u.save()
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')





