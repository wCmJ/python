#Numbers: int, float, complex
print(type(1))
<class 'int'>
print(type(1.0))
<class 'float'>
print(type(1+2.0j))
<class 'complex'>

#list
print(type([]))
<class 'list'>


#tuple
print(type(()))
<class 'tuple'>

#strings
print(type('1'))
<class 'str'>

#set
print(type({1}))
<class 'set'>

#dictionary
print(type({}))
<class 'dict'>

#generator
print(type((x for x in range(1,10))))
<class 'generator'>
except: StopIteration

#function
<class 'function'>



'''
Iterable: 
    1.list, tuple, dict, set, str
        iter(list/tuple/dict/set/str)   --->    Iterator
                            
    
                            
    2.生成器   <----->    Iterator(can be invoked by next() and returned value one by one) 
        ||
      generator
        ||
    3.function with yield   <----->    Iterator
'''

'''
Actually, for in python is same as next().
for x in [1,2,3,4,5]:
    pass
    
equal with:
it = iter([1,2,3,4,5])
while True:
    try:
        x = next(it)
    except StopIteration:
        break
'''        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

