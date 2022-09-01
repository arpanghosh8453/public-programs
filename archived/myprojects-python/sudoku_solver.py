
#------------------------------------------sample-sudoku ----------------------------------------------
'''
mainlist = ['-', '-', 4, '-', '-', '-', 6, '-', '-',
            8, 5, '-', '-', '-', '-', '-', 2, 1,
            '-', '-', 1, 6, '-', 7, 9, '-', '-',
            '-', 6, '-', 5, '-', 8, '-', 9, '-',
            '-', 4, '-', 9, '-', 2, '-', 6, '-',
            '-', 9, '-', 3, '-', 1, '-', 7, '-',
            '-', '-', 2, 1, '-', 4, 5, '-', '-',
            7, 1, '-', '-', '-', '-', '-', 4, 6,
            '-', '-', 5, '-', '-', '-', 8, '-', '-']

'''
#-------------------------------------------sample-sudoku-----------------------
'''
mainlist = [3, '-', '-', 8, '-', 7, '-', 4, 1,
            '-', '-', '-', '-', 1, 6, 3, 8, '-',
            1, '-', 8, 3, '-', '-', 5, 7, '-',
            8, 2, 7, 9, '-', '-', '-', '-', '-',
            '-', 3, 1, 7, '-', 8, '-', 2, '-',
            '-', '-', '-', '-', '-', 1, 8, 3, 7,
            '-', 8, 4, 1, '-', '-', 2, '-', '-',
            2, '-', 9, 6, 8, '-', '-', '-', '-',
            6, 1, 3, 4, '-', '-', '-', '-', 8]


'''
#--------------------------------prints the sudoku in boxes-----------------------------------------------
def printer(l):
    print "\n","-"*25
    for number in range(81):
        print l[number],
        if number%3 == 2:
            print " ",
        if number%9 == 8:
            print ""
        if number%27 == 26:
            print "\n",
    print "-"*25
#-------------------------checks if a number can stay in a specific place---------------------------
def canstay(l,pos,num):
    rem=pos%9
    if rem==0:
        horstart=pos
    else:
        horstart=(pos-rem)
    horange=range(horstart,horstart+9)
    mainbox = [[0,1,2,9,10,11,18,19,20],[3,4,5,12,13,14,21,22,23],[6,7,8,15,16,17,24,25,26],[27,28,29,36,37,38,45,46,47],[30,31,32,39,40,41,48,49,50],[33,34,35,42,43,44,51,52,53],[54,55,56,63,64,65,72,73,74],[57,58,59,66,67,68,75,76,77],[60,61,62,69,70,71,78,79,80]]
    for subbox in mainbox:
        if pos in subbox:
            subbox.remove(pos)
            break
    if rem==0:
        varrange=range(0,81,9)
    else:
        varrange=range(rem,81,9)
    horange.remove(pos)
    varrange.remove(pos)
    totalrange=horange+varrange+subbox
    for index in totalrange:
        if num==l[index]:
            return False
        
    else:
        return True
#---------------finds blank and remaining numberss in a given subbox-------------------        
def blankrestfinder(subbox,l):
    fillist = []
    blanklist = []
    restlist = []
    for index in subbox:
        if l[index] == '-':
            blanklist.append(index)
        else:
            fillist.append(l[index])
    for num in range(1,10):
        if num not in fillist:
            restlist.append(num)
    return blanklist,restlist
#------------------sorts possible combinations given by rangelogic----------------
def sorter(numlist,possible):
    numlist.sort()
    fixed = ""
    for i in numlist:
        fixed = fixed + str(i)
    num = int(fixed)
    end = int(fixed[::-1])
    sort = []
    while end>= num:
        for i in fixed:
            if i not in str(num):
                break
            if int(i) not in possible[str(num).find(i)]:
                break
        else:
            sort.append(str(num))
        num += 9
    return sort
#------------------finds and replaces values from sorted combinations----------------------
def rangelogic(l,indexlist):
    blanklist,numlist = blankrestfinder(indexlist,l)
    if numlist == []:
        return l
    possible = []
    for index in blanklist:
        pos = []
        for num in range(1,10):
            if canstay(l,index,num):
                pos.append(num)
        possible.append(pos)
    comblist = sorter(numlist,possible)
    for digit in comblist[0]:
        place = comblist[0].find(digit)
        for num in comblist:
            if num.find(digit) != place:
                break
        else:
            position = blanklist[place]
            l[position] = int(digit)
            print ".",
    return l

#--------------------replaces values if it has only one place to seat-----------------------
def replacer(l,blanklist,num):
    possible = []
    for blank in blanklist:
        if canstay(l,blank,num):
            possible.append(blank)
        if len(possible)>1:
            break
    if len(possible) == 1:
            l[possible[0]] = num
            blanklist.remove(possible[0])
            print ".",
    return l,blanklist
#-------------------calls replacer and passes blankindexs and values---------------------
def fill(l,indexlist):
    blanklist,restlist = blankrestfinder(indexlist,l)
    if len(blanklist)>0:
        for number in restlist:
            l,blanklist = replacer(l,blanklist,number)
    return l
#--------genarates row and column indexlist and passes to fill for checking---------------------
def replaceline(l,flag):
    for index in range(0,9):
        rowlist = range(index,81,9)
        l = fill(l,rowlist)
        if flag == 'hard':
            l = rangelogic(l,rowlist)
    for index in range(0,81,9):
        columnlist = range(index,index+9)
        l = fill(l,columnlist)
        if flag == 'hard':
            l = rangelogic(l,columnlist)
    return l
#------------------------checks all blankplace if only one value is possible---------------------------
def checkall(l):
    for index in range(81):
        if l[index] == '-':
            possible = []
            for number in range(1,10):
                if canstay(l,index,number):
                    possible.append(number)
            if len(possible) == 1:
                l[index] = possible[0]
            if len(possible) == 0:
                printer(l)
                print "error found in index number ",+ str(index)
                x = raw_input("Wrong values found!! Press ENTER to EXIT!>>>")
                exit()
    return l
#--------------------passes the mainlist to other functions for solving-----------------------
def solver(mainbox,l,flag):
    for subbox in mainbox:
        l = fill(l,subbox)
        if flag == 'hard':
            l = rangelogic(l,subbox)
    l = checkall(l)
    l = replaceline(l,flag)
    return l
#--------------calls solver-----checks if solved-----conducts the whole process-------------------
def main(l,flag):
    mainbox = [[0,1,2,9,10,11,18,19,20],
               [3,4,5,12,13,14,21,22,23],
               [6,7,8,15,16,17,24,25,26],
               [27,28,29,36,37,38,45,46,47],
               [30,31,32,39,40,41,48,49,50],
               [33,34,35,42,43,44,51,52,53],
               [54,55,56,63,64,65,72,73,74],
               [57,58,59,66,67,68,75,76,77],
               [60,61,62,69,70,71,78,79,80]]
    
    prevlist = list(l)
    print "Solving->>",
    newlist = solver(mainbox,l,flag)
    while True:
        newlist = solver(mainbox,newlist,flag)
        if '-' not in newlist:
            print "Solved!"
            break
        if newlist == prevlist:
            print "I cannot solve anymore....SORRY!!"
            break
        prevlist = list(newlist)
        print 'Restarting',
    return newlist
#------------------------------takes input from the user--------------------------------------
def takeinput():
    inputlist = []
    while len(inputlist)<81:
        try:
            inp = raw_input("Enter the value number "+str(len(inputlist)+1)+" : ")
            if inp == 'x':
                inputlist.append('-')
            elif int(inp) in range(1,10):
                inputlist.append(int(inp))
            else:
                raise Exception("Error!")
        except:
            print "Please enter a correct value or 'x' if value is unknown!!"
    return inputlist
#--------------------------------the programme starts-------------------------------------
print "Welcome to the sudoku solver!!\nEnter the given values serialy.if the value is blank or unknown,Enter simply 'x'\nLet's start.....\n"
mainlist = takeinput()#takes input
print "\nYour sudoku looks like this...."
printer(mainlist)#prints the user given list of values
x = raw_input("\nAre you sure?? Press enter to start solving->....\n")
solved = main(mainlist,'easy')#solves in easy mode
printer(solved)#prints the easy mode solvedlist
if '-' in solved:#if not solved......
    print "\nShifting to harder mode....\n"
    print "Swithing to advance algorithm....\n"
    print "Checking all posibilities....\n"
    print "This process may take some time.....PLEASE WAIT....\n"
    solvedagain = main(solved,'hard')#solves in harder mode
    printer(solvedagain)#prints the hard mode solvedlist
print "GoodBye!!"
x = raw_input("Press  Enter to exit:")#pauses the script from closing









        












            

    
