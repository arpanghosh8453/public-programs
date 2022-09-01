
import threading,time
def timer(name,delay,repeat):
    print "timer "+name+' started'
    while repeat>0:
        time.sleep(delay)
        print name+':'+str(time.ctime(time.time()))
        repeat -= 1
    print "timer "+name+' completed'
t1 = threading.Thread(target = timer,args = ('timer1',1,4))
t2 = threading.Thread(target = timer,args = ('timer2',1,3))
t3 = threading.Thread(target = timer,args = ('timer3',1.5,5))
t1.start()
t1.join()
time.sleep(0.5)
t2.start()
t2.join()
print threading.active_count()
print threading.enumerate()
print t2.is_alive()
time.sleep(0.5)
t3.start()
time.sleep(4)


