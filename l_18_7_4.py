#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#generator method1
g=(x*x for x in range(1,11) if x % 2 == 0)
for n in g:
    print(n)

#generator method2
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1 
    return 'done'
#if function contains 'yield', it is generator.
f=fib(6)

#if you want to get value of return, catch 'StopIteration'
while True：
    try:
        x=next(f)
        print(x)
    except StopIteration as e:
        print(e.value)










