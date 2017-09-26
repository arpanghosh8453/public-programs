import os
os.chdir("C:\\Users\\arpan\\Desktop")

filename = file('prime.txt','a')

f = input("Enter the starting number :")
e = input("Enter the ending number : ")
l = [2]
num = 2
prime = []
while e>=num :
    c = (num//2)+2
    for i in l:
        if num%i>0 or num==2:
            err = 1
        else:
            err = 0
            break
        if i>c:break
    if err:
        if num != 2:l.append(num)
        if num>= f:
            prime.append(num)
            print num,
    num += 1
    if num%2 == 0:num+=1
print ""
print "Number in range :",len(prime)
print "Number in total count:",len(l)
filename.write(str(prime))
filename.close()
i = input("ESC :")

