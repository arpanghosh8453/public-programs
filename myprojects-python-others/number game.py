import random
def numguess(digit):
    if digit>1 and digit<10:
        l = range(1,10)
        random.shuffle(l)
        i = n = 0
        l.insert(random.randint(1,9),0)
        while digit>i:
            n = (n*10)+l[i]
            i += 1
        return n
    else:
        raise ValueError("Digit must be between 1 to 9")
        
def checknum(num):
    for a in str(num):
        if str(num).count(a)>1:
            raise ValueError("Digit must contain single digit ")
        elif int(a) not in range(0,10):
            raise ValueError("number cannot contain any non-digit value")
        else:
            pass

d = input("Enter the digit count :")
num = numguess(d)
print "Number is Guessed"
chance = input("Enter the chance count :")
for i in range(chance):
    x =y =z=0
    c = input("Enter your Guess :")
    if c == num:
        print "You have WON!!"
        break
    checknum(c)
    if len(str(c))==d:
        for b in str(c):
            for e in str(num):
                if e==b:
                    if str(num).find(e)==str(c).find(b):
                        x += 1
                    else:
                        y += 1
                    break
            else:
                z += 1
    else:
        raise ValueError("Digit limit crossed or less..")
    print "Correctplace :",x,"Wrongplaces :",y,"Errorguess :",z
else:
    print "You have lost the game!!"
print "The number was :",num


