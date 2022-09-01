count = int(raw_input("Enter the number of number :"))
a = c = 0
b = 1
if count>0:
    while count>1:
        c = a + b
        a,b = b,c
        print c
        count -= 1
x = raw_input("Enter to exit :")
        
