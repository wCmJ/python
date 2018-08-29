print():  , will be explained as space
          r'\' is wrong. 
          r'\\' will output \\
          '''...''' ... is \n (run as command line, and ... is not one part of code, is prompt)
print('''line1
line2
line3''')
print(r'''line1
line2
line3''')    
    
bool: True, False
and, or, not

None: None is not 0.
        
because variable can be assigned any value. so python is dynamic language.    

/: get float.
10/3  -->   3.3333333333333335
9/3   -->   3.0
9.0/3 -->   3.0
9/3.0 -->   3.0

//:
10//3     -->   3
10.0//3   -->   3.0
10//3.0   -->   3.0
10.0//3.0 -->   3.0
  
%:
10%3      -->   1
10.0%3    -->   1.0
10%3.0    -->   1.0
10.0%3.0  -->   1.0

GB2312 contains chinese.

ASCII: 0000 0000 - 0111 1111 one byte
Unicode:  at least two bytes
UTF-8:  one byte to six bytes, contains ASCII.
server Unicode transfers to UTF-8, then sends to browser.
python uses Unicode.

ord('A')  -->   65
ord('中')  -->   20013(0x4e2d)
chr(20013)  -->   '中'
chr(65)     -->   'A'
'\u4e2d'    -->   '中'

b means byte.
'ABC'.encode('ascii')   -->   b'ABC'
'ABC'.encode('utf-8')   -->   b'ABC'
'中午'.encode('utf-8')  -->   b'\xe4\xb8\xad\xe5\x8d\x88'
在bytes中，无法显示为ASCII字符的字节，用\x##显示.
b'ABC'.decode('utf-8')  -->   'ABC'
b'\xe4\xb8\xad\xe5\x8d\x88'.decode('utf-8')   -->   '中午'
b'\xe4\xb8\xad'.decode('utf-8')   -->   '中'
b'\xe4\xb8\xad\xff'.decode('utf-8')   -->   error
b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')    -->   '中'

#!/usr/bin/env  python3
# -*- coding:utf-8 -*-

'hello, %s' % 'world'
%s ---  string
%d ---  digit
%f ---  float
%x ---  hex
'growth rate: %d %%' % 7  -->  'growth rate: 7 %'

'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
'Hello, {0}, 成绩提升了 {1:1.1f}%'.format('小明', 17.125)


dict:
d={'a':1,'b':2}
1.'key' in d
2.d.get('key')
3.d.get('key',-1)

d.pop('key')

Hash: get location by key in dictionary.
          
key type: string, int.


#write file
dbfile = open('location and filename','w')
print('')



GIL: global interpreter lock
every thread must get GIL before executing codes.
and interpreter will release GIL when 100 bytecode have been executed.
so threads run one by one in python.
multiple threads's concurrent is just a dream in python.

async IO: operator system provides async IO, we can use single process single thread model to execute multi task.
this new model also is called event drive model.

multiprocessing supports multi processes, managers submodule support distribute multi processes to multi machines.
service process --> network conmunicate -->  other processes

hash: according to key to get location
dict: {key1:value1,...}          
set: {key1,key2,...}
key: key is const object, str, int,...  not all set can be key

one .py file is a module.
mycompany (package): every package has one __init__.py file. otherwise this package will be common directory not a package. 
├─ __init__.py: this file's name of module is mycompany.
├─ abc.py
└─ xyz.py

mycompany
 ├─ web
 │  ├─ __init__.py
 │  ├─ utils.py
 │  └─ www.py
 ├─ __init__.py
 ├─ abc.py
 └─ xyz.py

function parameters:
1.location parameters:
          
2.default parameters:
    def func(a,b=1):
        pass
    func(1)/ func(1,2)/ func(1,b=2)
    
    def appe(L=[]):
        L.append(1)
    L points to a const location, and it can be changed.
    
3.changable parameters:
    def cp(*numbers): numbers convert to a tuple
        pass
    cp(1,2,3,4)/ cp()
    L=[1,2,3]
    cp(*L)

4.keyword parameters:
    def person(name, age, **kw): kw converts to a dict
        pass
    person('Bob', 35, city='Beijing')/ person('Adam', 45, gender='M', job='Engineer')        
    extra = {'city': 'Beijing', 'job': 'Engineer'}
    person('Jack', 24, city=extra['city'], job=extra['job'])
    extra = {'city': 'Beijing', 'job': 'Engineer'}
    person('Jack', 24, **extra)











