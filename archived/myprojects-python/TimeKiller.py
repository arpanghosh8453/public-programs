import threading,time

def first():
    global num,flag
    num = 0
    flag = True
    while flag:
        num += 1
        print num

def stopper(delay):
    global flag
    print "stopper started"
    time.sleep(delay)
    print "\ntime is up\n"+str(delay)+" second(s) passed !! \n"
    flag = False
    x = raw_input("Enter to Exit :")
    
def main():
    delay = int(raw_input("input delay in seconds :"))
    t1 = threading.Thread(target = first,name = "firstThread")
    t2 = threading.Thread(target = stopper,name = "stopperThread",args = (delay,))
    t1.start()
    t2.start()

main()


        
