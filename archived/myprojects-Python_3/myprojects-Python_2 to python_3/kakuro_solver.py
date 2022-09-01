def digitsplit(num):
    broken = list(str(num))
    answer = []
    for i in broken:
        answer.append(int(i))
    return answer

def sumlist(numlist):
    answer = 0
    for num in numlist:
        answer = answer+int(num)
    return answer

def join_to_num(numlist):
    answer = 0
    for num in numlist:
        answer = (answer*10)+num
    return answer

def breaknum(number,part):
    if number>45 or part>9 :
        return []
    primary = list(range(1,10))[0:part]
    difference = number-sumlist(primary)
    if difference < 0 or sumlist(list(range(9,9-part,-1)))<number:
        return []
    if difference==0:
        return [primary]
    index = -1
    while difference>0:
        add = 9-primary[index]
        if difference<add:
            add = difference
        primary[index] = primary[index]+add
        difference -= add
        index -= 1
    start = join_to_num(primary)
    end = join_to_num(primary[::-1])
    mainlist = []
    superset = []
    for num in range(start,end+1,9):
        total = sumlist(digitsplit(num))
        if total != number:
            continue
        sublist = digitsplit(num)
        if 0 in sublist:
            continue
        if (len(set(sublist))==part)and(set(sublist)not in superset):
            mainlist.append(sublist)
            superset.append(set(sublist))
    return mainlist

#-------------------------------------------------------------------------------#



def dependence(index,mylist):
    global boxlen
    x = index
    try:
        while mylist[x-1] == '-' or type(mylist[x-1]) == int:
            x -= 1
    except:
        pass
    y = index
    try:
        while mylist[y-boxlen] == '-' or type(mylist[y-boxlen]) == int:
            y -= boxlen
    except:
        pass
    return (x-1),(y-boxlen)

def row_column(index,mylist):
    global boxlen
    rowindex = index
    row = 0
    try:
        while mylist[rowindex+1] == '-':
            row += 1
            rowindex += 1
            if rowindex+1>len(mylist)-1:
                break
    except:
        pass
    columnindex = index
    column = 0
    try:
        while mylist[columnindex+boxlen] == '-':
            column += 1
            columnindex += boxlen
            if (columnindex+boxlen)>(len(mylist)-1):
                break
    except:
        pass
    return row,column

def split_value(item):
    parts = item.split('\\')
    splitted = []
    for i in parts:
        if i is '':
            splitted.append(0)
        else:
            splitted.append(int(i))
    return splitted[0],splitted[1]

def createdict(mylist):
    valuedict = {}
    blankdict = {}
    index = 0
    for item in mylist:
        if item == '-':
            blankdict[index] = [dependence(index,mylist),list(range(1,10))]
        elif item == 'x' or item == 'X':
            item = item
        elif '\\' in item:
            row,column = row_column(index,mylist)
            splitted = split_value(item)
            valuedict[index] = [breaknum(splitted[0],column),breaknum(splitted[1],row)]
        else:
            raise Exception(item+" is not a valid item !")
        index += 1
    return blankdict,valuedict

#-------------------------------------------------------------------------------------------------------#            
        
def list_merge(superlist):
    merged = set([])
    for sublist in superlist:
        for value in sublist:
            merged.add(value)
    return list(merged)

def reset_valuedict(valuedict,xdepend,ydepend,value):
    xvalues = valuedict[xdepend][1]
    yvalues = valuedict[ydepend][0]
    newx = []
    newy = []
    for subx in xvalues:
        if value in subx:
            subx.remove(value)
            newx.append(subx)
    for suby in yvalues:
        if value in suby:
            suby.remove(value)
            newy.append(suby)
    valuedict[xdepend][1] = newx
    valuedict[ydepend][0] = newy
    return valuedict

def common_list(list1,list2):
    result = []
    for value in list1:
        if value in list2:
            result.append(value)
    return result

def check_blank_sum(mylist,valuedict,valueindex):
    global boxlen
    xsum = 0
    ysum = 0
    xblank = []
    yblank = []
    tempx = valueindex
    tempy = valueindex

    while mylist[tempx+1] == '-' or type(mylist[tempx+1]) == int:
        if type(mylist[tempx+1]) == str:
            xblank.append(tempx+1)
            
        else:
            xsum += mylist[tempx+1]
        tempx += 1
        if tempx + 1 > len(mylist)-1:
            break
    try:
        while (mylist[tempy+boxlen] == '-') or (type(mylist[tempy+boxlen])) == int:
            if type(mylist[tempy+boxlen]) == str:
                yblank.append(tempy+boxlen)
                
            else:
                ysum += mylist[tempy+boxlen]
            tempy += boxlen
    except Exception as e:
        pass
    return xblank,yblank,xsum,ysum
    

def check_all_box(blankdict,valuedict,mylist):
    global count
    for blankindex in list(blankdict.keys()):
        xdepend = blankdict[blankindex][0][0]
        ydepend = blankdict[blankindex][0][1]
        xpossible = list_merge(valuedict[xdepend][1])
        ypossible = list_merge(valuedict[ydepend][0])
        valuelist = common_list(xpossible,ypossible)
        blankdict[blankindex][1] = valuelist
        if len(valuelist) == 1:
            mylist[blankindex] = valuelist[0]
            del blankdict[blankindex]
            valuedict = reset_valuedict(valuedict,xdepend,ydepend,valuelist[0])
            print('.', end=' ')
            count += 1
        if len(valuelist) == 0:
            raise Exception("No number can stay in box number "+str(blankindex+1))
    for valueindex in list(valuedict.keys()):
        xblank,yblank,xsum,ysum = check_blank_sum(mylist,valuedict,valueindex)
        ytotal,xtotal = split_value(mylist[valueindex])
        if len(xblank) == 2:
            list1 = blankdict[xblank[0]][1]
            list2 = blankdict[xblank[1]][1]
            canstay = []
            for num in list1:
                if xtotal-(xsum+num) in list2:
                    canstay.append(num)
            if len(canstay) == 1:
                mylist[xblank[0]] = canstay[0]
                del blankdict[xblank[0]]
                valuedict = reset_valuedict(valuedict,dependence(xblank[0],mylist)[0],dependence(xblank[0],mylist)[1],canstay[0])
                count += 1
                print('.', end=' ')
        if len(yblank) == 2:
            list1 = blankdict[yblank[0]][1]
            list2 = blankdict[yblank[1]][1]
            canstay = []
            for num in list1:
                if ytotal-(ysum+num) in list2:
                    canstay.append(num)
            if len(canstay) == 1:
                mylist[yblank[0]] = canstay[0]
                del blankdict[yblank[0]]
                valuedict = reset_valuedict(valuedict,dependence(yblank[0],mylist)[0],dependence(yblank[0],mylist)[1],canstay[0])
                count += 1
                print('.', end=' ')
    return blankdict,valuedict,mylist

def print_list(mylist):
    global boxlen
    start = 0
    end = boxlen
    print("\n"+"+"*(boxlen*4)+"+")
    while end <= len(mylist):
        partlist = mylist[start:end]
        string1 = "|"
        for i in partlist:
            if "\\" in str(i):
                y,x = split_value(i)
                if len(str(x)) == 1:
                    x = str(x)+" "
                else:
                    x = str(x)
                x = "\\"+x+"|"
            else:
                x = "   |"
            string1 = string1+x
        string2 = "|"
        for i in partlist:
            if "\\" in str(i):
                x = " \ |"
            elif i == '-':
                x = " ? |"
            elif type(i) == int:
                x = " "+str(i)+" |"
            string2 = string2 + x
        string3 = "|"
        for i in partlist:
            if "\\" in str(i):
                y,x = split_value(i)
                if len(str(y)) == 1:
                    y = str(y)+" "
                else:
                    y = str(y)
                y = y+"\\"+"|"
            else:
                y = "   |"
            string3 = string3+y
        print(string1)
        print(string2)
        print(string3)
        print("+"*(boxlen*4)+"+")
        start += boxlen
        end += boxlen

boxlen = 10
count = 0
prevcount = 0
kakuro_dir = input("Enter the path of kakuro file : ")
kakurolist = [line.rstrip('\n') for line in open(kakuro_dir)]
print("Genareting Dictionaries...")
blankdict,valuedict = createdict(kakurolist)
print("Solving>>", end=' ')
#blankdict = {14: [(13, 4), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 15: [(13, 5), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 16: [(13, 6), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 18: [(17, 8), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 19: [(17, 9), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 21: [(20, 11), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 22: [(20, 12), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 23: [(20, 13), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 24: [(20, 4), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 25: [(20, 5), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 26: [(20, 6), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 28: [(27, 8), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 29: [(27, 9), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 31: [(30, 11), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 32: [(30, 12), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 33: [(30, 13), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 35: [(34, 5), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 36: [(34, 6), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 38: [(37, 8), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 39: [(37, 9), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 42: [(41, 12), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 43: [(41, 13), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 44: [(41, 34), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 46: [(45, 6), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 47: [(45, 37), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 48: [(45, 8), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 53: [(52, 13), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 54: [(52, 34), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 56: [(55, 6), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 57: [(55, 37), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 62: [(61, 52), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 63: [(61, 13), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 64: [(61, 34), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 66: [(65, 6), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 67: [(65, 37), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 68: [(65, 58), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 71: [(70, 61), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 72: [(70, 52), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 74: [(73, 34), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 75: [(73, 65), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 77: [(76, 37), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 78: [(76, 58), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 79: [(76, 69), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 81: [(80, 61), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 82: [(80, 52), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 84: [(83, 34), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 85: [(83, 65), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 86: [(83, 76), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 87: [(83, 37), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 88: [(83, 58), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 89: [(83, 69), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 91: [(90, 61), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 92: [(90, 52), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 94: [(93, 34), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 95: [(93, 65), [1, 2, 3, 4, 5, 6, 7, 8, 9]], 96: [(93, 76), [1, 2, 3, 4, 5, 6, 7, 8, 9]]}
#valuedict = {4: [[[5, 9], [6, 8]], [[]]], 5: [[[1, 3, 9], [1, 4, 8], [1, 5, 7], [2, 3, 8], [2, 4, 7], [2, 5, 6], [3, 4, 6]], [[]]], 6: [[[1, 4, 6, 7, 8, 9], [2, 3, 6, 7, 8, 9], [2, 4, 5, 7, 8, 9], [3, 4, 5, 6, 8, 9]], [[]]], 8: [[[1, 2, 3, 8], [1, 2, 4, 7], [1, 2, 5, 6], [1, 3, 4, 6], [2, 3, 4, 5]], [[]]], 9: [[[6, 8, 9]], [[]]], 11: [[[7, 9]], [[]]], 12: [[[1, 3, 9], [1, 4, 8], [1, 5, 7], [2, 3, 8], [2, 4, 7], [2, 5, 6], [3, 4, 6]], [[]]], 13: [[[1, 2, 3, 4, 7], [1, 2, 3, 5, 6]], [[1, 8, 9], [2, 7, 9], [3, 6, 9], [3, 7, 8], [4, 5, 9], [4, 6, 8], [5, 6, 7]]], 17: [[[]], [[3, 9], [4, 8], [5, 7]]], 20: [[[]], [[1, 2, 3, 4, 5, 7]]], 27: [[[]], [[1, 6], [2, 5], [3, 4]]], 30: [[[]], [[6, 8, 9]]], 34: [[[1, 2, 6, 7, 8, 9], [1, 3, 5, 7, 8, 9], [1, 4, 5, 6, 8, 9], [2, 3, 4, 7, 8, 9], [2, 3, 5, 6, 8, 9], [2, 4, 5, 6, 7, 9], [3, 4, 5, 6, 7, 8]], [[7, 9]]], 37: [[[1, 2, 7, 8, 9], [1, 3, 6, 8, 9], [1, 4, 5, 8, 9], [1, 4, 6, 7, 9], [1, 5, 6, 7, 8], [2, 3, 5, 8, 9], [2, 3, 6, 7, 9], [2, 4, 5, 7, 9], [2, 4, 6, 7, 8], [3, 4, 5, 6, 9], [3, 4, 5, 7, 8]], [[7, 9]]], 41: [[[]], [[1, 2, 7], [1, 3, 6], [1, 4, 5], [2, 3, 5]]], 45: [[[]], [[1, 6, 9], [1, 7, 8], [2, 5, 9], [2, 6, 8], [3, 4, 9], [3, 5, 8], [3, 6, 7], [4, 5, 7]]], 52: [[[1, 7, 8, 9], [2, 6, 8, 9], [3, 5, 8, 9], [3, 6, 7, 9], [4, 5, 7, 9], [4, 6, 7, 8]], [[1, 3]]], 55: [[[]], [[1, 3]]], 58: [[[1, 2, 4]], [[]]], 61: [[[1, 2, 3]], [[1, 2, 5], [1, 3, 4]]], 65: [[[1, 2, 5], [1, 3, 4]], [[4, 8, 9], [5, 7, 9], [6, 7, 8]]], 69: [[[1, 4], [2, 3]], [[]]], 70: [[[]], [[3, 9], [4, 8], [5, 7]]], 73: [[[]], [[2, 9], [3, 8], [4, 7], [5, 6]]], 76: [[[8, 9]], [[1, 2, 3]]], 80: [[[]], [[1, 9], [2, 8], [3, 7], [4, 6]]], 83: [[[]], [[1, 2, 3, 5, 8, 9], [1, 2, 3, 6, 7, 9], [1, 2, 4, 5, 7, 9], [1, 2, 4, 6, 7, 8], [1, 3, 4, 5, 6, 9], [1, 3, 4, 5, 7, 8], [2, 3, 4, 5, 6, 8]]], 90: [[[]], [[1, 6], [2, 5], [3, 4]]], 93: [[[]], [[5, 8, 9], [6, 7, 9]]]}
while True:
    blankdict,valuedict,kakurolist = check_all_box(blankdict,valuedict,kakurolist)
    if prevcount == count:
        break
    prevcount = count
    print("retrying")
    print("Solving>>", end=' ')
#print kakurolist
print('I have done',count,"boxes")
print_list(kakurolist)
xyz = input("Exit :")


'''
Genareting Dictionaries...
Solving>> . . . . . . . . . . . . . retrying
Solving>> . . . . . . . . . . . . . . retrying
Solving>> . . . . retrying
Solving>> . . retrying
Solving>> . . . retrying
Solving>> . . . . retrying
Solving>> . . . . retrying
Solving>> . . . . retrying
Solving>> . . . . retrying
Solving>> . . . retrying
Solving>> . retrying
Solving>> I have done 56 boxes

+++++++++++++++++++++++++++++++++++++++++
|   |   |   |   |\0 |\0 |\0 |   |\0 |\0 |
|\0 |\0 |\0 |\0 | \ | \ | \ | \ | \ | \ |
|   |   |   |   |14\|13\|35\|   |14\|23\|
+++++++++++++++++++++++++++++++++++++++++
|   |\0 |\0 |\18|   |   |   |\12|   |   |
|   | \ | \ | \ | 9 | 3 | 6 | \ | 4 | 8 |
|   |16\|13\|17\|   |   |   |0 \|   |   |
+++++++++++++++++++++++++++++++++++++++++
|\22|   |   |   |   |   |   |\7 |   |   |
| \ | 7 | 4 | 3 | 5 | 1 | 2 | \ | 1 | 6 |
|0 \|   |   |   |   |   |   |0 \|   |   |
+++++++++++++++++++++++++++++++++++++++++
|\23|   |   |   |\16|   |   |\16|   |   |
| \ | 9 | 8 | 6 | \ | 9 | 7 | \ | 7 | 9 |
|0 \|   |   |   |33\|   |   |27\|   |   |
+++++++++++++++++++++++++++++++++++++++++
|   |\10|   |   |   |\16|   |   |   |   |
|   | \ | 1 | 2 | 7 | \ | 8 | 6 | 2 | 2 |
|   |0 \|   |   |   |0 \|   |   |   |   |
+++++++++++++++++++++++++++++++++++++++++
|   |   |\4 |   |   |\4 |   |   |\0 |   |
|   |   | \ | 1 | 3 | \ | 3 | 1 | \ | \ |
|   |   |25\|   |   |0 \|   |   |7 \|   |
+++++++++++++++++++++++++++++++++++++++++
|   |\8 |   |   |   |\21|   |   |   |\0 |
|\0 | \ | 2 | 5 | 1 | \ | 9 | 8 | 4 | \ |
|   |6 \|   |   |   |8 \|   |   |   |5 \|
+++++++++++++++++++++++++++++++++++++++++
|\12|   |   |\11|   |   |\6 |   |   |   |
| \ | 3 | 9 | \ | 9 | 2 | \ | 3 | 1 | 2 |
|0 \|   |   |0 \|   |   |17\|   |   |   |
+++++++++++++++++++++++++++++++++++++++++
|\10|   |   |\28|   |   |   |   |   |   |
| \ | 2 | 8 | \ | 5 | 1 | 8 | 9 | 2 | 3 |
|0 \|   |   |0 \|   |   |   |   |   |   |
+++++++++++++++++++++++++++++++++++++++++
|\7 |   |   |\22|   |   |   |   |   |   |
| \ | 1 | 6 | \ | 8 | 5 | 9 | 9 | 9 | 9 |
|0 \|   |   |0 \|   |   |   |   |   |   |
+++++++++++++++++++++++++++++++++++++++++
Exit :
'''
