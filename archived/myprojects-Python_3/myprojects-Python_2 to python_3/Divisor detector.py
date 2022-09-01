import time
i=eval(input("Enter the number :"))
s = 1
e = (i//2)+2
l = []
while e>=s :
    if i%s == 0 :
        l.append(s)
    s += 1
l.append(i)    
print("Total divisors :",len(l))
print(l)
time.sleep(10)
