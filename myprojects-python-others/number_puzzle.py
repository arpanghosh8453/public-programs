import random
from datetime import datetime
count = 0
wonthegame = False
while True:
    try:
        length = int(input("Enter the length of the box :"))
        if length>1 and length<21:
            end = (length **2)
            endlen = len(str(end-1))
            blank = "_"*endlen
            l1 = []
            l2 = []
            for i in range(1,end):
                d = endlen - len(str(i))
                p = (" "*d)+str(i)
                l1.append(p)
                l2.append(p)
            while l1 == l2:
                random.shuffle(l1)
            l1.append(blank)
            l2.append(blank)
            flag = 1
            timer_init = datetime.now()
            while True:
                if flag:
                    print "\n","-"*(length*(endlen+1)),"\n"
                    for my_list in range(end):
                        print l1[my_list],
                        if (my_list + 1)%length == 0:
                            print ""
                    print "\n","-"*(length*(endlen+1)),"\n"
                    print "Chance taken :",count
                if l1 == l2:
                    print "You have WON the game!!"
                    print 'Time taken: '+ str(datetime.now()-timer_init)
                    wonthegame = True
                    break
                else:
                    
                    try:
                        num = input("Enter a proper number to move :")
                        if type(num) is oct or type(num) is hex:
                            raise ValueError("Input Error!")
                        else:
                            int(num)
                        if num<end:
                            d = endlen - len(str(num))
                            m = (" "*d)+str(num)
                            sp = l1.index(blank)
                            if sp%length == 0:
                                check = [(sp+length),(sp-length),(sp +1)]
                            elif (sp+1)%length == 0:
                                check = [(sp+length),(sp-length),(sp-1)]
                            else:
                                check = [(sp+length),(sp-length),(sp +1),(sp-1)]
                            for c in check:
                                if c in range(end):
                                    if l1[c] == m:
                                        l1[sp] = m
                                        l1[c] = blank
                                        count += 1
                                        print "Action Performed!"
                                        flag = 1
                                        break
                            else:
                                print "Movement can't be performed!"
                                flag = 0
                        else:
                            print "Invalid input!"
                            flag = 0
                    except:
                        print "Please enter a number!"
                        flag = 0
        else:
            print "length is out of range!!SORRY!!"

    except:
        print "Please enter a range between 1 to 20"
    if wonthegame:
        break
