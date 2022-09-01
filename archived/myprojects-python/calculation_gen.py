import random


def seq_gen(start, end, count):
    seq = str(random.randint(start, end))
    for i in range(count-1):
        symbol = random.choice(['+','-','*','/'])
        entry = str(random.randint(start, end))
        seq = seq+symbol+entry
        print '.',
        if i%1000 == 0 :
            print 'Working..Please wait'
    return seq


start = int(raw_input("Enter the starting value : "))
end = int(raw_input("Enter the endting value : "))
count = int(raw_input("Enter the count value : "))
path = raw_input("Enter the filepath to create the new file(in .py extention) : ")

filename = file(path,'w')
filename.write("from datetime import datetime\n")
filename.write("print 'Calculating...Please Wait...'\n")
filename.write("initial = datetime.now()\n")
filename.write("x = "+seq_gen(start,end,count)+"\n")
filename.write("print 'Result :',x\n")
filename.write("final = datetime.now()\n")
filename.write("print 'Execution Time :',final-initial\n")
filename.write("y = raw_input('Press Enter : ')")
filename.close()
