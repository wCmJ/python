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

































