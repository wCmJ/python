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














