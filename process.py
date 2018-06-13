#1
import os
pid=os.fork() # fork in unix/linux, windows donot include
if pid==0:
    print(os.getpid(),os.getppid())

#2
from multiprocessing import Process
import os
def run_proc(name):
    print('Run child process %s (%s)...' % (name,os.getpid()))
if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p=Process(target=run_proc,args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

#3
from multiprocessing import Pool
import os,time,random
def long_time_task(name):
    print('get time of creating process')  
if __name__=='__main__':
    p=Pool()                                   #default is same as numbers of CPU
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    p.close()
    p.join()
    

#4
import subprocess
r=subprocess.call(['nslookup','www.python.org'])

output:
Server:  bjgwpdc01p.polycom.com
Address:  10.250.102.30

Non-authoritative answer:
Name:    dualstack.python.map.fastly.net
Addresses:  2a04:4e42:2::223
          151.101.8.223
Aliases:  www.python.org


#5 subprocess input
import subprocess
p=subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output, err=p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
set q=mx python.org exit


#6
from multiprocessing import Process, Queue
import os,time,random
def write(q):
    for value in ['A','B','C']:
        q.put(value)
        time.sleep(random.random())
def read(q):
    while True:
        value=q.get(True)
if __name=='__main__':
    q=Queue()
    pw=Process(target=write,args=(q,))
    pr=Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
        
        
#7
#_thread and threading are two modules in python. threading is higher level module. 
import threading, time
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n=0
    while n<5:
        n=n+1
        print('thread %s >>> %s' % (threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)
print('thread %s is running...' % threading.current_thread().name)
t=threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)


#8
#GIL(Global Interpreter Lock): for every thread. thread should get GIL before execute. then it will release GIL when 100 lines of code execute.
#python can achieve multicore task with multiprocess, each has its own GIL.



































