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



























