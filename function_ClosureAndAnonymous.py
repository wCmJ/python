#function as return 
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1,3,5,7,9)
f
#<function lazy_sum........>
f()
#25
#sum keeps parameters and variables of lazy_sum.
#every time lazy_sum will return different function.


def createCounter():
    n = [0]
    def counter():
        n[0] = n[0] + 1
        return n[0]
    return counter
cA = createCounter()
print(cA(), cA(), cA(), cA())   # 1 2 3 4
cB = createCounter()
print(cB(), cB(), cB(), cB())   # 1 2 3 4

s = 0 
def createCounter():
    def counter():
        global s
        s = s + 1
        return s
    return counter
cA = createCounter()
print(cA(), cA(), cA(), cA())   # 1 2 3 4
cB = createCounter()
print(cB(), cB(), cB(), cB())   # 5 6 7 8


#   lambda x: x * x
#   same as
def f(x):
    return x * x
#   lambda means anonymous function.
#   lambda has only one expression


















