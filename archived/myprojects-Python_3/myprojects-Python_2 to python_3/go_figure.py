import time
def startfunc():
    import datetime
    import time
    global myflag
    myflag = 0
    def enter():
        flag = 1
        while flag == 1:
            try:
                n1 = eval(input("Enter the first number :"))
                if type(n1) is not int:
                    raise Exception("error!")
                flag = 0
            except:
                print("Please enter a correct value!")
                flag = 1
        flag = 1
        while flag == 1:
            try:
                n2 = eval(input("Enter the second number :"))
                if type(n2) is not int:
                    raise Exception("error!")
                flag = 0
            except:
                print("Please enter a correct value!")
                flag = 1
        flag = 1
        while flag == 1:
            try:
                n3 = eval(input("Enter the third number :"))
                if type(n3) is not int:
                    raise Exception("error!")
                flag = 0
            except:
                print("Please enter a correct value!")
                flag = 1
        flag = 1
        while flag == 1:
            try:
                n4 = eval(input("Enter the forth number :"))
                if type(n4) is not int:
                    raise Exception("error!")
                flag = 0
            except:
                print("Please enter a correct value!")
                flag = 1
        flag = 1
        while flag == 1:
            try:
                r = eval(input("Enter the result :"))
                if type(r) is not int:
                    raise Exception("error!")
                flag = 0
            except:
                print("Please enter a correct value!")
                flag = 1
        return [n1,n2,n3,n4,r]



    def opr(n1,n2,s):
        if s == '+':
            r = (n1+n2)
            myflag = 1
        elif s == '-':
            r = (n1-n2)
            myflag = 1
        elif s == '*':
            r = (n1*n2)
            myflag = 1
        elif s == '/':
            if n2 == 0:
                myflag = 0
            else:
                r = (float(n1)/n2)
                myflag = 1
                
        if myflag:
            pass
        else:
            raise ValueError("Error!")
        return r
    numlist = enter()
    start = datetime.datetime.now()
    count = 0
    numindex = [4321,4312,4231,4213,4132,4123,3421,3412,3214,3241,3142,3124,2431,2413,2341,2314,2134,2134,1423,1432,1342,1324,1243,1234]
    oprlist = []
    los = ['+','-','*','/']
    for i in los:
        for j in los:
            for k in los:
                oprlist.append(i+j+k)
    for i in numindex:
        a = numlist[(i%10)-1]
        b = numlist[((i//10)%10)-1]
        c = numlist[((i//100)%10)-1]
        d = numlist[((i//1000)%10)-1]
        for x in oprlist:
            try:
                if numlist[4] == opr(opr(opr(a,b,x[0]),c,x[1]),d,x[2]):
                    print(numlist[4],"=","[","{","(",a,x[0],b,")",x[1],c,"}",x[2],d,"]")
                    count += 1
            except:
                pass
            try:
                if numlist[4] == opr(opr(a,b,x[0]),opr(c,d,x[2]),x[1]):
                    print(numlist[4],"=","{","(",a,x[0],b,")",x[1],"(",c,x[2],d,")","}")
                    count += 1
            except:
                pass
            try:
                if numlist[4] == opr(opr(a,opr(b,c,x[1]),x[0]),d,x[2]):
                    print(numlist[4],"=","[","{",a,x[0],"(",b,x[1],c,")","}",x[2],d,"]")
                    count += 1
            except:
                pass
            try:
                if numlist[4] == opr(a,opr(opr(b,c,x[1]),d,x[2]),x[0]):
                    print(numlist[4],"=","[",a,x[0],"{","(",b,x[1],c,")",x[2],d,"}","]")
                    count += 1
            except:
                pass
            try:
                if numlist[4] == opr(a,opr(b,opr(c,d,x[2]),x[1]),x[0]):
                    print(numlist[4],"=","[",a,x[0],"{",b,x[1],"(",c,x[2],d,")","}","]")
                    count += 1
            except:
                pass
    print(count,"results found!!")
    end = datetime.datetime.now()
    print("Time taken :",(end-start))
startfunc()
while True:
    try:
        check = eval(input("Enter 0 to stop & 1 to restart :"))
        if check == 1:
            startfunc()
        elif check == 0:
            print("Program terminated!")
            break
        else:
            raise Exception("error!")
    except:
        print("Please enter 1 or 0!!")
time.sleep(1)
exit()

    

