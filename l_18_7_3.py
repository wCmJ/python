#!/usr/bin/env python3
# -*- coding:utf-8 -*-

di={'a':1,'b':2,'c':3}
for v in di:
    print(v)  # a b c
for v in di.values():
    print(v)  #1 2 3    
for k,v in di.items():
    print(k,v)  #a 1    b 2    c 3
    
    
li=[1,2,3,4]
for i in li:
    print(i)    #1 2 3 4
for i,value in enumerate(li):    #enumerate make list to index-value
    print(i,value)  #1 1    2 2     3 3     4 4
#same as tuple

from collections import Iterable
isinstance(123,Iterable)

#list comprehensions
list(range(1,11))
[x*x for x in range(1,11)]  #1,4,16,....,100
[x*x for x in range(1,11) if x % 2 == 0]    #4,16,36,64,100
[m+n for m in 'ABC' for n in 'XYZ'] #'AX','AY',...,'CZ'

import os
[d for d in os.listdir('.')] #get files and directorys









