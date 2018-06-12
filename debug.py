#print
  
#assert
n=0
assert n != 0, 'n is zero!'
#python debug.py will execute assert.
#python -O debug.py will discard assert, treat it as pass. -O will close assert.

#logging
import logging
#specify level of debug
logging.basicConfig(level=logging.INFO/DEBUG/ERROR/WARNING)
logging.info/debug/error/warning('n=%d' % n)

#pdb
import pdb
#python -m pdb debug.py
#l check code
#p variable check value
#n run line by line
#q quit pdb

pdb.set_trace()
#python debug.py
#p variable 
#c continue to run

