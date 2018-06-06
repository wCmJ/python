#tye...except...finally
try:
    print('try...')
    r=10/0
    print('result:',r)
except ZeroDivisionError as e:
    print('except:',e)
finally:
    print('finally')
print('END')

try:
    pass
except ValueError as e:
    pass
except ZeroDivisionError as e:
    print('ZeroDivisionError',e)
finally:
    print('finally...')
print('END')

try:
    pass
except ValueError as e:
    pass
except ZeroDivisionError as e:
    print('ZeroDivisionError',e)
else:
    pass
finally:
    print('finally...')
print('END')


#Error record

import logging
try:
    pass
except Exception as e:
    logging.exception(e)

#Raise Error

raise ValueError('input error')


#the following are totally acceptable in python:
#passing a string representation of an integer into int     int('5')
#passing a string representation of a float into float      float('5.1')
#passing a string representation of an integer into float   float('5')
#passing a float into int                                   int(5.1)
#passing an integer into float                              float(5)

