print "\n\n ** WELCOME TO THE PELMUTER CREATED BY ARPAN GHOSH....\n\n"
def pelmute(values,max_len='',repeat=False,must_occure=[]):
    values = list(values)
    if max_len == '':
        max_len = len(values)
    if repeat == True:
        indexstr = [0]*max_len
    else:
        indexstr = range(max_len)
    global alllist
    alllist = []
    while True:
        result = ''
        for index in indexstr:
            result += values[int(index)]
        flag = True
        if repeat == False:
            for i in values:
                if values.count(i)<list(result).count(i):
                    flag = False
                    break
                else:
                    flag = True
        if flag == True:
            for i in must_occure:
                if i not in result:
                    flag = False
                    break
                else:
                    flag = True
        if (flag == True) and (result not in alllist):
            yield result
            alllist.append(result)
        if indexstr == [max_len-1]*max_len:
            break

        #-------------------------Continuing--------------------------------------

        check = True
        indexgen = []
        for i in indexstr[::-1]:
            if int(i) < (len(values)-1) and check == True:
                indexgen.append(i+1)
                check = False
            elif check == True:
                indexgen.append(0)
            else:
                indexgen.append(i)
        indexstr = indexgen[::-1]



string = raw_input("Enter the string to pelmute :")
length = int(raw_input("Enter the length of resulting permutions :"))
repeat = raw_input("Repeat the values for permutation ? (y/n) :")
always_occures = input("Enter values that must occure as strings in a list (i.e.>> ['ab','dc'...] ,if nothing to give, Enter : []) :")
filename = raw_input("Enter the full file path (i.e. >> D:/Permutation_results.txt) : ")

if repeat == 'y' or repeat == 'Y':
    repeat = True
else:
    repeat = False
        
if always_occures == '':
    must_occure = []
    always_occures = []
else:   
    must_occure = list(set(list(''.join(always_occures))))
    
if filename == '':
    filename = "D://Permutation_results.txt"
print "\n\nPrinting the results : ......\n\n"           
generator = pelmute(string,length,repeat,must_occure)
filehandle = file(filename,'w')
for item in generator:
    flag = True
    for occurence in always_occures:
        if occurence not in item:
            flag = False
            break
    if flag:
        filehandle.write(item+'\n')
        print item,
  
filehandle.close()

print "\n\nTotal Results Found : ",len(alllist)


