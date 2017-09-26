def mean(*values):
    sumvalue = 0
    length = len(values)
    try:
        for i in values:
            sumvalue = sumvalue + i
        return (sumvalue/length)
    except:
        print('Error in values...')
        return None

def median(*values):
    try:
        length = len(values)-1
        listval = list(values) 
        listval.sort()
        if length % 2 == 0:
            return listval[int(length/2)]
        else:
            half = int(length/2)
            return ((listval[half]+listval[half + 1])/2)
    except:
        print('Error in values...')
        return None

def mode(*values):
    try:
        listval = list(values)
        count = 0
        for i in listval:
            if listval.count(i) > count:
                count = listval.count(i)
                grater = i
        return grater
    except:
        print('Error in values...')
        return None

print(mean(2,4))      
            
